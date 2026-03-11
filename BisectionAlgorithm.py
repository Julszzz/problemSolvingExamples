# this code calculates the cube root of a number
# using a bisection algorithm

cube = 1000
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low)/2.0
while abs(guess**3 - cube)>=epsilon:
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print('Number of guesses =',num_guesses)
print(guess,'is close to the cube root of',cube)
