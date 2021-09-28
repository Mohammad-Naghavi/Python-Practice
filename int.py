# numbers=[1,5,2,4,6,10,3];
# for number in numbers:
#     if (number%2)==0 :
#         print(number, "is even")
#     else: 
#         print(number, "is odd")

# for row in range(1,14):
#     # print(row+1)
    
#     for col in range(row):
#         print('{:4}'.format(col+1), end="")
#     print()
# number = int(input("enter your number:"))
# # print(type(number))
# number=9
# type(number)
# number
# print(type(number))


# count = int(input("enter your number:"))
# while count >=0:
#     print (count)
#     count -=1

# numbers=[1,-5,2,-4,0,6,-10,3]
# pos=[]
# neg=[]

# for number in numbers:
#     if number >0:
#         pos.append(number)
#     else:
#         neg.append(number)
# print(pos)
# print(neg)





# import random
# number=[i for i in range(1,26)]
# random.shuffle(number)
# print(number)
# # shuffled=[8, 3, 23, 25, 17
# #             , 2, 9, 1, 18, 19
#             ,10, 13, 7, 24, 20
#             , 14, 15, 12, 6, 16
# #             , 11, 4, 5, 21, 22]
# groups= [[],
#         [],
#         [],
#         [],
#         []]
# for i in range(0,5):
#     for j in range (0,5):
#         groups[j].append(number.pop(-1))


# for race in groups:
#     race.sort()
#     print(race)

# def last(x):
#     return x[-1]
# new_groups=sorted(groups,key=last, reverse=True)
# print()
# for race in new_groups:
#     print(race)

# جدول ضرب

# def time_table():
#     while True:
#         try:
#             x = int(input("please enter a number:"))
#             for row in range(x+1):
#                 for col in range(x+1):
#                     print(f"{row*col:3}", end=" ")
#                 print()
#         except ValueError:
#             print("Ooops,enter a number please.")
#         q = input("Do you want another number?y/n?").lower()
#         if q[0] == "n":
#                  break

# time_table()
            

# Prime numbers اعداد اول
# def is_prime(num):
#     for i in range (2,num):
#         if num%i == 0:
#             return False
#     return True
# test=[3,5,8,9,13,22,33,54,89,121]
# for num in test:
#     print (f"{num} is a prime number {is_prime(num)}")


# leaf year


# def is_leap(year):
#     # leap = False
#     if year % 4 == 0:
#         if  year %100 !=0:
#             return True
#         elif year %400==0:
#                 return True
#     return False            

#     # return leap

# year = int(input())
# print(is_leap(year))



# n --> 123...n
n= int(input("enter your number"))

def number():
    for i in range(1,n+1):
        for j in range(1,i):
            print(f"{j:3}", end="")
        print()

number()
