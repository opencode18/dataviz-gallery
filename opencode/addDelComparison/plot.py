import requests, json
import matplotlib.pyplot as plt
import numpy as np

#added token = 'your token'

doc = requests.get('https://api.github.com/repos/opencode18/OpenCode-Collaborative/stats/contributors?access_token=' + token)
docDict = json.loads(doc.content)

name = []
commits = []
deletions = []
additions = []

for i in range(100):
    name.append(docDict[i]['author']['login'])
    commits.append(docDict[i]['total'])
    add = 0
    deletion = 0
    for j in range(5):
        x = docDict[i]['weeks'][j]['a']
        y = docDict[i]['weeks'][j]['d']
        add += x
        deletion += y
    deletions.append(deletion)
    additions.append(add)

name = name[90:100]
additions = additions[90:100]
deletions = deletions[90:100]


N=10
ind = np.arange(N)
width = 0.4
plt.style.use('ggplot')

fig, ax = plt.subplots()

rects1 = ax.bar(ind, additions, width, color='#01579b')
rects2 = ax.bar(ind+0.4, deletions, width, color='#0288d1')

ax.set_xlabel('Participants')
plt.xticks(rotation=30)
ax.set_ylabel('No. Of Addition/Deletions')
ax.set_title('No. of Additions and Deletions by Participants in OpenCode-Collaborative')

ax.set_xticks(ind + width - 0.4)
ax.set_xticklabels(name)

rects = [ rects1[0], rects2[0] ]
names = [ 'Additions', 'Deletions']
ax.legend(rects, names)

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
plt.tight_layout()

plt.show()
