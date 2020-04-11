length = input('Please enter the length of your field in feet: ')
width = input('Please enter the length of your field in feet: ')

length = int(length)
width = int(width)

area = (length * width)
acre_conversion_constant = 43560
acre_area = str(round((area/acre_conversion_constant), 2))

print ('The area of your field is: ' + acre_area + 'acres' )