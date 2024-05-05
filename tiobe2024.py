import matplotlib.pyplot as plt

languages = ["Python", "C", "C++", "Java", "C#", "Javascript",
             "Go", "VB", "SQL", "andere"]
percent_values = [16.4,10.2,9.8,8.9,6.8,2.9,1.9,1.7,1.6]

percent_others = 100 - sum(percent_values)
percent_values.append(percent_others)

fig, ax = plt.subplots()
ax.pie(percent_values, labels=languages,shadow=True, autopct='%1.1f%%', startangle=90)
plt.show()