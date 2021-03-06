import random
correct = 'You Guessed It Correctly'

too_low = 'Too Low!!!'

too_high = 'Too High'


def configure_range():

    lowNumber = int(input("lowest number possible "))
    highNumber = int(input("highest number possible "))

    '''Set the high and low values for the random number'''
    return lowNumber, highNumber


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    while True:
        try:
            return int(input('Guess the secret number? '))
        except:
            print('Only excepts numbers')


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():

    (low, high) = configure_range()
    secret = generate_secret(1, 30)
    counts = 0

    question = input('Wanna play a game (Enter any character to play): ')
    while question:
        guess = get_guess()
        result = check_guess(guess, secret)
        counts += 1
        print('You tried ' + result)

        if result == correct:
            print(counts)
            question = input('Wanna play a again (Enter any character to play): ')
            


if __name__ == '__main__':
    main()
