import requests, json
import matplotlib.pyplot as plt
import numpy as np

opencodeCollab = requests.get('https://api.github.com/repos/opencode18/opencode-collaborative/stats/participation')
hackerSkills = requests.get('https://api.github.com/repos/opencode18/hackerskills/stats/participation')
codeStash = requests.get('https://api.github.com/repos/opencode18/codestash/stats/participation')
proDesigner = requests.get('https://api.github.com/repos/opencode18/prodesigner/stats/participation')

opencodeCollab_dict = json.loads(opencodeCollab.content)
hackerSkills_dict = json.loads(hackerSkills.content)
codeStash_dict = json.loads(codeStash.content)
proDesigner_dict = json.loads(proDesigner.content)

opencodeCollab = [opencodeCollab_dict['all'][47], opencodeCollab_dict['all'][48], opencodeCollab_dict['all'][49], opencodeCollab_dict['all'][50], opencodeCollab_dict['all'][51]]
hackerSkills = [hackerSkills_dict['all'][47], hackerSkills_dict['all'][48], hackerSkills_dict['all'][49], hackerSkills_dict['all'][50], hackerSkills_dict['all'][51]]
codeStash = [codeStash_dict['all'][47], codeStash_dict['all'][48], codeStash_dict['all'][49], codeStash_dict['all'][50], codeStash_dict['all'][51]]
proDesigner = [proDesigner_dict['all'][47], proDesigner_dict['all'][48], proDesigner_dict['all'][49], proDesigner_dict['all'][50], proDesigner_dict['all'][51]]

# print(opencodeCollab)
# print(hackerSkills)
# print(codeStash)
# print(proDesigner)

N=5
ind = np.arange(N)
width = 0.2
plt.style.use('ggplot')

fig, ax = plt.subplots()

rects1 = ax.bar(ind-0.4, opencodeCollab, width, color='#01579b')
rects2 = ax.bar(ind-0.2, hackerSkills, width, color='#0288d1')
rects3 = ax.bar(ind+0.2, codeStash, width, color='#b3e5fc')
rects4 = ax.bar(ind, proDesigner, width, color='#81d4fa')


ax.set_ylabel('Number of Commits')
ax.set_xlabel('Weeks')
ax.set_title('Commits Visulization for Popular OpenCode18 Repositories')
ax.set_xticks(ind + width - 0.4)
ax.set_xticklabels(('Week-1', 'Week-2', 'Week-3', 'Week-4', 'Week-5'))

rects = [ rects1[0], rects2[0], rects3[0], rects4[0] ]
names = [ 'OpenCode-Collaborative', 'HackerSkills', 'CodeStash', 'ProDesigner' ]
ax.legend(rects, names)

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)

plt.show()
