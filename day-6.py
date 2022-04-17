'''

Challenge
The airport uses sensors to keep track of all its airplane gates, and monitor which ones are available. Every time an airplane needs to park at a gate, the system directs them to an available spot for that particular airplane type, or notifies them that no spots are available.

We need to write a function called find_the_gate() that returns the coordinates of an available gate, or returns false if there is no available spot. Our function receives a list representing all gates, and a string with the type of airplane that is looking for a gate.

There are 2 kinds of possible airplanes: Narrow-Body (Single aisle) or Wide-Body.

Wide-Body planes can only use gates in W spots.
Narrow-Body planes can use gates in either N** or **W spots.
In the list of gates, gates are written in either lower-case or upper-case. An upper-case letter means that the particular gate is AVAILABLE, while a lower-case letter means that the gate is UNAVAILABLE.

Our function must return a number with the position of the gate where the airplane can park. See the example input and output below for an illustration.

Note: There may be multiple available spots for a particular airplane. If that happens, our function should return the first possible spot to minimize the airplane taxiing time. If there are no available gates, remember to return boolean value False.

'''

def find_the_gate(spots, type):
    # Loop through spots array in range of its length
    for i in range(len(spots)):
        # if the wanted plane type is wide and finds first available wide spot, return the index of array
        if type == 'wide' and spots[i] == 'W':
            return i
        # if the wanted plane type is narrow and finds first available narrow or wide spot, return the index of array
        elif type == 'narrow' and (spots[i] == 'N' or spots[i] == 'W'):
            return i

print(find_the_gate(['w','n','n','w','N','n','w','N','N','w','n','n','w','n','n','W','W','W','W','n','n','w','n','n'], 'wide')) # => 15

