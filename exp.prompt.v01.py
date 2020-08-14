# https://stackabuse.com/getting-user-input-in-python/


# # Python 2

# txt = raw_input("Type something to test this out: ")
# print "Is this what you just said?", txt

# Python 3

txt = input("Type something to test this out: ")

# Note that in version 3, the print() function
# requires the use of parenthesis.
print("Is this what you just said? ", txt)

# An input is requested and stored in a variable
test_text = input ("Enter a number: ")

# Converts the string into a integer. If you need
# to convert the user input into decimal format,
# the float() function is used instead of int()
test_number = int(test_text)

# Prints in the console the variable as requested
print ("The number you entered is: ", test_number)

# or this way:
test_number = int(input("Enter a number: "))

# Input Exception Handling
test2word = input("Tell me your age: ")
test2num = int(test2word)
print("Wow! Your age is ", test2num)

# Now let's see how we would make this code safer to handle user input:

test3word = input("Tell me your lucky number: ")

try:
    test3num = int(test3word)
    print("This is a valid number! Your lucky number is: ", test3num)
except ValueError:
    print("This is not a valid number. It isn't a number at all! This is a string, go and try again. Better luck next time!")

# a complete example:

# Makes a function that will contain the
# desired program.
def example():

    # Calls for an infinite loop that keeps executing
    # until an exception occurs
    while True:
        test4word = input("What's your name? ")

        try:
            test4num = int(input("From 1 to 7, how many hours do you play in your mobile?" ))

        # If something else that is not the string
        # version of a number is introduced, the
        # ValueError exception will be called.
        except ValueError:
            # The cycle will go on until validation
            print("Error! This is not a number. Try again.")

        # When successfully converted to an integer,
        # the loop will end.
        else:
            print("Impressive, ", test4word, "! You spent", test4num*60, "minutes or", test4num*60*60, "seconds in your mobile!")
            break

# The function is called
example()
