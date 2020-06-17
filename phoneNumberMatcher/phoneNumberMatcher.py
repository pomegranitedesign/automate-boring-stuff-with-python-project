#! python3
# phoneNumberMatcher.py - Finds all phone numbers from the text
import re

numberRegex = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
mo = numberRegex.search('My new number is: (647) 554-9993')
# print('Phone numbers found: ' + mo.group(1))
# print('Phone numbers found: ' + mo.group(2))
print(mo.groups()[0])
