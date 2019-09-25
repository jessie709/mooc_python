from matplotlib import pyplot as plt 
import numpy as np 

x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y = np.sin(x)
plt.plot(x,y)
plt.xlim(-2*np.pi, 2 * np.pi)
plt.ylim(-1,1)
plt.title('y = sin(x)')
plt.show( )


import time
print(time.localtime())

try:
  file = open('q','b')
except Exception as e:
  print('there is no file name as b')

string= "test"
number = 1

print("change the upper and lower case")
print(string.title())
print(string.upper())
print(string.lower())
print('\n')

print('insert the teb')
print('\t'+ string)
print("clera the space")
print(string.strip())

listT1 = ['a','b','c','d','e','f']
listT1.append('g')
listT1.insert(0,'0')
print(listT1)


tupleT1 = (0,1,2,5,4,"apple")
print(tupleT1[5])