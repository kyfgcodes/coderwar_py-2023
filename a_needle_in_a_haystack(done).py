'''Can you find the needle in the haystack?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle'''

def find_needle(haystacks):
    
    for i in haystacks:
        if i == 'needle':
            return f'found the needle at position {haystacks.index(i)}'

print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))

#Done!!!