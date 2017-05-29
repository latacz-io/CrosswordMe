from random import randint

#input

words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
user_input = ""

"""while 1 == 1:
    user_input = input("Word: ")
    if user_input.lower() == "done":
        break
    words.append(user_input)"""

# creating the puzzle
## horizontals
line = randint(0,9) #First line to write in
lines_used = [] #Empty array which contains lines which have been written in already (can probably be removed when its possible to write multiple words in one line)

puzzle = [["$" for x in range(10)] for y in range(10)] #Creates 10x10 array filled with "$"

for word in range(0, len(words)): #loops through every word in the words list

    lines_used.append(line) #appends used lines to used lines list

    word_position = 0 #resets the word_position. this is needed beacuse word_position counts through the length of every word being written

    start_position = randint(0, 10-len(words[word])) #int for start_position
    end_position = start_position+len(words[word]) #int for end_position

    for array_position in range(start_position, end_position): #Loops through position within the array

        puzzle[line][array_position] = words[word][word_position] #Writes the word at random position of the array
        word_position += 1 #Fake loop for the word position

    line = randint(0,9) #Choosees new line
    while line in lines_used: #keeps creating a new line as long as the line has been used alreard
        line = randint(0,9)


#Prints the puzzle
for line in range(10):
    for position in range(10):
        print(str(puzzle[line][position]) + " ", end="") #Prints character in current position
    print() #Prints Newline
