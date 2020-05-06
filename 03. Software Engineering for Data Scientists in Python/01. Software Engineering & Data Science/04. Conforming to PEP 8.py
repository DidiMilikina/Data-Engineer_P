'''
Conforming to PEP 8
As we've covered, there are tools available to check if your code conforms to the PEP 8 guidelines. One possible way to stay compliant is to use an IDE that warns you when you accidentally stray from the style guide. Another way to check code is to use the pycodestyle package.

The results below show the output of running pycodestyle check against the code shown in your editor. The leading number in each line shows how many occurrences there were of that particular violation.

my_script.py:2:2:  E225 missing whitespace around operator
my_script.py:2:7:  E231 missing whitespace after ','
my_script.py:2:9:  E231 missing whitespace after ','
my_script.py:5:7:  E201 whitespace after '('
my_script.py:5:11: E202 whitespace before ')'
Instructions
100 XP
Leverage the output of pycodestyle to edit the code to be compliant with PEP 8.
'''
SOLUTION

# Assign data to x
x = [8, 3, 4]

# Print the data
print(x)
