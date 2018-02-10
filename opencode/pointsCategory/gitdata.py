import requests, json
import matplotlib.pyplot as plt

labelList = []

for i in range(1,17):
    doc = requests.get('https://api.github.com/repos/opencode18/OpenCode-Collaborative/issues?state=all&page=' + str(i))
    docStr = json.loads(doc.content)


    if i!=16:
        for j in range(30):
            labels = docStr[j]['labels']
            for label in labels:
                labelList.append(label['name'])

    if i==16:
        for j in range(29):
            labels = docStr[j]['labels']
            for label in labels:
                labelList.append(label['name'])

rookie = labelList.count('Rookie: 10 Points')
skilled = labelList.count('Skilled: 20 Points')
advanced = labelList.count('Advanced: 30 Points')
expert = labelList.count('Expert: 50 Points')

# print(rookie)
# print(skilled)
# print(advanced)
# print(expert)


plt.style.use('ggplot')
x = ['Rookie', 'Skilled', 'Advanced', 'Expert']
y = [rookie, skilled, advanced, expert]

fig, ax = plt.subplots()

ax.set_xlabel('Points Category')
ax.set_ylabel('No. Of Issues')
ax.set_title('Points Category Comparison in OpenCode-Collaborative')

rects = ax.bar(x, y, width=0.35)

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1*height,
                '%d' % int(height),
                ha='center', va='bottom')
autolabel(rects)
plt.show()
