import matplotlib.pyplot as plt
import random

languages = ["Python", "C", "C++", "Java", "C#", "Javascript",
             "Go", "VB", "SQL", "Fortran", "andere"]
percent_values = [16.4,10.2,9.8,8.9,6.8,2.9,1.9,1.7,1.6, 1.5]

percent_others = 100 - sum(percent_values)
percent_values.append(percent_others)
colors = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(11)]

print(colors)
fig, ax = plt.subplots()
ax.set_title("TIOBE April 2024")
#Tortendiagramm
ax.pie(percent_values, labels=languages,startangle=90, colors=colors)
#Legende links
labels = ['{0} - {1:1.1f} %'.format(i, j) for i, j in zip(languages, percent_values)]
plt.legend(labels, loc='center left', bbox_to_anchor=(-0.35, .5), fontsize=8)
plt.show()