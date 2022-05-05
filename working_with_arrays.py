#1.- To work with arrays, numpy has to be used:
import numpy as np

list_1 = [1,2,3,4]
array_1 = np.array(list_1)
print("Array_1 = ",array_1)
print("Type = ",type(array_1))
print("Columns = ",len(array_1))
print("Shape = ",array_1.shape)

list_2 = [[11,12,13,14],[15,16,17,18]]
array_2 = np.array(list_2)
print("Array_2 = ",array_2)
print("Tipo = ",type(array_2))
print("Columns = ",len(array_2),"--","Rows = ",len(array_2[0,:]))
print("Shape",array_2.shape)

list_3 = [[21,22,23,24],[25,26,27,28],[29,30,31,32]]
array_3 = np.array(list_3)
print("Array_3 = ",array_3)
print("Type = ",type(array_3))
print("Columns = ",len(array_3),"--","Rows = ",len(array_3[0,:]))
print("Shape",array_3.shape)


#2.- To acces to the values in the arrays:
print("First value in array_1 = ",array_1[0],"\n")
print("First column in array_2 = ",array_2[0,:])
print("First value in first column in array_2 = ",array_2[0,0],"\n")
print("Same way for array_3")
print(array_3[0,:])
print(array_3[0,0])


#3.- Initialize one dimension array:
n=4
zeros_array_one_dim = np.zeros(n)
print("Array full with zeros = ",zeros_array_one_dim)
ones_array_one_dim = np.ones(n)
print("Array full with ones = ",ones_array_one_dim)

#4.- For more dimensions:
array_zeros = np.zeros((2,4))
print("Array with 2 columns, 4 rows full with zeros = ",array_zeros)
array_ones = np.ones((2,4))
print("Array with 2 columns, 4 rows full with ones = ",array_ones)

#5.-Element types integer:
array_zeros = np.zeros((2,4),dtype=int)
print("Array with 2 columns, 4 rows full with integer zeros = ",array_zeros)
array_ones = np.ones((2,4),dtype=int)
print("Array with 2 columns, 4 rows full with integer ones = ",array_ones)

#6.-Element types integer real:
array_zeros = np.zeros((2,4),dtype=int)
print("Array with 2 columns, 4 rows full with float zeros = ",array_zeros)
array_ones = np.ones((2,4),dtype=int)
print("Array with 2 columns, 4 rows full with float ones = ",array_ones)

#7.- Useful numpy functions:
array_long_4 = np.linspace(0,12,4)
print("Array with 4 elements equally spaced",array_largo_4)

