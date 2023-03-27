#Exercises 2

#3
def compare_lists(list1, list2):
    list1_set = set(list1)
    list2_set = set(list2)
    if (list1_set & list2_set):
        print(list1_set & list2_set)
    else:
        print()

list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
compare_lists(list1, list2)



#4
def remove_duplicates(lst):
    return list(set(lst))
lst = [1, 2, 3, 3, 4, 4, 5, 6, 6, 7, 8, 9]
new_list = remove_duplicates(lst)
print(new_list)

#5
def dict_func(dictionary):
    print(f"You have a {dictionary['Type']} from {dictionary['Brand']} that costs {dictionary['Price']}.")

my_dict = {"Type": 'Phone', 'Brand': 'Nokia', 'Price': 250}
dict_func(my_dict)




