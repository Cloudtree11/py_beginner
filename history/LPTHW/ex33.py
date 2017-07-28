
#i = 0
numbers = []

def loop_func(a,b):
    i = 0
    while i < a:
        print "At the top i is %d" % i
        numbers.append(i)

        i += b
        print "Number now: ", numbers
        print "At the bottom i is %d" % i

loop_func(20, 3)

print "The numbers: "

for num in numbers:
    print num
