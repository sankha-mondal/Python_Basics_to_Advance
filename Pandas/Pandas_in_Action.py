## Pandas - a library used for working with data sets
## returns <class 'pandas.core.series.Series'> type
## --------------------------------------------------

import pandas as pd

## == :Working with Series: ==

reviews = pd.Series([4.9, 4.3, 5, 4.7, 4.2])
print(reviews)
'''
    0    4.9
    1    4.3
    2    5.0
    3    4.7
    4    4.2
    dtype: float64
'''
print(reviews[0])       # 4.9

print(reviews.count())  # 5
print(reviews.mean())   # 4.619999999999999
print(reviews.min())    # 4.2
print(reviews.max())    # 5.0
print(reviews.std())    # 0.3563705936241093

print(reviews.describe())
'''
    count    5.000000
    mean     4.620000
    std      0.356371
    min      4.200000
    25%      4.300000
    50%      4.700000
    75%      4.900000
    max      5.000000
'''

# Custom indexing:
reviews = pd.Series([4.9, 4.3, 5, 4.7, 4.2], index=['python','c++','java','django','ruby'])
print(reviews)
'''
    python    4.9
    c++       4.3
    java      5.0
    django    4.7
    ruby      4.2
    dtype: float64
'''

reviews = pd.Series({'python':4.6, 'java':4.5, 'ruby':4.8, 'c++':5})
print(reviews)
'''
    python    4.6
    java      4.5
    ruby      4.8
    c++       5.0
    dtype: float64
'''

# Accessing value by indexing:
print(reviews['python'])  # 4.6
print(reviews.python)  # 4.6
print(reviews.java)    # 4.5
print(reviews.index)   # Index(['python', 'java', 'ruby', 'c++'], dtype='object')
print(reviews.values)  # [4.6 4.5 4.8 5. ]

cources = pd.Series(['Java','Python','Ruby'])
print(cources)
'''
    0      Java
    1    Python
    2      Ruby
    dtype: object
'''
print(cources.str.upper())
'''
    0      JAVA
    1    PYTHON
    2      RUBY
    dtype: object
'''
print(cources.str.contains('y'))
'''
    0    False
    1     True
    2     True
    dtype: bool
'''

## ==================================================================================

## == :Working with Data-Frames: ==

scores_dict = {'Kohli':[100,50,70,81], 'Rohit':[100,88,45,71], 
               'Surya':[77,110,20,57], 'Jadeja':[99,120,58,93],
               'Rahul':[33,89,107,28]}
scores = pd.DataFrame(scores_dict)
print(scores)
'''
        Kohli  Rohit  Surya  Jadeja  Rahul
    0    100    100     77      99     33
    1     50     88    110     120     89
    2     70     45     20      58    107
    3     81     71     57      93     28
'''

scores = pd.DataFrame(scores_dict, index=['I1','I2','I3','I4'])
print(scores)
'''
        Kohli  Rohit  Surya  Jadeja  Rahul
    I1    100    100     77      99     33
    I2     50     88    110     120     89
    I3     70     45     20      58    107
    I4     81     71     57      93     28
'''

# Access Column data:
print("Kohli's Scores:")
print(scores['Kohli'])
'''
    Kohli's Scores:
    I1    100
    I2     50
    I3     70
    I4     81
    Name: Kohli, dtype: int64
'''
print(scores.Kohli)
'''
    I1    100
    I2     50
    I3     70
    I4     81
    Name: Kohli, dtype: int64
'''

# Access Row data:
print(scores.loc['I1'])
'''
    Kohli     100
    Rohit     100
    Surya      77
    Jadeja     99
    Rahul      33
    Name: I1, dtype: int64
'''
print(scores.iloc[0])
'''
    Kohli     100
    Rohit     100
    Surya      77
    Jadeja     99
    Rahul      33
    Name: I1, dtype: int64
'''

# Use Slicing and Lists:
print(scores.loc['I1':'I3'])  # returns data from I1 to I2
'''
        Kohli  Rohit  Surya  Jadeja  Rahul
    I1    100    100     77      99     33
    I2     50     88    110     120     89
    I3     70     45     20      58    107
'''
print(scores.iloc[1:3]) # returns n to (m-1)
'''
        Kohli  Rohit  Surya  Jadeja  Rahul
    I2     50     88    110     120     89
    I3     70     45     20      58    107
'''
print(scores.loc[['I1','I3']])  # returns particular rows
'''
        Kohli  Rohit  Surya  Jadeja  Rahul
    I1    100    100     77      99     33
    I3     70     45     20      58    107
'''
