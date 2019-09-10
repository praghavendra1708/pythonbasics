""" Date time sample """

from datetime import date

now = date.today()
birthday = date(1981, 1, 7)

age = now - birthday

print(f'age :{age}')

