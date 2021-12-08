import random
from answers import answer
import time

def run(__name):
    step = [.2, .3]
    question = input("ΤΟ ΕΡΩΤΗΜΑ ΣΟΥ: ")
    if len(question) > 0:
        print(f"{__name} ΡΩΤΗΣΕ: {question}" if len(__name) > 0 else f'ΑΝΩΝΥΜΟ ΕΡΩΤΗΜΑ: {question}')
        print(f'ΑΠΑΝΤΗΣΗ: ', end='')
        x = answer.get(random.randint(1, len(answer)), "ΣΦΑΛΜΑ")
        for letter in x:
            print(letter, end='')
            time.sleep(random.choice(step))
        print()
    else:
        return run(__name)
    return __name


def app():
    name = ''
    while True:
        try:
            if len(name) == 0:
                name = input('ΤΟ ΟΝΟΜΑ ΣΟΥ: ')
            name = run(name)
        except KeyboardInterrupt:
            print("\nGood By!!")
            break

app()
