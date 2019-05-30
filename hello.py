# simple hellow world program that has a basic greeting conversation with user

print('Hello World!')     # greet user
print('What is your name?')    # ask for user's name
myName = input()    # user input name
print('It\'s nice to meet you ' + myName)    # responds to user input
print('the length of your name is:')    # find length of name and prints length
print(len(myName))
print('What is your age?')    # asks for age
myAge = input()    # user input age integer
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
