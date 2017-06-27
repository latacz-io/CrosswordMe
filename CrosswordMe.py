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

    words = ["ngong", "looooong"]
    user_input = ""
    words.sort(key=len, reverse=True)

    return words

def define_field_size():
    #defines field size
    global line_count
    line_count = 12
    global column_count
    column_count = 12

def calculate_postions(word_length):

    start_x_position = randint(0, column_count-word_length)
    start_y_position = randint(0, line_count-word_length)
    end_x_position = start_x_position+word_length
    end_y_position = start_y_position+word_length

    return start_x_position, start_y_position, end_x_position, end_y_position

def calculate_fits(word, word_index, puzzle):

    fit = 0

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
                    word_direction = 0

def write_horizontal(words, word_index, puzzle):
    if word_index == 0:

        start_x_position, start_y_position, end_x_position, end_y_position = calculate_postions(len(words[word_index]))
        line = randint(0, line_count-1)

        word_position = 0 #resets the word_position. this is needed beacuse word_position counts through the length of every word being written
        for array_position in range(start_x_position, end_x_position): #Loops through position within the array

            puzzle[line][array_position] = words[word_index][word_position] #Writes the word at random position of the array
            word_position += 1 #Fake loop for the word position

    else: #every word which isnt the first


                    """ # test prints print("Word: ", words[word_index], "; Line: ", line, "; First array_position: ", array_position)#, "; Fit: " ,fit[len(fit)-1])
                if len(fit) > 0:
                    print("; Fit: " ,fit[len(fit)-1])"""

    return puzzle

def write_vertical(words, word_index, puzzle):
    if word_index == 0:

        start_x_position, start_y_position, end_x_position, end_y_position = calculate_postions(len(words[word_index]))
        column = randint(0, column_count-1)

        word_position = 0 #resets the word_position. this is needed beacuse word_position counts through the length of every word being written
        for array_position in range(start_y_position, end_y_position): #Loops through position within the array

            puzzle[array_position][column] = words[word_index][word_position] #Writes the word at random position of the array
            word_position += 1 #Fake loop for the word position

    return puzzle

def write_diagonal(words, word_index, puzzle):
    if word_index == 0:

        start_x_position, start_y_position, end_x_position, end_y_position = calculate_postions(len(words[word_index]))

        word_position = 0 #resets the word_position. this is needed beacuse word_position counts through the length of every word being written
        for x_position, y_position in zip(range(start_x_position, end_x_position), range(start_y_position, end_y_position)): #Loops through position within the array

            puzzle[y_position][x_position] = words[word_index][word_position] #Writes the word at random position of the array
            word_position += 1 #Fake loop for the word position

    return puzzle

def create_puzzle(words):
    # creates an array with "$" symbols to be the field and loops through the words being written
    puzzle = [["$" for x in range(column_count)] for y in range(line_count)] #Creates array filled with "$"

    for word_index in range(len(words)): #loops through every word in the words list

        if word_index == 0: #Special case for the first word which is written in a random position in a random direction on the board
            word_direction = randint(0,2) #Random direction
            start_x_position = randint(0, column_count-word_length) #Random x position within the boundries
            start_y_position = randint(0, line_count-word_length) #Random y position within the boundries

            if word_direction == 0:
                puzzle = write_horizontal(words, word_index, puzzle)
            elif word_direction == 1:
                puzzle = write_vertical(words, word_index, puzzle)
            elif word_direction == 2:
                puzzle = write_diagonal(words, word_index, puzzle)



    return puzzle

words = word_input()
define_field_size()
puzzle = create_puzzle(words)
print_puzzle(puzzle)
