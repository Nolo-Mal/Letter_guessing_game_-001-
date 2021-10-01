import random
import sys


def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    return input('Guess the missing letter: ')


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words): # select a random letter in the word
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip() #revome the white spaces "\n"
    return word


# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    letter = word[random.randint(0, len(word)-1)]
    space = "" #created an empty string so that i can fill in missing word with an "_"
    for i in range(len(word)): #for every letter in the length of the word
        if word[i]!= letter: # for every letter that is not sected randomly print "_"
            space+="_"
        else:
            space+=letter #add the letter to the word.
    return space

# TODO: Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):
    if char in  original_word and char not in answer_word: # supports above function. 
        return True
    else:
        return False
        

# TODO: Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
    index_char = original_word.find(char) # find the index letter of the word.
    if index_char != -1: 
        answer_list = list(answer_word) # the answered word will be added in a list(answer_list) 
        answer_list[index_char] = char # to identify the index to the character 
        answer_word = "".join(answer_list) #it joins the answered words to print one word.
    return answer_word


def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    print(answer) 
    return answer


# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):
    if answer:
        print('Wrong! Number of guesses left: '+str(number_guesses))
        draw_figure(number_guesses)


# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
    if number_guesses == 4:
        print("""/----
|
|
|
|
_______""")
    elif number_guesses == 3:
        print("""/----
|   0
|
| 
| 
_______""")
    elif number_guesses == 2:
        print("""/----
|   0
|  /|\\
|  
| 
_______""")
    elif number_guesses == 1:
        print("""/----
|   0
|  /|\\
|   |
| 
_______""")
        
    elif number_guesses == 0:
        print("""/----
|   0
|  /|\\
|   |
|  / \\
_______""")

# TODO: Step 2 - update to loop over getting input
# TODO: step 3 - update loop to exit game if user types 'exit' or 'quit'
# TODO: Step 6 - update to get words_file to use from commandline argument

def run_game_loop(word, answer):
    guesses = 5
    print("Guess the word: " +str(answer)) #convert letter to string.
    while True: #checks if the conditions are true.
        guess = get_user_input() 
        if guess.lower() == 'quit' or guess.lower() == 'exit':
            print("Bye!")
            break
        if is_missing_char(word, answer, guess):
            answer = do_correct_answer(word,answer,guess)
        else:
            guesses -= 1 #supports the number of guesses or the number of tries
            do_wrong_answer(answer, guesses)
            if guesses == 0: #supports the number of the guesses or the number of tries.
                print("Sorry, you are out of guesses. The word was: " + word)
                break
        if answer == word:  
                break

if __name__ == "__main__":
    try:
        file = sys.argv[1]
        if "txt" in sys.argv[1].split("."): 
            words = read_file(sys.argv[1]) #read the words inside the .txt file we created.
            selected_word = select_random_word(words)
            current_answer = random_fill_word(selected_word)

            run_game_loop(selected_word, current_answer)
    except IndexError:
        words_file = ask_file_name()
        words = read_file(words_file)
        selected_word = select_random_word(words)
        current_answer = random_fill_word(selected_word)

        run_game_loop(selected_word, current_answer)

