import re


# 1. sort the list in ascendign order and print first element
l1 = ['yxe', 'pot', 'core', 'abc', 'what']
print(l1)
l1.sort()
print(l1)


# 2. Python program to find second largest number in a list
nums = [5, 2, 50, 9, 1, 66, 32, 4]
nums.sort()
print(nums[-2])


# 3. Python program to print odd numbers & even numbers separately in al list of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd numbers
print(nums[::2])
# even numbers
print(nums[1::2])


# 4. Program for Reversing a list
l1 = ['yxe', 'pot', 'core', 'abc', 'what']
print(l1)
l1.reverse()
print(l1)


# 5. Program to print all odd numbers from 1-50
print(list(range(1, 50, 2)))


# 6. Program to count Even and odd numbers in a list
nums = [5, 2, 50, 9, 1, 66, 32, 4]
odd = 0
even = 0
for i in nums:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print('{} odd, {} even'.format(odd, even))


# 1. Write a python program to remove zeros from an IP address("216.08.094.196")
ip = "216.08.094.196"
print(ip)
cleanIP = re.sub(r'\.0+', '.', ip)
cleanIP = re.sub(r'^0+', '', cleanIP)
print(cleanIP)


# 2. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'
txt = 'this is a test b'
x = re.findall(r'.*a.*b$', txt)
print(x)


# 3. Replace all occurences of 6 with 'six' and 10 with 'ten' for the given string 'They ate 6 apples and 10 banana'
txt = 'They ate 6 apples and 10 banana'
x = re.sub(r' 6 ', ' six ', txt)
y = re.sub(r' 10 ', ' ten ', x)
print(y)