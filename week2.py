my_list =[]
elements_to_append = [10,20,30,40]
for item in elements_to_append:
    my_list.append(item)
print(my_list)
my_list.insert(1,15)
list_to_extend = [50,60,70]
my_list.extend(list_to_extend)
my_list.pop()
my_list = sorted(my_list)
print(my_list)
print(my_list.index(30))