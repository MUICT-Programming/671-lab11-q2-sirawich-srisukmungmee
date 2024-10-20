n=int(input())
lst1=[]
lst2=[]
updated_list=[]
def summation(n):
    for i in range(n):
        list1=int(input())
        lst1.append(list1)
    for i in range(n):
        list2=int(input())
        lst2.append(list2)
        updated_list.append(lst1[i]+lst2[i])
    return updated_list
def find_min_max(updated_list):
    min_value=min(updated_list)
    max_value=max(updated_list)
print(summation(n))
print(find_min_max(updated_list))
