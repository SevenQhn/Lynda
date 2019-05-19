#
# Example file for working with functions
#

# define a basic function
def func1():
    print("l am a function")

# function that takes arguments
def func2(arg1,arg2):
    print(arg1,arg2)

# function that returns a value
def cube(x):
  return x*x*x

# function with default value for an argument
def power(num,x=1): #parameter with default value
    result = 1
    for i in range(x):
        result = result * num
    return result

#function with variable number of arguments
def multi_add(*args): #note *operator to allow pass in multiple parameters
  result = 0;
  for x in args:
    result = result + x
  return result


func1() #will call function func1() directly
print(func1()) #this print will print the return value of the function func1() Value = None
print(func1) #will print functin itself demonstratrate this is a object
func2(10,20) #Pass the pramaters into functions
print(func2(10,20)) #Print the value of func2 return
print(cube(3)) #
print(power(2))
print(power(2,3))
print (power(x=3, num=2))# dont have to need follow order if pass with specific name them
print (multi_add(4,5,10,4))