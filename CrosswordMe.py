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

    words = ["one", "looooong", "hello", "chris", "glux"]
    user_input = ""
    words.sort(key=len, reverse=True)

    return words

def define_field_size():
    #defines field size
    global line_count
    line_count = 12
    global column_count
    column_count = 12

def set_direction_parameters(direction):
    #returns direction parameters
    if direction == 0: #horizontal
        x_counter = 1
        y_counter = 0

    elif direction == 1: #vertical
        x_counter = 0
        y_counter = 1

    elif direction == 2: #diagonal
        x_counter = 1
        y_counter = 1

    return x_counter, y_counter

def calculate_fits(puzzle, current_word):

    fit = 0

    for puzzle_y_position in range(line_count): #loops through every position in the lines
        for puzzle_x_position in range(column_count): #loops through every position in the columns
            for fit_direction in range(3): #loops through every direction

                x_counter, y_counter = set_direction_parameters(fit_direction)


                temp_fit = 0
                if (puzzle_x_position + len(current_word)) * x_counter <= column_count and (puzzle_y_position + len(current_word)) * y_counter <= line_count: #Makes shure the temp Puzzle index doenst get out of range  to the right

                    for word_position in range(len(current_word)):

                        if puzzle[puzzle_y_position + (word_position * y_counter)][puzzle_x_position + (word_position * x_counter)] == current_word[word_position]: #increases temp fit, if the letter of word and puzzle match

                            temp_fit += 1

                        elif puzzle[puzzle_y_position + (word_position * y_counter)][puzzle_x_position + (word_position * x_counter)] != current_word[word_position] and puzzle[puzzle_y_position + (word_position * y_counter)][puzzle_x_position + (word_position * x_counter)] != "$": #if the ltter doesn match and the puzzle postion isnt empty ("$"), then the fit socre is being resetted and the loop checking for temp is broken (which makes sense, since it the word doesnt fit horizontally for this x,y combination)

                            temp_fit = -1
                            break

                    if temp_fit > fit: #defines position and direction if its the best fit so far. With > it takes the first fit, with >= it takes the last. A non fit has to be "-1" if this is >=. Otherwise the last position of a non fit will be written into the variables. This doesnt matter as long as a fit = 0 is overwritten in the end. But stil, temporary there would be wrong informations in the variables
                        #print(temp_fit, current_word)
                        fit = temp_fit
                        start_x_position = puzzle_x_position
                        start_y_position = puzzle_y_position
                        word_direction = fit_direction



    if fit == 0: #Temp writing at 0,0,horizontal to simulate what happens if there is no fit at all
        start_x_position, start_y_position, word_direction = 0, 0, 0

    return start_x_position, start_y_position, word_direction


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
