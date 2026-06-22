from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SECTION_GLOB = "part-*/*/section-*.html"
CODE_RE = re.compile(
    r'(<pre><code[^>]*class="[^"]*(?:language-python|lang-python)[^"]*"[^>]*>)([\s\S]*?)(</code></pre>)',
    re.IGNORECASE,
)


def decode_code(block: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", block))


def encode_code(code: str) -> str:
    return (
        html.escape(code, quote=False)
        .replace("'", "&#x27;")
    )


def snake(name: str) -> str:
    name = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    return name.lower()


def sample_value(field_name: str, annotation: str) -> str:
    low_name = field_name.lower()
    ann = annotation.strip().lower()
    if "bool" in ann:
        return "True"
    if "int" in ann:
        return "30" if "hz" in low_name or "fps" in low_name else "1"
    if "float" in ann:
        return "0.75"
    if "tuple" in ann:
        if "int" in ann:
            return "(0, 1, 2)"
        return '("baseline", "stress")'
    if "list" in ann:
        return '["success_rate", "safety_cost"]'
    if "dict" in ann:
        return '{"split": "train"}'
    defaults = {
        "robot": '"mobile_manipulator"',
        "observation": '"front_rgbd plus proprioception"',
        "action": '"delta_end_effector_pose"',
        "demonstrator": '"teleop"',
        "split": '"train"',
        "license": '"CC-BY-4.0"',
        "metric": '"success_rate"',
        "section": '"example"',
        "tool": '"PyTorch"',
        "panel": '"heldout_objects"',
        "task": '"pick_place"',
        "simulator": '"ManiSkill3"',
        "wrapper": '"rgbd_observation"',
    }
    return defaults.get(low_name, f'"{field_name}_example"')


def add_as_row_method(code: str) -> str:
    if "def as_row(" in code:
        return code
    lines = code.splitlines()
    class_idx = next((i for i, line in enumerate(lines) if re.match(r"\s*class\s+\w+", line)), None)
    if class_idx is None:
        return code
    insert_idx = class_idx + 1
    while insert_idx < len(lines):
        line = lines[insert_idx]
        if line.strip() and not line.startswith((" ", "\t")):
            break
        insert_idx += 1
    is_pydantic = "BaseModel" in code
    body = [
        "    def as_row(self) -> dict[str, object]:",
        "        return self.model_dump()" if is_pydantic else "        return asdict(self)",
        "",
    ]
    lines[insert_idx:insert_idx] = body
    return "\n".join(lines)


def add_sample_usage(code: str) -> str:
    if "print(" in code or ".model_dump(" in code or "asdict(" in code:
        return code
    class_match = re.search(r"class\s+(\w+)\s*\(", code) or re.search(r"class\s+(\w+)\s*:", code)
    if not class_match:
        return code
    class_name = class_match.group(1)
    fields = re.findall(r"^\s+(\w+)\s*:\s*([^\n=]+)", code, re.MULTILINE)
    if not fields:
        return code
    instance_name = snake(class_name)
    args = ",\n".join(f"    {name}={sample_value(name, ann)}" for name, ann in fields)
    suffix = (
        f"\n{instance_name} = {class_name}(\n{args}\n)\n"
        f"print({instance_name}.as_row())"
    )
    return code.rstrip() + "\n" + suffix


def transform_dataclass_block(code: str) -> str:
    if ("@dataclass" not in code and "BaseModel" not in code) or "def " in code:
        return code
    updated = add_as_row_method(code)
    updated = re.sub(r"print\(asdict\((\w+)\)\)", r"print(\1.as_row())", updated)
    updated = re.sub(r"=\s*asdict\((\w+)\)", r"= \1.as_row()", updated)
    updated = re.sub(r"\[asdict\((\w+)\)\s+for", r"[\1.as_row() for", updated)
    updated = re.sub(r"print\((\w+)\.model_dump\(\)\)", r"print(\1.as_row())", updated)
    updated = updated.replace(".model_dump() for", ".as_row() for")
    updated = add_sample_usage(updated)
    return updated


def transform_contract_scaffold(code: str) -> str:
    src = (
        'contract = {"observation": "", "action": "", "metric": "", "perturbation": ""}\n'
        "print(contract)"
    )
    if src not in code:
        return code
    dst = (
        'contract = {"observation": "", "action": "", "metric": "", "perturbation": ""}\n\n'
        'def missing_contract_fields(payload: dict[str, str]) -> dict[str, object]:\n'
        '    missing = [key for key, value in payload.items() if value == ""]\n'
        '    return {"contract": payload, "missing_fields": missing}\n\n'
        "print(missing_contract_fields(contract))"
    )
    return code.replace(src, dst)


def transform_baseline_like(code: str, var_name: str) -> str:
    pattern = re.compile(rf"({var_name}\s*=\s*\{{[\s\S]*?\}})\nprint\({var_name}\)")
    match = pattern.search(code)
    if not match:
        return code
    replacement = (
        f"{match.group(1)}\n\n"
        f"def summarize_{var_name}(payload: dict[str, object]) -> dict[str, object]:\n"
        f'    missing = sorted(key for key, value in payload.items() if value in ("TODO", 0.0, "", None))\n'
        f'    return {{"record": payload, "missing_fields": missing}}\n\n'
        f"print(summarize_{var_name}({var_name}))"
    )
    return pattern.sub(replacement, code, count=1)


def transform_single_dict_print(code: str) -> str:
    if "def " in code or "class " in code:
        return code
    # keep numerical or thresholding examples alone
    if any(token in code for token in (" + ", " - ", " * ", " / ", ">=", "<=", " and ", " or ")):
        return code
    match = re.search(r"^(\w+)\s*=\s*\{[\s\S]*?\n\}\nprint\(\1\)\s*$", code.strip(), re.MULTILINE)
    if not match:
        return code
    var_name = match.group(1)
    replacement = (
        f"def validate_{var_name}(payload: dict[str, object]) -> dict[str, object]:\n"
        f"    assert payload, \"payload must not be empty\"\n"
        f"    return payload\n\n"
        + code.strip().replace(f"print({var_name})", f"print(validate_{var_name}({var_name}))")
    )
    return replacement


def transform_multi_print_example(code: str) -> str:
    if 'print("agent_view:", agent_view)\nprint("evaluator_view:", evaluator_view)' in code:
        return code.replace(
            'agent_view = {\n    "observation": transition["observed_block_pose"],\n    "actions": transition["available_actions"],\n}\nevaluator_view = {\n    "state": transition["true_block_pose"],\n    "action": transition["chosen_action"],\n    "reward": transition["reward"],\n    "constraint": transition["constraint_violation"],\n}\nprint("agent_view:", agent_view)\nprint("evaluator_view:", evaluator_view)',
            'def split_views(payload: dict[str, object]) -> tuple[dict[str, object], dict[str, object]]:\n'
            '    agent_view = {\n'
            '        "observation": payload["observed_block_pose"],\n'
            '        "actions": payload["available_actions"],\n'
            '    }\n'
            '    evaluator_view = {\n'
            '        "state": payload["true_block_pose"],\n'
            '        "action": payload["chosen_action"],\n'
            '        "reward": payload["reward"],\n'
            '        "constraint": payload["constraint_violation"],\n'
            '    }\n'
            '    return agent_view, evaluator_view\n\n'
            'agent_view, evaluator_view = split_views(transition)\n'
            'print("agent_view:", agent_view)\n'
            'print("evaluator_view:", evaluator_view)'
        )
    if "sim_trial =" in code and "real_trial =" in code and "print(evidence)" in code:
        return code.replace(
            'sim_trial = {"surface": "rubber_mat", "success": 0.92, "failure": "none"}\n'
            'real_trial = {"surface": "rubber_mat", "success": 0.74, "failure": "slip"}\n'
            'gap = sim_trial["success"] - real_trial["success"]\n'
            "evidence = {\n"
            '    "task": "top_grasp_cup",\n'
            '    "action": "cartesian_grasp_pose",\n'
            '    "sim_success": sim_trial["success"],\n'
            '    "real_success": real_trial["success"],\n'
            '    "sim_real_gap": round(gap, 2),\n'
            '    "real_failure": real_trial["failure"],\n'
            "}\n"
            "print(evidence)",
            'sim_trial = {"surface": "rubber_mat", "success": 0.92, "failure": "none"}\n'
            'real_trial = {"surface": "rubber_mat", "success": 0.74, "failure": "slip"}\n\n'
            'def compare_trials(sim_trial: dict[str, object], real_trial: dict[str, object]) -> dict[str, object]:\n'
            '    gap = sim_trial["success"] - real_trial["success"]\n'
            '    return {\n'
            '        "task": "top_grasp_cup",\n'
            '        "action": "cartesian_grasp_pose",\n'
            '        "sim_success": sim_trial["success"],\n'
            '        "real_success": real_trial["success"],\n'
            '        "sim_real_gap": round(gap, 2),\n'
            '        "real_failure": real_trial["failure"],\n'
            '    }\n\n'
            'evidence = compare_trials(sim_trial, real_trial)\n'
            'print(evidence)'
        )
    if "currency =" in code and "validation_artifacts =" in code and 'print(currency)\nprint(validation_artifacts)' in code:
        return code.replace(
            'print(currency)\nprint(validation_artifacts)',
            'def audit_release_support(\n'
            '    currency: dict[str, str], validation_artifacts: dict[str, str]\n'
            ') -> tuple[dict[str, str], dict[str, str]]:\n'
            '    assert currency.keys() == validation_artifacts.keys()\n'
            '    return currency, validation_artifacts\n\n'
            'currency, validation_artifacts = audit_release_support(currency, validation_artifacts)\n'
            'print(currency)\n'
            'print(validation_artifacts)'
        )
    return code


def transform_code(code: str) -> str:
    updated = code
    updated = transform_dataclass_block(updated)
    updated = transform_contract_scaffold(updated)
    for var_name in ("baseline", "shortcut", "perturbed"):
        updated = transform_baseline_like(updated, var_name)
    updated = transform_multi_print_example(updated)
    updated = transform_single_dict_print(updated)
    return updated


def process_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    changed = False

    def repl(match: re.Match[str]) -> str:
        nonlocal changed
        prefix, code_html, suffix = match.groups()
        code = decode_code(code_html)
        new_code = transform_code(code)
        if new_code != code:
            changed = True
            return prefix + encode_code(new_code) + suffix
        return match.group(0)

    updated = CODE_RE.sub(repl, text)
    if changed:
        path.write_text(updated, encoding="utf-8")
    return changed


def main() -> None:
    changed = 0
    for path in ROOT.glob(SECTION_GLOB):
        if process_file(path):
            changed += 1
    print(f"changed_files={changed}")


if __name__ == "__main__":
    main()
