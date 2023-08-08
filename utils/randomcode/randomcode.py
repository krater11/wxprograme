import random


def RandomCode():
    randnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    random_code = ""
    for i in range(6):
        random_code += randnumber[(random.randint(0, 9))]
    print(random_code)
    return random_code
