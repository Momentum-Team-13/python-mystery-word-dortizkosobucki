import random

def generate_word_for_game():
    file = "words.txt"
    with open(file) as open_file:
        read_file = open_file.read ()
    word_list = str.split(read_file)
    index = random.randint(0, (len(word_list)- 1))
    answer = word_list [index]
    return answer 

def make_spaces():
    get_word = generate_word_for_game()
    # print (get_word)
    def split(get_word):
        return list(get_word)
    split_list = list(get_word)
    spaces = " _ " * len (split_list)
    print (f"Welcome to Mystery Words - Your Word to Guess Contains {len(split_list)} Letters")
    print(spaces)
    return split_list  

def guess_against_word(split_list):
    correct_letters = []
    incorrect_letters = []
    display = [(letter.replace(letter, "_")) if letter not in correct_letters else letter for letter in split_list]
    # print(display)
    while len(incorrect_letters) < 8:
        letter = input("Guess a letter:")
        if letter.isalpha() and len(letter) == 1:
            lowercase_guess = letter.lower()
            if lowercase_guess in split_list:
                correct_letters.append(lowercase_guess)
                print (f'Good job, {lowercase_guess} is in the word.')
                display = [(letter.replace(letter, " _ "))if letter not in correct_letters else letter for letter in split_list]
                print (display)
                if display == correct_letters:
                    print ('You guessed all the letters correctly! Way to go.')
                    break
            else: 
                print(f'{lowercase_guess} is not in the word, try again!')
                incorrect_letters.append(lowercase_guess)
        else:
            print (f"That guess wasn't valid, please try again!")
        print(f'Letters already guessed:{incorrect_letters + correct_letters}')
    print ("Game Over!")

def play_game():
    split_list = make_spaces()
    start_play = guess_against_word(split_list)

if __name__ == "__main__":
    play_game()
