#In this quiz, you’ll need to change the types of the input and output data in order to get the result you want. Calculate and print the total sales for the week from the data provided. Print out a string of the form "This week's total sales: xxx", where xxx will be the actual total of all the numbers. You’ll need to change the type of the input data in order to calculate that total.

mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.

mon_sales=int(121)
tues_sales=int(105)
wed_sales=int(110)
thurs_sales=int(98)
fri_sales=int(95)
total_sales=(mon_sales+tues_sales+wed_sales+thurs_sales+fri_sales)
other_sentence=("This week's total sales")
print(other_sentence+" "+str(total_sales))

