import numpy as np
import pandas as pd


x = pd.Series([2, 5, 6, 8, 9])
y = pd.Series([6, 9, 2, 3, 4])
res = x + y
print("Add two Series: ",res)
print(res)
res = x - y
print("Subtract two Series:",res)
res = x * y
print("Multiply two Series:",res)
res = x / y
print("Divide x/y:",res)


dict = {'a': 1,'b':2,'c':3,'d':4}
print("\nOriginal Dictionary:",dict)
pandas = pd.Series(dict)
print("\nconverted series:",pandas)

array = np.array([10,11,12,14,15])
print("NumPy array:",array)
pandas = pd.Series(array)
print("Converted Pandas:",pandas)




exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James',
'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
res = pd.DataFrame(exam_data,index = labels)
print('Score is less than 20 and greater than 15:')
print(res[(res['score'] < 21) & (res['score'] > 15)])



exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James',
'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
res = pd.DataFrame(exam_data,index = labels)
print("\nSum of the exam attempts by the student:")
print(res['attempts'].sum())