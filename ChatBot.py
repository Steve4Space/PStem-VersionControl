import random, time

def ask(say, ur, ur1, ur2):
    time()
    print(say)
    print(ur, "\n", ur1, "\n", ur2)
    time()
    response = input("1, 2, or 3\n")
    return(response)
    
def main():
    import random
    random = random.randint(0, 2)
    responses = ["How're you?", "Why did you wane me up?! Fine, how're you, i'll be nice.. maybe", "What. Fiiiiiinnnnnnnneeeeeeeeee. How're you???"]
    humanr = ["Good!", "Bad:(", "Fine.", "Decent."]
    input = ask("Hello, " + responses[random], humanr[0], humanr[1], humanr[2])
    
def time(): #gotta prove python is slow
    import time
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    
main()
