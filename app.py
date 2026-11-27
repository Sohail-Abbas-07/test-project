import random
import pandas as pd
students_data = {'name':[],'age':[], 'major': [], 'gpa': []}
for i in range(20):
    student = [
        f'Student {i+1}',
        random.randint(18, 25),
        random.choice(['Computer Science', 'Engineering', 'Business', 'Arts']),
        round(random.uniform(2.5, 4.0), 2)
    ]
    for key, val in zip(students_data.keys(), student):
        students_data[key].append(val)

df = pd.DataFrame(students_data)
print(df)