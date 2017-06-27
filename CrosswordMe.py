from random import randint
from random import sample

def print_puzzle(puzzle):
    #Prints the puzzle puzzle on a board
    for line in range(line_count):
        for position in range(column_count):
            print(str(puzzle[line][position]) + " ", end="") #Prints character in current position
        print() #Prints Newline

def word_input():
    #Collects the words for the puzzle and sorts them by lenght descending

    words = ["one", "looooong"]
    user_input = ""
    words.sort(key=len, reverse=True)

    return words

def define_field_size():
    #defines field size
    global line_count
    line_count = 12
    global column_count
    column_count = 12


def calculate_fits(puzzle, current_word):

    fit = 0

    for puzzle_y_position in range(line_count): #loops through every position in the lines
        for puzzle_x_position in range(column_count): #loops through every position in the columns

            position_puzzle_letter_in_word = current_word.find(puzzle[puzzle_y_position][puzzle_x_position]) # Checks if the letter in the puzzle is within the current word
            #print("Puzzle Letter: " + puzzle[puzzle_y_position][puzzle_x_position] + ";Word Letter: " + current_word[position_puzzle_letter_in_word] + "; Score: " + str(position_puzzle_letter_in_word))

            if position_puzzle_letter_in_word >= 0: #The letter in the puzzle is the same as on of the current_word

                # horizontal
                horizontal_fit = 0
                if puzzle_x_position - position_puzzle_letter_in_word >= 0 and puzzle_x_position + (len(current_word)-1-position_puzzle_letter_in_word) < column_count: #Makes shure the horizontal Puzzle index doenst get out of range to the left and to the right
                    for word_postion in range(len(current_word)):
                        if puzzle[puzzle_y_position][puzzle_x_position - position_puzzle_letter_in_word + word_postion] == current_word[word_postion]:
                            horizontal_fit += 1

                        elif puzzle[puzzle_y_position][puzzle_x_position - position_puzzle_letter_in_word + word_postion] != current_word[word_postion] and puzzle[puzzle_y_position][puzzle_x_position - position_puzzle_letter_in_word + word_postion] != "$":
                            horizontal_fit = -1
                            break

                    if horizontal_fit >= fit:
                        #print(horizontal_fit)
                        fit = horizontal_fit
                        start_x_position = puzzle_x_position - position_puzzle_letter_in_word
                        start_y_position = puzzle_y_position
                        word_direction = 0

    if fit == 0: #Temp writing at 0,0,horizontal to simulate what happens if there is no fit at all
        start_x_position, start_y_position, word_direction = 0, 0, 0

    return start_x_position, start_y_position, word_direction

    """ oooooold

    for line in range(line_count): #Calculates horizontal fits
        for array_position in range(column_count-len(words[word_index])+1): # loops through every position in the line

            if puzzle[line][array_position] == words[word_index][0]: #Checks if the postion is the same as the first letter in the word
                temp_fit = 1
                for letter in range(1, len(words[word_index])): #loops through letters of the word
                    if puzzle[line][array_position+letter] == words[word_index][letter]: #checks if the letter is the same as the letter on the board
                        temp_fit +=1

                    elif puzzle[line][array_position+letter] != words[word_index][letter] and puzzle[line][array_position+letter] != "$": #breaks and deletes temp_fit score, when a letter is different and the field is not empty (represented by "$")
                        temp_fit = -1
                        break

                if temp_fit >= fit:
                    start_x_position = array_position
                    start_y_position = line
                    word_direction = 0"""

def write_puzzle(puzzle, current_word, start_x_position, start_y_position, word_direction):

    word_position = 0 #resets the word_position. this is needed beacuse word_position counts through the length of every word being written

    if word_direction == 0:
    # writes horizontal
        for puzzle_x_position in range(start_x_position, start_x_position+len(current_word)): #Loops through position within the puzzle

            puzzle[start_y_position][puzzle_x_position] = current_word[word_position] #Writes the word at random position of the array
            word_position += 1 #Fake loop for the word position


    elif word_direction == 1:
    # writes vertical
        for puzzle_y_position in range(start_y_position, start_y_position+len(current_word)): #Loops through position within the puzzle

                puzzle[puzzle_y_position][start_x_position] = current_word[word_position] #Writes the word at random position of the array
                word_position += 1 #Fake loop for the word position


    elif word_direction == 2:
    # writes diagonal
        for puzzle_x_position, puzzle_y_position in zip(range(start_x_position, start_x_position+len(current_word)), range(start_y_position, start_y_position+len(current_word))): #Loops through position within the array

            puzzle[puzzle_x_position][puzzle_y_position] = current_word[word_position] #Writes the word at random position of the array
            word_position += 1 #Fake loop for the word position


    return puzzle


def create_puzzle(words):
    # creates an array with "$" symbols to be the field and loops through the words being written
    puzzle = [["$" for x in range(column_count)] for y in range(line_count)] #Creates array filled with "$"

    for word_index in range(len(words)): #loops through every word in the words list

        if word_index == 0: #Special case for the first word which is written in a random position in a random direction on the board
            word_direction = randint(0,2) #Random direction
            start_x_position = randint(0, column_count-len(words[word_index])) #Random x position within the boundries
            start_y_position = randint(0, line_count-len(words[word_index])) #Random y position within the boundries

        else: #For every word after the first one
            start_x_position, start_y_position, word_direction = calculate_fits(puzzle, words[word_index])

        puzzle = write_puzzle(puzzle, words[word_index], start_x_position, start_y_position, word_direction)




    return puzzle

words = word_input()
define_field_size()
puzzle = create_puzzle(words)
print_puzzle(puzzle)
