import random

def generate_word_for_game():
    file = "text-word.txt"
    with open(file) as open_file:
        read_file = open_file.read ()
    word_list = str.split(read_file)
    index = random.randint(0, (len(word_list)- 1))
    answer = word_list [index]
    return answer 

def compare_guess_to_word(guess, word):
    # this will take user_guess variable and computer_word variable
    if guess in word:
        print(f'{guess} is in the mystery word')
        # change display to show where the guess is
    else:
        print(f'{guess} is not in the mystery word.')
        #decrement number of guesses left  
    return guess       

def get_word_to_guess():
    open_file = open('test-word.txt')
    #print(open_file.read())
    string_word = str(open_file.read())
    #print(string_word)
    return string_word

def user_guess():
    user_inpt = input("Guess a letter: ")
    if user_inpt.isalpha():
        letter = user_inpt
        return letter
    else:
        print("That guess was not a letter.")
        return user_guess()

def guess_character():
    user_guess = input('Guess a letter: ')  
    if len(user_guess) == 1 and user_guess.isalpha():
        user_guess = user_guess.lower()
        print(f'You guessed {user_guess}')
        return user_guess  
    else:    
        print('Your guess is not a single letter.')   
        return guess_character()    

    the_input = user_guess()
    # print(the_input)

def play_game():
    get_word = get_word_to_guess()
    def split(get_word):
        return list(get_word)
    split_list = split(get_word)
    # print(split_list)
    guesses = []
    while len(guesses) <= 8:
        guesses.append(guess_character())
    new_list = [(item.replace(item, "_")) for item in split_list]
    print(new_list)

if __name__ == "__main__":
    play_game()