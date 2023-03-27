my_list = [1, 2, 3, 4, 5, 6]

for i in my_list:
    print(i)
    if i >= 3:
        my_list.remove(i)
        print(my_list)

numbers_list = [1,2,3,4,5]
filter_list = [x for x in numbers_list if x >3]


new_list=[1,2,3]
print(new_list)
new_list.append([4,5,6])
print(new_list)


x = [1,2,3,4]
y = (5,6,7,8,9,10)
x.append(y)
print(x)

number = [8,3,5,6]
number.insert(0,[1])
print(number)

z=[1,2,3]
u="456"
z.extend(u)
print(z)

animals = ['dog', 'cat', 'mouse']
animals.sort()
print(animals)

animals = ['dog', 'cat', 'mouse']
animals.sort(reverse=True)
print(animals)

animals = ['dog', 'cat', 'peacock']
print(sorted(animals))
print(animals)

my_tuple=[21,22,23,24]
y=list(my_tuple)
y[3]=25
x="27"
y.extend(x)
my_tuple=tuple(y)
print(my_tuple)

#set removes duplicates and it's also unordered, can't add any lists into sets
my_set = {'cat', 'DOG','cat'}
print(my_set)
#difference() findes difference that exists only in one set to the other
my_set2 = {'cat', 'dog', 'lizard'}
my_set3 = my_set2.difference(my_set)
print(my_set3)
my_set.difference_update(my_set2)
print(my_set)
#The difference_update() method is different from the difference() method,
# because the difference() method returns a new set, without the unwanted items,
# and the difference_update() method removes the unwanted items from the original set.
#The intersection() method returns a set that contains the similarity between two or more sets.
new_set=my_set.intersection(my_set2)
print(new_set)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

my_book=dict(first_name='Daniel', last_name='Johnson')
my_book.pop("last_name")
print(my_book)
print(my_book["first_name"])

dict={"brand":'BMW', "year": 1998}
dict.popitem()
print(dict)

dict={"brand":'BMW', "year": 1998}
x = dict.setdefault("brand")
print(x)

