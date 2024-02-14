#Q 1.Print the first 10 natural numbers using for loop.
# for i in range(1,11):
#     print(i)
# n=11
# for i in range(n):
#     print(i)


#Q 2. Python program to print all the even numbers within the given range.
# n=10
# for i in range(1,n):
#     if(i%2==0):
#         print(i)


# Q 3.Python program to calculate the sum of all numbers from 1 to a given number.
# n=10
# sum=100
# for i in range(n):
#     sum+=i
#     print(sum)


#Q 4. Python program to calculate the sum of all the odd numbers within the given range.
# n=10
# sum=50
# for i in range(n):
#     if(i%2!=0):
#         sum+=i
#         print(sum)


#Q 5.Python program to print a multiplication table of a given number
# n=10
# for i in range(10):
#     print(n*i)
# n=15
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)


#Q 6.Python program to display numbers from a list using a for loop.
# list=[1,33,98,76,54]
# for i in list:
#     print(i)


#Q 7.Python program to count the total number of digits in a number.
# r = 129475
# # since we cannot iterate over an integer
# # in python, we need to convert the
# # integer into string first using the
# # str() function
# r = str(r)
# count = 0
# for i in r:
#     count += 1
# print(count)


#Q 8. Python program to count the number of even and odd numbers from a series of numbers.
# n=[2,66,78,89,54,55,63]
# for i in n:
#     if(i%2==0):
#         print(i,'num is even')
#     else:
#         print(i,'num is odd')

#Q 9.Python program to get the Fibonacci series between0 to 50.
num = 50
# initial values in the series
first_value, second_value = 0, 1
for n in range(0, num):

    # if no. is less than 1
    # move to next number
    if (n <= 1):
        next = n

    # if number is within range
    # execute the below code block
    if nextnum:
        break
    # print each element that
    # satisfies all the above conditions
    print(next)

# Q 10.Python program to find the factorial of a given number
# n= 5
#
# # since 1 is a factor
# # of all number
# # set the factorial to 1
# factorial = 1
#
# # iterate till the given number
# for i in range(1, n + 1):
#     factorial = factorial * i
# print("The factorial of ", n , " is ", factorial)
