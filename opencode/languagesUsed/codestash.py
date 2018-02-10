import requests, json,pprint
import matplotlib.pyplot as plt
import numpy as np

token = 'c165507103883200aea2b06f1adba2adb84f27a1'

codestash = requests.get('https://api.github.com/repos/opencode18/codestash/languages?access_token=' + token)
codestash = json.loads(codestash.content)

labels = ['Python', 'Go', 'C', 'C++', 'Java']
sizes = [codestash['Python'], codestash['Go'], codestash['C'], codestash['C++'], codestash['Java']]
explode = (0, 0, 0.1, 0, 0)

fig1, ax1 = plt.subplots()
ax1.set_title('Languages Used in CodeStash')
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')
plt.tight_layout()

plt.show()
