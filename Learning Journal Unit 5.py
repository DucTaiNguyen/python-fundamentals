prefixes = 'JKLMNOPQ'



suffix = 'ack'



for letter in prefixes:

    if letter == 'O':

        print(letter + 'u' +suffix)

    elif letter == 'Q':

        print(letter + 'u' +suffix)

    else:

        print(letter + suffix)


""" 
output:

Jack
Kack
Lack
Mack
Nack
Ouack
Pack
Quack
>>> 
""""

#2. Give at least three examples that show different features of string slices. Describe the feature illustrated by each example. Invent your own examples. Do not copy them for the textbook or any other source.

s="I am very happy"
print(s[0:5])       # return the part of the string from 0-eth to the 5-eth, include the first but not the last
print(s[5:len(s)])  # return the part of the string from 5-eth to the length-eth of string, including the first but not the last
print(s[:9])        # the slice starts at the beginning of the string
print(s[10:])       # the slice goes to the end of the string
print(s[6:6])       # empty string

"""
output
I am 
very happy
I am very
happy

>>> 
"""
