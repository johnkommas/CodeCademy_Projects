# TODO
"""
Setting up

1.
Declare a variable `name` and assign it to the name of the person who will be asking the Magic 8-Ball.

2.
Next, declare a variable `question`, and assign to a “Yes” or “No” question you’d like to ask the Magic 8-Ball.

3.
We want to store the answer of the Magic 8-Ball in another variable, which we’ll call `answer`.
For now, assign this variable to an empty string.

4.
In order for the answer to be different each time we run the program, we will utilize randomly generated values.
In Python, we can use the .randint() function from the random module to generate a random number from a range.

5.
Next, we’ll create a variable to store the randomly generated value.
Declare a variable called random_number, and assign it to the function call:
random.randint(1, 9)
which will generate a random number between 1 (inclusive) and 9 (inclusive).
Next, add a print() statement that outputs the value of random_number,
and run the program several times to ensure random values are being generated as expected.
Once you’re sure this is working as we expected, feel free to comment out this print() statement.

6.
Now that we’ve declared all the variables needed, it’s time to implement the core logic of our program!
For this section, we’ll be utilizing control flow using an if/elif/else statement
to assign different answers for each randomly generated value.
First, write an if statement where if the random_number is equal to 1,
answer is assigned to the phrase “Yes - definitely.”
"""
import random
from answers import answer


def run(__name):
    question = input("ΤΟ ΕΡΩΤΗΜΑ ΣΟΥ: ")
    if len(question) > 0:
        print(f"{__name} ΡΩΤΗΣΕ: {question}" if len(__name) > 0 else f'ΑΝΩΝΥΜΟ ΕΡΩΤΗΜΑ: {question}')
        print(f'ΑΠΑΝΤΗΣΗ: {answer.get(random.randint(1, len(answer)), "ΣΦΑΛΜΑ")}')
    else:
        return run(__name)
    return __name


name = ''
while True:
    try:
        if len(name) == 0:
            name = input('ΤΟ ΟΝΟΜΑ ΣΟΥ: ')
        name = run(name)
    except KeyboardInterrupt:
        print("\nGood By!!")
        break

