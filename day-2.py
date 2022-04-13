'''

Challenge

Modify the name on Dot’s passport so it can be recognized by passport control. Which combination of string functions will give us the right results?

name: Dot

Required format: #DOT!

'''

# Variable
name = '  Dot  '

# Solution
print('#' + name.strip().upper() + '!') # => #DOT!
