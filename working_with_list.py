#1.- We can create lists as it follows:
empty_list = []
list_1 = [1,2,3,4]
list_2 = [[11,12,13,14],[15,16,17,18]]
list_3 = [[21,22,23,24],[25,26,27,28],[29,30,31,32]]

print("Empty list = ",empty_list)
print("List with four values = ",list_1)
print("List with 2 sub-lists with four values each one = ",list_2)
print("List with 3 sub-lists with four values each one = ",list_3)
print("Type = ",type(list_1))


#2.- To access to the values in the lists:
print("First value in list_1 = ",list_1[0],"\n")
print("First sub-list in list_2 = ",list_2[0])
print("First value in first sub.list in list_2 = ",list_2[0][0],"\n")
print("Same way for list_3")
print(list_3[0])
print(list_3[0][0])
