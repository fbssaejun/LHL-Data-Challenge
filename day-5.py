'''

Challenge
Dot wants to visit all the London landmarks where the wait time is less than 15 minutes. We have a dictionary called landmarks, within which landmark names are keys and wait times are their respective values.

Using Python, develop a list of the landmarks where the wait time is less than 15 minutes. What will be the length of the list?

'''

# Landmarks dictionary
landmarks = {
    "Big Ben": 12,
    "Tower Bridge": 25,
    "Buckingham Palace": 15,
    "Madame Tussauds": 25,
    "London Eye": 40,
    "Tower of London": 25,
    "Emirates Air Line cable car": 16,
    "London Transport Museum": 7,
    "Wembley Stadium": 8,
    "Hyde Park": 0,
    "The View from The Shard": 14
}


def find_less_wait_time():
    # create emppty array variable to store wanted values
    less_wait_time = []
    for location in landmarks:
        # check wanted condition
        if landmarks[location] < 15:
            # append name of landmark to empty array
            less_wait_time.append(location)
    # return the array
    return less_wait_time

print(find_less_wait_time()) # => ['Big Ben', 'London Transport Museum', 'Wembley Stadium', 'Hyde Park', 'The View from The Shard']
