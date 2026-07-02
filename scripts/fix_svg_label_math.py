# Convert LaTeX inside SVG <text> labels to plain Unicode (KaTeX never renders SVG text).
import re, glob, sys

APPLY = "--apply" in sys.argv

GREEK = {
    r'\alpha': 'α', r'\beta': 'β', r'\gamma': 'γ', r'\delta': 'δ', r'\epsilon': 'ε',
    r'\zeta': 'ζ', r'\eta': 'η', r'\theta': 'θ', r'\iota': 'ι', r'\kappa': 'κ',
    r'\lambda': 'λ', r'\mu': 'μ', r'\nu': 'ν', r'\xi': 'ξ', r'\pi': 'π', r'\rho': 'ρ',
    r'\sigma': 'σ', r'\tau': 'τ', r'\phi': 'φ', r'\chi': 'χ', r'\psi': 'ψ', r'\omega': 'ω',
    r'\Gamma': 'Γ', r'\Delta': 'Δ', r'\Theta': 'Θ', r'\Lambda': 'Λ', r'\Pi': 'Π',
    r'\Sigma': 'Σ', r'\Phi': 'Φ', r'\Psi': 'Ψ', r'\Omega': 'Ω', r'\nabla': '∇',
}
OPS = {
    r'\sim': '~', r'\cdot': '·', r'\mid': '|', r'\to': '→', r'\leftarrow': '←',
    r'\Rightarrow': '⇒', r'\in': '∈', r'\sum': 'Σ', r'\prod': 'Π', r'\int': '∫',
    r'\infty': '∞', r'\leq': '≤', r'\geq': '≥', r'\neq': '≠', r'\approx': '≈',
    r'\times': '×', r'\pm': '±', r'\propto': '∝', r'\partial': '∂', r'\ldots': '…',
    r'\dots': '…', r'\circ': '∘', r'\odot': '⊙', r'\oplus': '⊕',
}
SUB = str.maketrans('0123456789+-=()aehijklmnoprstuvx', '₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₕᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓ')
SUP = str.maketrans('0123456789+-=()n', '⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿ')


def latex_to_unicode(s):
    for k, v in {**GREEK, **OPS}.items():
        s = s.replace(k, v)
    # subscripts: _{...} and _x
    def sub_rep(m):
        inner = m.group(1) or m.group(2)
        try:
            return inner.translate(SUB)
        except Exception:
            return '_' + inner
    s = re.sub(r'_\{([^}]*)\}|_([A-Za-z0-9+\-=()])', sub_rep, s)
    def sup_rep(m):
        inner = m.group(1) or m.group(2)
        try:
            return inner.translate(SUP)
        except Exception:
            return '^' + inner
    s = re.sub(r'\^\{([^}]*)\}|\^([A-Za-z0-9+\-=()])', sup_rep, s)
    # \hat{x} -> x + combining hat
    s = re.sub(r'\\hat\{([^}])\}', lambda m: m.group(1) + '̂', s)
    s = re.sub(r'\\(?:mathcal|mathbf|mathrm|text)\{([^}]*)\}', r'\1', s)
    s = s.replace(r'\(', '').replace(r'\)', '').replace(r'\,', ' ').replace(r'\;', ' ')
    s = re.sub(r'\\[a-zA-Z]+', '', s)     # drop any leftover commands
    s = s.replace('{', '').replace('}', '')
    return s


total = 0
for f in sorted(glob.glob('part-*/module-*/section-*.html')):
    t = open(f, encoding='utf-8').read()
    def repl(m):
        global total
        inner = m.group(1)
        if r'\(' in inner or r'\)' in inner:
            total += 1
            fixed = latex_to_unicode(inner)
            return m.group(0).replace(inner, fixed)
        return m.group(0)
    t2 = re.sub(r'<text[^>]*>(.*?)</text>', repl, t, flags=re.DOTALL)
    if t2 != t:
        print(f'  {f.split("module-")[-1][:45]}')
        if APPLY:
            open(f, 'w', encoding='utf-8').write(t2)

print(f"\n{'APPLIED' if APPLY else 'DRY-RUN'}: converted {total} SVG label(s)")
