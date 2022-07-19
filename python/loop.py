# Print the list of numbers which are dividible by 5
# and multiple of 8 between 2000 and 2500
for i in range(2000, 2500):
    if (i % 5 == 0) and (i % 8 == 0):
        print(i)


# Write a Python program to create the table (from 1 to 10)
# of a number getting input from the user

n = int(input('Enter a number: '))
for i in range(1, 11):
    print('{} x {} = {}'.format(n, i, n * i))