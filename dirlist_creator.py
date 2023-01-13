#!python3

# описатель структуры папок в json формат
# https://gist.github.com/prabindh/35dfb54249a0b5cfc1550aa8c4bd72f1

import os
import json

def path_to_dict(path):
    d = {os.path.basename(path): {}}
    if os.path.isdir(path):
        d[os.path.basename(path)]['type'] = "directory"
        d[os.path.basename(path)]['children'] = dict((key,d[key]) for d in [path_to_dict(os.path.join(path,x)) for x in os.listdir(path)] for key in d)
    else:
        d[os.path.basename(path)]['type'] = "file"
    return d

with open('MANIFEST.JSON', 'w', encoding='utf-8') as f:
    json.dump(path_to_dict('.'), f, ensure_ascii=False, indent=4)
