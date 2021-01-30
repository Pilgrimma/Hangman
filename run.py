import nltk, random

word = ""
word_len = 0
word_string = ""
letters_found = 0
used_list = []
hangman = ""

def print_info(wrongs):
    print("\n")
    global hangman
    print(hangman)
    print(word_string)
    print("Letters used: " + str(used_list).replace("[","").replace("]","").replace("'",""))

def change_hangman(wrongs):
    global hangman
    if wrongs == 1:
        hangman = hangman[:42]+"0"+hangman[43:]
    elif wrongs == 2:
        hangman = hangman[:52]+"|"+hangman[53:]
        hangman = hangman[:62]+"|"+hangman[63:]
    elif wrongs == 3:
        hangman = hangman[:51]+"\\"+hangman[52:]
    elif wrongs == 4:
        hangman = hangman[:53]+"/\n"+hangman[54:]
    elif wrongs == 5:
        hangman = hangman[:72]+"/"+hangman[73:]
    elif wrongs == 6:
        hangman = hangman[:74]+"\ \n"+hangman[75:]

def set_game():
    ran_number = round(random.uniform(0, (len(words_list) -1)))
    global word
    word = words_list[ran_number]
    global word_len
    word_len = len(word)
    global word_string
    word_string = ""
    for letter in word:
        word_string += "_"
    global letters_found
    letters_found = 0
    global used_list 
    used_list = []
    global hangman
    hangman = "  ------   \n |      | \n |      | \n |       \n |       \n |       \n |       \n |       \n/ \\"

def run_game():
    wrongs = 0
    global word_string
    global letters_found
    global word_len
    while (wrongs != 6):
        letter = input("Enter a letter")
        if (len(letter) != 1) or (letter.isalnum() != True) or (letter.isnumeric() == True):
            print("Please enter a valid letter.")
            print_info(wrongs)
            continue
        found = False
        i = 0
        if letter in used_list:
            print("You already used this letter!")
            print_info(wrongs)
            continue
        else:
            used_list.append(letter)
        while i < word_len:
            if word[i] == letter:
                found = True
                word_string = word_string[:i]+letter+word_string[i+1:]
                letters_found += 1
            i += 1
        if found == True:
            print("The letter '" + letter + "' is in the word.")
            print_info(wrongs)
            if letters_found == word_len:
                print("Congratulations! You win!")
                end_game()
        else:
            print("The letter '" + letter + "' is not found in the word.")
            wrongs += 1
            change_hangman(wrongs)
            print_info(wrongs)
    if wrongs == 6:
        print("Game over!")
        end_game()

def end_game():
    answer = False
    while answer == False:
        inp = input("Do you want to play again? Y/N")
        if inp == "Y":
            set_game()
            run_game()
        elif inp == "N":
            exit()
        else:
            print("Please answer with Y (Yes) or N (No)")

words_listf = open("Words.txt", encoding="utf-8")
words_list = words_listf.read()
words_listf.close()
words_list = nltk.word_tokenize(words_list)

set_game()
run_game()