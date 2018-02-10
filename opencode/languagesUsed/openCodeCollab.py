import requests, json,pprint
import matplotlib.pyplot as plt
import numpy as np

#added token = 'your token'

opencodecollab = requests.get('https://api.github.com/repos/opencode18/OpenCode-Collaborative/languages?access_token=' + token)

opencodecollab = json.loads(opencodecollab.content)


labels = ['HTML', 'JavaScript', 'CSS']
sizes = [opencodecollab['HTML'], opencodecollab['JavaScript'], opencodecollab['CSS']]
explode = (0, 0, 0.1)

fig1, ax1 = plt.subplots()
ax1.set_title('Languages Used in OpenCode-Collaborative')
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.show()
