import requests, json
import matplotlib.pyplot as plt

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

name = name[80:100]
commits = commits[80:100]

plt.style.use('ggplot')

fig, ax = plt.subplots()

ax.set_xlabel('Participants')
plt.xticks(rotation=30)
ax.set_ylabel('No. Of Commits')
ax.set_title('No. of Commits by Participants in OpenCode-Collaborative')

rects = ax.bar(name, commits, width=0.35)

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1*height,
                '%d' % int(height),
                ha='center', va='bottom')
autolabel(rects)
fig.tight_layout()
plt.show()
