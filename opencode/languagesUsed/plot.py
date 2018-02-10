import requests, json,pprint
import matplotlib.pyplot as plt
import numpy as np

token = 'c165507103883200aea2b06f1adba2adb84f27a1'

opencodecollab = requests.get('https://api.github.com/repos/opencode18/OpenCode-Collaborative/languages?access_token=' + token)
prodesigner = requests.get('https://api.github.com/repos/opencode18/prodesigner/languages?access_token=' + token)
codestash = requests.get('https://api.github.com/repos/opencode18/codestash/languages?access_token=' + token)
hackerskills = requests.get('https://api.github.com/repos/opencode18/hackerskills/languages?access_token=' + token)

opencodecollab = json.loads(opencodecollab.content)
prodesigner = json.loads(prodesigner.content)
codestash = json.loads(codestash.content)
hackerskills = json.loads(hackerskills.content)

print(opencodecollab)
print(prodesigner)
print(codestash)
print(hackerskills)
