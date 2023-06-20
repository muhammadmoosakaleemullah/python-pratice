# method or function
# append
# number_li=[1,2,12,1,21,2,2];
# number_li.append('zAIN')
# print(number_li)
# help(number_li)
# print(number_li.count('he'));
# help(number_li)
# print(number_li.index(2))
# number_li.pop(1)
# print(number_li)
# number_li.sort()
# print(number_li);
# new_li=[7,1,1,4,5];
# #new_li.append('moosa')
# #print(new_li.count(1))
# #print(new_li)
# #print(new_li.index(1))
# #new_li.remove(1)
# #print(new_li)
# #new_li.sort()
# #print(new_li)
# new_li.reverse()
# print(new_li)
# def add_two_numbers(x,y): #x,y => parameters,  placheholder
#     output=x+y
#     return output

# print(add_two_numbers(1,10));
# res=add_two_numbers(1,10) #1,10 => actual  arguments
# print(res)

# def average_three_numbers(x,y,z):
#     sum=x+y+z;
#     avg=sum/3;
#     return avg;

# print(average_three_numbers(10,20,30))
# av=average_three_numbers(10,20,30);
# print(av)
# def divison_two_numbers(a,b):
#     res=a/b;
#     return res;
# print(divison_two_numbers(20,5))
# number_li=[1,2,1,21,21,2,3];
# print(number_li.count(2))
# number_li.sort()
# print(number_li)
# print(number_li.index(2))
# number_li.append('zain')
# print(number_li)
# number_li.clear()
# print(number_li)
# new_number_list=number_li.copy()
# print(new_number_list)
# number_li.extend(['zain','umer'])
# print(number_li)
# number_li.insert(2,'zain')
# number_li.pop(2)
# print(number_li)
# def percentage_result(a, b):
# return a/b*100


# print(percentage_result(83, 100))

# function definition
# def find_square(num):
# result = num * num
# return result


# square = find_square(3)

# print('Square:',square)

# function definition
# def get_square(num):
# return num * num

# for i in [1,2,3]:

# result = get_square(i)
# print('Square of',i, '=',result)
# new_li=[1,2,3,4]

# new_li.append(5)
# print(new_li.count(2))
# print(new_li.index(2))
# new_li.pop(1)
# new_li.sort
# new_li.remove(2)
# new_li.reverse()
# new_li.insert(2,3)
# new_li.extend([5,6,7])
# new_li.copy()
# new_li.clear()
# print(new_li)
# my_tupple=(1,2,3,4,5)
# print(my_tupple.index(4))
# my_set={1,2,3,4,5,6}
# my_set.add(7)
# my_set.pop()
# my_set.discard(5)
# my_set.update({7,8,9})
# print(my_set)
# def percentage_numbers(a,b):
#    return a/b*100
# print(percentage_numbers(12,20))

# def avg_numbers(a,b,c):
#    return a+b+c/3
# print(avg_numbers(2,3,4))
# my_set={1,2,3,4,5}
# my_set.discard(5)
# my_set.update({7,8,9})
# my_set.pop()
# my_set.add(6)
# print(my_set)
# my_li=(1,2,2,3,4,5)
# print(my_li.index(3))
# new_dict={
#     'name': 'moosa',
#     'age': '23',
#     'gender': 'Male'
# }
# new_dict['role']= 'student';
# print(new_dict)

# unpacking list,tuple
# number_list=['a','b','c','d'];
# a=number_list[0];
# b=number_list[1];
# c=number_list[2]
# a,b,*_=letter_tuple
# print(a,b,_)

# friends_list=['zain','fazain','umer','uzair'];
# f_name_1,*other_friends = friends_list;
# print(f_name_1,other_friends)

# Iterable
#
# letter_tuple=('a','b','c','d');
# new_list=tuple(letter_tuple);
# print(new_list)

# letter_tuple=('a','b','c','d');
# new_set=set(letter_tuple);
# print(new_set)

# def di(value_1=1,value_2=1):
# return  value_1/value_2;
# print(di());

# def count_para(*args,**kwargs):
#     print(kwargs)
#     return len(args);

# print(count_para(1,1,21,2,1,2,value_1=1,value_2=2))
## print(sum([1,2,1,2,2]))

# condtion =>
# logical operators
# > , < ==, !=,

# and , or , not
has_license = True;
has_id = False;
age = 18
# and => both ture or => i ture not reverse
# if(age >=18  or has_license or has_id):
#     print('He can drive in Pkr')
#
# conditional statements
# if(has_id and age >=18 or has_license  ):
#      print('He can drive in Pkr')
# if(has_id and age >=18 or not has_license):
#     print('He can drive in Pkr')
#     print('hi how are you ')
# else:
#     print('He can not drive ')

# escape sequence character
# print('He can\'t drive ')
# print('Hi,\nHow are you')
# print('Hi,\tHow are you')
# print('Hi,\bHow are you')

# + , - , *, % , /
# print(1+1)
# print(1-1)
# print(3%2)
# print(3/2)
# print(3*2)
# print(3/'2')
# print('2'+ '2')
# print('#' * 10)

# template litrals in js or formated string or fstring
# age=10
# print(f'He is {age} years old ')
# print(r'He is \n years old ')

# tomorrow terniary operator
print(f"my name \is moosa")