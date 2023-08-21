user = int(input("enter the number of tuples: "))
list= []
for i in range(user):
    tuple_input = input("enter the tuple: ").split(",")
    tuple_convert= tuple(map(int,tuple_input))
    list.append(tuple_convert)
sort_list= sorted(list,key= lambda x: x[-1])
for j in sort_list:
    print(j)
