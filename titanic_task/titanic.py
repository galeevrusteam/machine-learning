import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd

data = pd.read_csv("./test.csv")

ages = list(data.Age)
sexes = list(data.Sex)
ids = list(range(1, len(ages) + 1))
colors = []
for i in range(0, len(ages)):
    if sexes[i] == 'female':
        colors.append("red")
    else:
        colors.append("blue")

plt.bar(ids, ages, color=colors)

blue_patch = mpatches.Patch(color='blue', label='Male')
red_patch = mpatches.Patch(color='red', label='Female')
plt.legend(handles=[red_patch, blue_patch])

plt.ylabel('Age')
plt.xlabel('Id')
plt.title('Ages and sexes')

plt.show()