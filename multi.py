# print the odd number between 1 to 1000
for i in range(1,1000):
    if i%2 != 0:
        print i

# print all the mulitples of 5 from 5 to 1000000
j = 5
while j <=1000000:
    print j
    j = j*5

# print the sum of all the values in the list below
a = [1, 2, 5, 10, 255, 3]

sum = 0
for  counter in range(0,len(a)):
    sum = a[counter] + sum
print sum

# print the average of the values in following list
aver = sum/len(a)
print aver
