## Numpy in action: returns <class 'numpy.ndarray'> type
## =====================================================

import numpy as np
from numpy import *

narr = np.array([1,2,3,4,5])
carr = np.array(['a','b','c','d'])
sarr = np.array(["RAM","ROM","CPU"])

print(narr)     # [1 2 3 4 5]
print(carr)     # ['a' 'b' 'c' 'd']
print(sarr)     # ['RAM' 'ROM' 'CPU']

print(linspace(0,100,20))   # [  0. 5.26315789 10.52631579 15.78947368 .. .. ]
print(logspace(1,20))       # [1.00000000e+01 2.44205309e+01 5.96362332e+01 1.45634848e+0 .. ..]
print(arange(1,10))         # [1 2 3 4 5 6 7 8 9]
print(arange(10,0,-1))      # [10  9  8  7  6  5  4  3  2  1]
print(zeros(5))             # [0. 0. 0. 0. 0.]
print(ones(5))              # [1. 1. 1. 1. 1.]

## ============================================================================================================

# ===:Math_Funcion:===
a1 = np.array([1,2,3,4])
a2 = np.array([10,11,12,13])
a3 = np.array([1,-2,3,-4])

print(a1+a2)     # [11 13 15 17]
print(a1-2)      # [-1  0  1  2]
print(sin(a1))   # [ 0.84147098  0.90929743  0.14112001 -0.7568025 ]
print(log(a1))   # [0. 0.69314718 1.09861229 1.38629436]
print(mean(a1))  # 2.5
print(abs(a3))   # [1 2 3 4]
print(min(a3))   # -4
print(sum(a1))   # 10

# ===:Comparison_Function:===
ar1 = array([20,30,90,50,70])
ar2 = array([20,40,50,60,70])

print(ar1 > ar2)       # [False False  True False False]
print(ar1 == ar2)      # [ True False False False  True]
print(any(ar1 > ar2))  # True
print(all(ar1 > ar2))  # False
print(logical_and(ar1>20,ar1<100))   # [False True True True True]
print(logical_or(ar1>20,ar1<100))    # [True True True True True]

ar3 = array([2,3,6,7,8])
print(where(ar3%2==0,ar3,''))  # ['2' '' '6' '' '8']

# ===:Array_Copy:===
aa = arange(1,10)
bb = arange(1,10)
a_view = aa.view()  # Shallowcopy
b_copy = bb.copy()  # DeepCopy

print('Array aa',aa)    # Array aa [1 2 3 4 5 6 7 8 9]
print('a_view',a_view)  # a_view [1 2 3 4 5 6 7 8 9]
print('Array bb',bb)    # Array bb [1 2 3 4 5 6 7 8 9]
print('b_copy',b_copy)  # b_copy [1 2 3 4 5 6 7 8 9]

a_view[3] = 40
b_copy[3] = 40

print("After modification: ")
print('Array aa',aa)    # Array aa [ 1  2  3 40  5  6  7  8  9]  # modified
print('a_view',a_view)  # a_view [ 1  2  3 40  5  6  7  8  9]    # modified    
print('Array bb',bb)    # Array bb [1 2 3 4 5 6 7 8 9]           # original
print('b_copy',b_copy)  # b_copy [ 1  2  3 40  5  6  7  8  9]    # modified

# ===:Slicing:===
ar = arange(3,12)  
print(ar)          # [ 3  4  5  6  7  8  9 10 11]
print(ar[3:7])     # [6 7 8 9]
print(ar[1:9:2])   # [ 4  6  8 10]  
print(ar[4:])      # [ 7  8  9 10 11]

# ===:n-dimentional array:===

a1 = arange(12)
print('a1',a1)
print('Dimention: '+str(a1.ndim))  #1
'''
	a1 [ 0  1  2  3  4  5  6  7  8  9 10 11]
'''

a2 = reshape(a1,(4,3))
print('a2',a2)
print('Dimention: '+str(a2.ndim))  #2
'''
	a2[[ 0  1  2]
	   [ 3  4  5]
	   [ 6  7  8]
	   [ 9 10 11]]
'''

a3 = reshape(a1,(2,2,3))
print('a3',a3)
print('Dimention: '+str(a3.ndim))  #3
'''
	a3 [[[ 0  1  2]
	     [ 3  4  5]]
	    [[ 6  7  8]
	     [ 9 10 11]]]
'''

print(eye(3))
'''
	[[1. 0. 0.]
	 [0. 1. 0.]
	 [0. 0. 1.]]
'''

print(ones((2,3),int))
'''
	[[1 1 1]
 	 [1 1 1]]
'''

print(zeros((2,3),int))
'''
    [[0 0 0]
     [0 0 0]]
'''

## ============================================================================================================
