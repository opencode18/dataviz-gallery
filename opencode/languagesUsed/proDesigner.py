import requests, json,pprint
import matplotlib.pyplot as plt
import numpy as np

token = 'c165507103883200aea2b06f1adba2adb84f27a1'

prodesigner = requests.get('https://api.github.com/repos/opencode18/prodesigner/languages?access_token=' + token)

prodesigner = json.loads(prodesigner.content)

labels = ['HTML', 'JavaScript', 'CSS']
sizes = [prodesigner['HTML'], prodesigner['JavaScript'], prodesigner['CSS']]
explode = (0, 0.1, 0)

fig1, ax1 = plt.subplots()
ax1.set_title('Languages Used in ProDesigner')
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  
plt.tight_layout()

plt.show()
