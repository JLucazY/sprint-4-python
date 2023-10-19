import os
import json


try:
    u = {}
    if os.path.exists('/Users/joaolucas/Documents/sprint-4-python/dados.json'):
        with open('/Users/joaolucas/Documents/sprint-4-python/dados.json') as f:
            u = json.loads(f.read())
            print(u.keys())

except FileNotFoundError:
    print("O arquivo json não existe!")