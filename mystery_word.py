import random

def generate_word_for_game():
    file = "test-word.txt"
    with open(file) as open_file:
        read_file = open_file.read ()
    word_list = str.split(read_file)
    index = random.randint(0, (len(word_list)- 1))
    answer = word_list [index]
    return answer 

def guess_character():
    user_guess = input('Guess a letter: ')  
    if len(user_guess) == 1 and user_guess.isalpha():
        user_guess = user_guess.lower()
        # print(f'You guessed {user_guess}')
        return user_guess  
    else:    
        print('Your guess is not a single letter.')   
        return guess_character()    

def play_game():
    get_word = generate_word_for_game()
    def split(get_word):
        return list(get_word)
    split_list = split(get_word)
    # print(split_list)
    new_list = [(letter.replace(letter, "_")) for letter in split_list]
    guesses = []
    while len(guesses) < 8:
        guesses.append(guess_character())
        new_list = [(letter.replace(letter, "_")) if letter not in guesses else letter for letter in split_list] 
        print(new_list)

if __name__ == "__main__":
    play_game()