def odd_even():
    for i in range (1, 5):
        if i%2 != 0:
            print "Number is",i,".", "This is an odd number."
        else:
            print "Number is", i,".", "This is an even number."
odd_even()

# a is for the list. b is the number be multiplied. c is for the results list
def multiply(a,b):
    for i in range (0,len(a)):
        a[i] = a[i]*b
    return a

multiply([2,4,5],3)



def layered_multiples(arr):
    newArray = []
    for i in range (0,len(arr)):
        ll = []
        for j in range (0,arr[i]):
            ll.append(1)
        newArray.append(ll)
    print newArray

layered_multiples(multiply([2,4,5],3))

# # output
# >>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
