import random, time

def printlist(right_list):
    stringtoprint=""
    h=0
    for h in range(len(right_list)):
        stringtoprint=stringtoprint + right_list[h]
    print(stringtoprint)

def computer_play(possible_words, right_list, wrong_list):
    temp_possible_words = possible_words.copy()
    for loop in range (len(possible_words)):
        word_matches=1
        for loop2 in range(len(right_list)):
            if right_list[loop2] != "_" and possible_words[loop][loop2] != right_list[loop2]:
                word_matches = 0
        if word_matches == 0 and possible_words[loop] in temp_possible_words:
            temp_possible_words.remove(possible_words[loop])

        for loop2 in range(len(wrong_list)):
            if wrong_list[loop2] in possible_words[loop] and possible_words[loop] in temp_possible_words:
                temp_possible_words.remove(possible_words[loop])

    possible_words = temp_possible_words.copy()

    counters = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for loop in range (len(possible_words)):
        for loop2 in range(len(possible_words[loop])-1):
            which_letter = ord(possible_words[loop][loop2]) - 97
            counters[which_letter] = counters[which_letter]+1

    found_guess = 0
    while (found_guess == 0):
        most_used_index = counters.index(max(counters))
        most_used_letter = chr(97+most_used_index)
        if ((most_used_letter not in right_list) and (most_used_letter not in wrong_list)):
            found_guess = 1
        else:
            counters[most_used_index] = 0

    guess = most_used_letter
    return guess

board=[

'''   +---+
       |
       |
       |
      ===''',
'''   +---+
   O   |
       |
       |
      ===''',
'''   +---+
   O   |
   |   |
       |
      ===''',
'''   +---+
   O   |
   |\\  |
       |
      ===''',
'''   +---+
   O   |
  /|\\  |
       |
      ===''',
'''   +---+
   O   |
  /|\\  |
   |   |
      ===''',
'''   +--+
   O  |
  /|\\ |
   |\\ |
     ===''',
'''   +--+
   O  |
  /|\\ |
  /|\\ |
     ===''']


filename = "hangman_words.txt"
file = open(filename,"r")

possible_words = file.readlines()
random_word=possible_words[random.randint(1,len(possible_words))]
file.close()

secret = random_word
wrong_list=[]
right_list=[]
for c in range(len(secret)-1):
    right_list.append ("_")


temp_possible_words = possible_words.copy()

for loop in range (len(possible_words)):
    if (len(possible_words[loop])-1) != len(right_list):
        temp_possible_words.remove(possible_words[loop])
possible_words = temp_possible_words.copy()

errorcount=0
winstatus = 0
while (errorcount < 7 and winstatus == 0):
    print(board[errorcount])
    print("Incorrect letters:")
    printlist(wrong_list)
    print("Word:")
    printlist(right_list)
    guess = ""
    guess = computer_play(possible_words, right_list, wrong_list)
    print("The computer guesses " + guess)
    time.sleep(1)
    if guess in secret:
        print("Correct")

        for c in range(len(secret)):
            if secret[c]==guess:
                right_list[c]=(guess)

    if guess not in secret:
        print("Incorrect")
        wrong_list.append(guess)
        errorcount=errorcount+1

    if "_" not in right_list:
        winstatus = 1

if (errorcount == 7):
    print(board[7])
    print("The computer lost!")
    print("The word was: ")
    print(secret)
if (winstatus == 1):
    printlist(right_list)
    print("You got it, Good Job!")
    print("The word was: ")
    print(secret)