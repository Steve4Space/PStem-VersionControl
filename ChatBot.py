import random

def ask(say, ur, ur1, ur2):
    print(say)
    print(ur, "/n", ur1, ur2)
    response = input("1, 2, or 3\n")
    return(response)
    
def main():
    import random
    random = random.randint(0, 2)
    responses = ["How're you?", "Why did you wane me up?! Fine, how're you, i'll be nice.. maybe", "What. Fiiiiiinnnnnnnneeeeeeeeee. How're you???"]
    humanr = ["Good!", "Bad:(", "Fine.", "Decent."]
    input = ask("Hello, " + responses[random], humanr[0], humanr[1], humanr[2])
    
main()
