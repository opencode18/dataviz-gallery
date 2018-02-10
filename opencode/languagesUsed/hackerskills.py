import requests, json,pprint
import matplotlib.pyplot as plt
import numpy as np

#added token = 'your token'

hackerskills = requests.get('https://api.github.com/repos/opencode18/hackerskills/languages?access_token=' + token)

hackerskills = json.loads(hackerskills.content)

labels = ['Python', 'JavaScript', 'HTML', 'Java', 'C', 'C++', 'Shell', 'Go', 'CSS']
sizes = [hackerskills['Python'], hackerskills['JavaScript'], hackerskills['HTML'], hackerskills['Java'], hackerskills['C']
, hackerskills['C++'], hackerskills['Shell'], hackerskills['Go'], hackerskills['CSS']]
explode = (0.1, 0.1, 0.1, 0, 0.1, 0.1, 0.1, 0.1, 0.1)

fig1, ax1 = plt.subplots()
ax1.set_title('Languages Used in hackerSkills')
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90, radius=4)
ax1.axis('equal')
plt.tight_layout()

plt.show()
