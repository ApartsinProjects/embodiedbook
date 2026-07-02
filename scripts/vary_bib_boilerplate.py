# Vary the 28x identical Part-2 bibliography framing sentence per module topic.
import glob, re

GENERIC = "Use these references to check notation, frame conventions, units, solver assumptions, and maintained-library behavior."
BY_MODULE = {
    'module-04': "Use these references to check rotation-order choices, frame conventions, and unit assumptions before relying on any transform.",
    'module-05': "Use these references to check joint conventions, DH-parameter choices, and Jacobian definitions when your kinematics disagree with a library.",
    'module-06': "Use these references to check inertia conventions, integrator assumptions, and contact-model details when a simulation drifts.",
    'module-07': "Use these references to check gain conventions, stability assumptions, and discretization choices before trusting a controller.",
    'module-08': "Use these references to check noise-model conventions, calibration assumptions, and filter-tuning defaults when an estimator misbehaves.",
}
import sys
APPLY = "--apply" in sys.argv
n = 0
for f in glob.glob('part-*/module-*/section-*.html'):
    if GENERIC not in open(f, encoding='utf-8').read():
        continue
    mod = re.search(r'(module-\d+)', f).group(1)
    repl = BY_MODULE.get(mod, GENERIC)
    if repl == GENERIC:
        continue
    t = open(f, encoding='utf-8').read().replace(GENERIC, repl)
    n += 1
    if APPLY:
        open(f, 'w', encoding='utf-8').write(t)
print(f"{'APPLIED' if APPLY else 'DRY-RUN'}: varied {n} bibliography framing sentences")
