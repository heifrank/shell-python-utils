import sys
import json
import os

dir = '/data/news'

os.chdir(dir)

outdir = '/home/services/songyang/201606ids'
if not os.path.exists(outdir):
    os.mkdir(outdir)

for folder in os.listdir('.'):
    if folder.startswith('201606') and os.path.isdir(folder):
        for file in os.listdir(folder):
            filename = os.path.join(folder, file)
            if filename.endswith("dat"):
                f = open(filename, 'r')
                of = open(os.path.join(outdir, file), 'w')
                for line in f:
                    if line.strip():
                        obj = json.loads(line)
                        of.write(obj.get('_id') + '\n')

                f.close()
                of.close()

