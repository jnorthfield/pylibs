# Numbers

2 ** 16   #2 to the 16th power

5//4    #floor

6 % 4   #mod or remainder

t = 2

y = 16

id(t)

id(y)

t is y

t == y

t > y

t < y

t != y

z = 2/5, 2/5.0                  # Integer / truncates in 2.X, but not 3.X

type(z)     #TUPLE

type(z[0])  #FLOAT

number = input('Enter a number?')  #INPUT FROM USER

type(number)  #Returns a string

numa, numb = 7, 6

# Strings

S = "green" + "eggs"                   # Concatenation

S = S + " ham"

S.find('eggs')

S * 5                             # Repetition

S[:2]                             # Read from the left to the 2 position (non-inclusive)

S[-1:]                            #Read from the right to the end

S[:-1]                            #Read from the left to the -1 position (non-inclusive)

"green %s and %s" % ("eggs", S)   # Formatting - the old c way - not scalable

'green {0} and {1}'.format('eggs', S)  #Python3 - pythonic, scalable, uses python's auto-typing

S[0] = 'p'                         #Immutable - Cannot change the string

num = '5678'
num.isnumeric()

num = 'x54r'
num.isnumeric()

num.            #PLENTY OF METHODS ASSOCIATED WITH STRINGS

my_s = "7, 14, 6, 30"

my_s.split(',')

new_s = "   Supercali   "
new_s.strip()

# Lists

L = [4,5,6] + [1,2,3]            # List operations

L, L[:], L[:0], L[-2], L[-2:]


([1,2,3]+[4,5,6])[2:4]

[L[2], L[3]]                      # Fetch from offsets; store in a list

L.reverse(); L                    # Method: reverse list in place

L.sort(); L                       # Method: sort list in place

L.index(4)                        # Method: offset of first four (search)
3

L.append(75)

L.__len__()

len(L)
#######################################################

