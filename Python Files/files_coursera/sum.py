Python 3.13.4 (v3.13.4:8a526ec7cbe, Jun  3 2025, 21:14:54) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> num1 = 1
>>> num2= 2
>>> sum = num1 +num2
>>> print("The sum is " + sum)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print("The sum is " + sum)
TypeError: can only concatenate str (not "int") to str
>>> print("The sum is " , sum)
The sum is  3
>>> # You can't do "The sum is " + sum, as sum is an int and the sum is
>>> # print, thus you can have the above syntax or instead do
>>> #print("The sum is " + str(sum))
