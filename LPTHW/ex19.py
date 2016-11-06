def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

def print_string_num(string_to_print, num_to_print):
	print "String is \"%s\"" % string_to_print
	print "Num is: %d" % num_to_print


# print "We can just give the function numbers directly:"
# cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
# string_print = 'I\'m so handsome!'
string_print = raw_input("string_print: ")
# num_print = 555
num_print = raw_input("num_print: ")
# cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# print "We can even do math inside too:"
# cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
print_string_num(string_print, int(num_print))
