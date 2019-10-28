import json
import pdb

with open('./korquad1.0/aug_train_wQA.json') as f:
    d = json.load(f)

print(json.dumps(d, indent=4, ensure_ascii=False))
