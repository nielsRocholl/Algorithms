import numpy as np
from matplotlib import pyplot as plt
import json

data = {}
for student in range(10):
    # half of the students studies little
    if student < 5:
        mu, sigma = 5, 5
        exercises = np.random.normal(mu, sigma)
        reading = np.random.normal(mu, sigma)
        # 80 percent of these students fail
        passed = False if np.random.random(1)[0] < 0.8 else True
    # half of the students studies a lot
    else:
        mu, sigma = 15, 5
        exercises = np.random.normal(mu, sigma)
        reading = np.random.normal(mu, sigma)
        # 80 percent of these students pass
        passed = True if np.random.random(1)[0] < 0.8 else False
    data[f'student {student}'] = {'passed': passed, 'features': [exercises, reading]}

with open('data.json', 'w') as fp:
    json.dump(data, fp)

for student in data:
    features = data[student]['features']
    passed = data[student]['passed']
    plt.scatter(features[0], features[1])
    label = ' Passed' if passed else ' Failed'
    plt.annotate(label, (features[0], features[1]))
plt.scatter(16, 17)
label = ' unknown'
plt.annotate(label, (16, 17))
plt.ylabel('hours studied (practice exercises)')
plt.xlabel('hours studied (reading materials)')
plt.title('Practise Exercises vs. Reading Material ')
plt.grid()
plt.savefig('dataset.png')
plt.show()
