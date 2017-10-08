# X to represent the input value
#input
x = []

integer = [elm for elm in x if isinstance(elm, int)]

decimal = [elm for elm in x if isinstance(elm, float)]

string = [elm for elm in x if isinstance(elm, str)]

sum1 = 0
for i in range (0,len(integer)):
    sum1 = integer[i] + sum1


sum2 = 0
for i in range (0,len(decimal)):
    sum2 = decimal[i] + sum2


sum = sum1 + sum2


sen = ""
for i in range (0,len(string)):
    sen = sen + " " +string[i]


if (integer != [] or decimal !=[]) and string !=[]:
    print'The list you entereed is of mixed type'
    print 'Sum is ', sum
    print 'string: ', sen

elif string == [] and (integer != [] and decimal !=[]):
        print'The list you entereed is of mixed type'
        print 'Sum from integer and decimal is ', sum

elif string != [] and integer == [] and decimal ==[]:
        print'The list you entereed is of string type'
        print 'string: ', sen

elif string == [] and integer != [] and decimal ==[]:
        print'The list you entereed is of integer type'
        print 'Sum is ', sum

elif string == [] and integer == [] and decimal !=[]:
        print'The list you entereed is of float type'
        print 'Sum is ', sum

elif string == [] and integer == [] and decimal ==[]:
        print'you have an empty list entered'
