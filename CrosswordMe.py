from random import randint
from random import sample
from random import choice
from string import ascii_lowercase

def print_puzzle(puzzle):
    #Prints the puzzle puzzle on a board
    for line in range(line_count):
        for position in range(column_count):
            print(str(puzzle[line][position]).upper() + " ", end="") #Prints character in current position
        print() #Prints Newline

def fill_field_with_randoms(puzzle):
    #Fills the rest of the free space (represented by "$") with random letters

    for puzzle_y_position in range(line_count):
        for puzzle_x_position in range(column_count):

            if puzzle[puzzle_y_position][puzzle_x_position] == "$":
                puzzle[puzzle_y_position][puzzle_x_position] = choice(ascii_lowercase)



    return puzzle

def word_input():
    #Collects the words for the puzzle and sorts them by lenght descending

    words = ["Test", "Noch", "Nocheiner"]
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
        x_activator = 1
        y_activator = 0

    elif direction == 1: #vertical
        x_activator = 0
        y_activator = 1

    elif direction == 2: #diagonal
        x_activator = 1
        y_activator = 1

    return x_activator, y_activator

def calculate_fits(puzzle, current_word):

    fit = 0

    for puzzle_y_position in sample(range(line_count), k = line_count): #loops through every position in the lines in random order
        for puzzle_x_position in sample(range(column_count), k = column_count): #loops through every position in the columns in random order
            for fit_direction in sample(range(3), k = 3):

                x_activator, y_activator = set_direction_parameters(fit_direction)


                temp_fit = 0
                if (puzzle_x_position + len(current_word)) * x_activator <= column_count and (puzzle_y_position + len(current_word)) * y_activator <= line_count: #Makes shure the temp Puzzle index doenst get out of range  to the right

                    for word_position in range(len(current_word)):

                        if puzzle[puzzle_y_position + (word_position * y_activator)][puzzle_x_position + (word_position * x_activator)] == current_word[word_position]: #increases temp fit, if the letter of word and puzzle match

                            temp_fit += 1

                        elif puzzle[puzzle_y_position + (word_position * y_activator)][puzzle_x_position + (word_position * x_activator)] != current_word[word_position] and puzzle[puzzle_y_position + (word_position * y_activator)][puzzle_x_position + (word_position * x_activator)] != "$": #if the ltter doesn match and the puzzle postion isnt empty ("$") this breaks the loop

                            temp_fit = -1
                            break

                    if temp_fit == len(current_word): #In case a word fits perfectly into another. Also in case a word fits perfectly into a combination of other (which is unlikely tho)

                            temp_fit = -1


                    elif temp_fit > fit: #defines position and direction if its the best fit so far. With > it takes the first fit, with >= it takes the last. A non fit has to be "-1" if this is >=. Otherwise the last position of a non fit will be written into the variables. This doesnt matter as long as a fit = 0 is overwritten in the end. But stil, temporary there would be wrong informations in the variables
                        #print(temp_fit, current_word)
                        fit = temp_fit
                        start_x_position = puzzle_x_position
                        start_y_position = puzzle_y_position
                        word_direction = fit_direction



    if fit == 0: #If there is no fit

        start_x_position = 0 #this is used for breaking out of the for loops

        for puzzle_y_position in sample(range(line_count), k = line_count): #loops through every position in the lines in random order
            for puzzle_x_position in sample(range(column_count), k = column_count): #loops through every position in the columns in random order
                for fit_direction in sample(range(3), k = 3): #loops through every direction in random order

                    x_activator, y_activator = set_direction_parameters(fit_direction)
                    if (puzzle_x_position + len(current_word)) * x_activator <= column_count and (puzzle_y_position + len(current_word)) * y_activator <= line_count: #Makes shure the temp Puzzle index doenst get out of range  to the right
                        for word_position in range(len(current_word)):
                            if puzzle[puzzle_y_position + (word_position * y_activator)][puzzle_x_position + (word_position * x_activator)] != current_word[word_position] and puzzle[puzzle_y_position + (word_position * y_activator)][puzzle_x_position + (word_position * x_activator)] != "$": #if the ltter doesn match and the puzzle postion isnt empty ("$") this breaks the loop
                                #the word doesnt fit in this position, breaks out of word loop
                                start_x_position = -1
                                start_y_position = -1
                                word_direction = -1
                                break

                        else:
                            #for is exceted without a break --> the word fits in this position
                            start_x_position = puzzle_x_position
                            start_y_position = puzzle_y_position
                            word_direction = fit_direction
                            break #breaks out of for direction loop, if a fitting position has been found
                if start_x_position > 0: #breaks out of for x loop, if a fitting position has been found
                    break
            if start_x_position > 0: #breaks out of for y loop, if a fitting position has been found
                break


    return start_x_position, start_y_position, word_direction


def write_puzzle(puzzle, current_word, start_x_position, start_y_position, word_direction):

    x_activator, y_activator = set_direction_parameters(word_direction)

    for word_position in range(len(current_word)): #Loops through position within the array

        puzzle[start_y_position + (word_position * y_activator)][start_x_position + (word_position * x_activator)] = current_word[word_position]


    return puzzle


def create_puzzle(words):
    # creates an array with "$" symbols to be the field and loops through the words being written
    puzzle = [["$" for x in range(column_count)] for y in range(line_count)] #Creates array filled with "$"

    for word_index in range(len(words)): #loops through every word in the words list

        if word_index == 0: #Special case for the first word which is written in a random position in a random direction on the board
            word_direction = randint(0,2) #Random direction
            start_x_position = randint(0, column_count-len(words[word_index])) #Random x position within the boundries
            start_y_position = randint(0, line_count-len(words[word_index])) #Random y position within the boundries
            puzzle = write_puzzle(puzzle, words[word_index], start_x_position, start_y_position, word_direction)


        else: #For every word after the first one
            start_x_position, start_y_position, word_direction = calculate_fits(puzzle, words[word_index])
            if start_x_position == -1: #means the word cant be fit
                print("The word " + words[word_index] + " could not be fit in the puzzle")

            else:
                puzzle = write_puzzle(puzzle, words[word_index], start_x_position, start_y_position, word_direction)




    return puzzle

words = word_input()
define_field_size()
puzzle = create_puzzle(words)
puzzle = fill_field_with_randoms(puzzle)
print_puzzle(puzzle)
