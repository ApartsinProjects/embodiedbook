# Soften KDP-facing templated/AI-sounding phrasing in front-matter and index pages.
import glob, re

edits = {
    'index.html': [
        ('<p>Every chapter connects concepts to a runnable artifact, from a tiny environment to a robot-learning pipeline.</p>',
         '<p>A structured technical guide with worked examples, labs, and implementation-oriented exercises, from tiny environments to robot-learning pipelines.</p>'),
    ],
    'toc.html': [
        (' Every chapter and section linked below is generated and live.', ''),
    ],
    'part-5-learning-from-demonstration-and-robot-data/index.html': [
        ('This part covers a coherent segment of the embodied AI stack. It connects formal ideas with the tools and labs needed to build working systems.',
         'This part covers imitation learning, demonstrations, teleoperation, robot datasets, action chunking, diffusion policies, and offline reinforcement learning: how robots learn skills from human-provided data.'),
    ],
}

for f, subs in edits.items():
    if not glob.glob(f):
        print(f'  MISSING {f}'); continue
    t = open(f, encoding='utf-8').read()
    n = 0
    for old, new in subs:
        if old in t:
            t = t.replace(old, new); n += 1
        else:
            print(f'  NOT FOUND in {f}: {old[:50]}...')
    if n:
        open(f, 'w', encoding='utf-8').write(t)
        print(f'  {f}: {n} edit(s)')

# Soften the 5x repeated "Before leaving this chapter, choose one section and name its..." boilerplate
templ = re.compile(r'Before leaving this chapter, choose one section and name its hook, core mechanism, runnable artifact, figure, misconception warning, exercise, bibliography trail, and evaluation caveat\.')
varied = 'A good self-check: pick one section and trace it end to end, from its opening hook and core mechanism through the worked example, figure, and exercises.'
cnt = 0
for f in glob.glob('part-*/module-*/index.html'):
    t = open(f, encoding='utf-8').read()
    t2 = templ.sub(varied, t)
    if t2 != t:
        open(f, 'w', encoding='utf-8').write(t2); cnt += 1
print(f'  softened repeated chapter-recap boilerplate in {cnt} module indexes')
