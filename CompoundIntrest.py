user_input = input('Enter initial amount: ')
user_input = int(user_input)
years = 3

for i in range(years):
    user_input = user_input * 1.04 
    print ('In Year ' + str(i+1) + ' your savings account will have: $' + str(round(user_input, 2))) 