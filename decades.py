age = int(input('How old are you?\n'))

decades = age // 10
years = age % 10
message = 'You are ' + str(decades) + ' decades and\n' + str(years) + ' year(s) old.'

print(message)
