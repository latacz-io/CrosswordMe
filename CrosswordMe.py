#Fill in the words in line 32 you want to be set
#Comment out fill_field_with_randoms call in the end to see where your words are being set (will be at a different postion the next time, since a new puzzle will be generated)

from random import sample, choice
from string import ascii_letters
from enum import Enum
from itertools import product


class directions(Enum):
    HORIZONTAL = 0
    VERTICAL = 15
    DIAGONAL = 25


def print_puzzle(puzzle):
    #Prints the puzzle puzzle on a board
    for puzzle_y_position, puzzle_x_position in product(range(LINE_COUNT), range(COLUMN_COUNT)):
        print(
            str(puzzle[puzzle_y_position][puzzle_x_position]).upper(),
            end=" ")  #Prints character in current position
        if puzzle_x_position + 1 == COLUMN_COUNT: #Time for a new line
            print()  #Prints Newline


def fill_field_with_randoms(puzzle):
    #Fills the rest of the free space (represented by " ") with random letters

    for puzzle_y_position, puzzle_x_position in product(range(LINE_COUNT), range(COLUMN_COUNT)):

        if puzzle[puzzle_y_position][
                puzzle_x_position] == " ":  #If the position is empty
            puzzle[puzzle_y_position][puzzle_x_position] = choice(
                ascii_letters)

    return puzzle


def word_input():
    #Collects the words for the puzzle.
    #Sorts the words by length descedning. Therefore the longes word is set first
    #Gets messed up if a contain something else than ascii

    words = [
        "looooooooooooooooooooooooooooooooong", "EuropythonAAAAAAAAAAAAAAAAAAAA", "Rimini",
        "Bologna", "looooooooooooooooooooooooooooooooxxong", "Amore", "coala",
        "Beach", "Sea", "Umbrellas", "Hamburg"
    ]
    for word in reversed(words):
        if len(word) > LINE_COUNT:
            print(word + " has " + str(len(
                word)) + " letters. A maximum length of " + str(LINE_COUNT) +
                  " Letters is possible. " + word + " has been ommitted")
            words.remove(word)


    words.sort(key=len, reverse=True)

    return words


def define_field_size():
    #defines field size
    global LINE_COUNT
    LINE_COUNT = 12
    global COLUMN_COUNT
    COLUMN_COUNT = LINE_COUNT


def set_direction_parameters(direction):
    #Takes the direction and returns the parameters so the loops only trigger the right direction

    if direction == directions.HORIZONTAL:  #horizontal
        x_activator = 1
        y_activator = 0

    elif direction == directions.VERTICAL:  #vertical
        x_activator = 0
        y_activator = 1

    elif direction == directions.DIAGONAL:  #diagonal
        x_activator = 1
        y_activator = 1



    return x_activator, y_activator


def word_fits_in_range(current_word, puzzle_x_position, x_activator,
                       puzzle_y_position, y_activator):
    #Checks if the word exceeds the range for the current position. Returns true if it fits. Returns false Otherwise
    if (puzzle_x_position + len(current_word)
        ) * x_activator <= COLUMN_COUNT and (
            puzzle_y_position + len(current_word)) * y_activator <= LINE_COUNT:
        return True
    else:
        return False


def word_matches_position(puzzle, current_word, word_position,
                          puzzle_x_position, x_activator, puzzle_y_position,
                          y_activator):
    #Checks if the letter of the current word matches the letter on the board
    if puzzle[puzzle_y_position + (word_position * y_activator)][
            puzzle_x_position + (word_position * x_activator)] == current_word[
                word_position]:
        return True
    else:
        return False


def puzzle_position_is_empty(puzzle, word_position, puzzle_x_position,
                             x_activator, puzzle_y_position, y_activator):
    #Checks if the current position on the board is empty
    if puzzle[puzzle_y_position + (word_position * y_activator)][
            puzzle_x_position + (word_position * x_activator)] == " ":
        return True
    else:
        return False


def find_random_position(puzzle, current_word):
    #Finds a random position and direction for a word and returns the coordinates and the direction. Returns -1 for all three if the word cant be fit into the current puzzle
    start_x_position = 0  #Set the variable to zero so it can be checked for the break of the for loops later

    for puzzle_y_position, puzzle_x_position, fit_direction in product( sample( range(LINE_COUNT), k=LINE_COUNT), sample(
            range(COLUMN_COUNT), k=COLUMN_COUNT), sample(list(directions), k = 3)):  #loops through every position in the lines in random order

        x_activator, y_activator = set_direction_parameters(
            fit_direction)
        if word_fits_in_range(current_word, puzzle_x_position,
                              x_activator, puzzle_y_position,
                              y_activator):
            for word_position in range(len(current_word)):
                if not word_matches_position(
                        puzzle, current_word, word_position,
                        puzzle_x_position, x_activator,
                        puzzle_y_position,
                        y_activator) and not puzzle_position_is_empty(
                            puzzle, word_position, puzzle_x_position,
                            x_activator, puzzle_y_position,
                            y_activator):
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
                break  #breaks out of for direction loop, if a fitting position has been found

    return start_x_position, start_y_position, word_direction


def find_best_fit(puzzle, current_word):
    #Finds the best fit in the current puzzle for the word and returns the postion and direction
    #The function checks the postion and directions in random order. The first Highscore wins.
    #The funtion return a random position is no overlap fits can be found
    fit = 0

    for puzzle_y_position in sample(
            range(LINE_COUNT), k=LINE_COUNT
    ):  #loops through every position in the lines in random order
        for puzzle_x_position in sample(
                range(COLUMN_COUNT), k=COLUMN_COUNT
        ):  #loops through every position in the columns in random order
            for fit_direction in directions:

                x_activator, y_activator = set_direction_parameters(
                    fit_direction)

                temp_fit = 0
                if word_fits_in_range(current_word, puzzle_x_position,
                                      x_activator, puzzle_y_position,
                                      y_activator):

                    for word_position in range(len(current_word)):

                        if word_matches_position(
                                puzzle, current_word, word_position,
                                puzzle_x_position, x_activator,
                                puzzle_y_position, y_activator):

                            temp_fit += 1

                        else:
                            #if the letter doesn match and the puzzle postion
                            if not puzzle_position_is_empty(
                                    puzzle, word_position, puzzle_x_position,
                                    x_activator, puzzle_y_position,
                                    y_activator):
                                # if the postion is not empty
                                temp_fit = -1  #Immitates a False
                                break  #Breaks out of the for loop (--> Stops checking the current_word)

                    if temp_fit == len(
                            current_word
                    ):  #In case a word fits perfectly into another. Also in case a word fits perfectly into a combination of other (which is unlikely tho)

                        temp_fit = -1

                    elif temp_fit > fit:  #defines position and direction if its the best fit so far. With > it takes the first fit, with >= it takes the last. A non fit has to be "-1" if this is >=. Otherwise the last position of a non fit will be written into the variables. This doesnt matter as long as a fit = 0 is overwritten in the end. But stil, temporary there would be wrong informations in the variables

                        fit = temp_fit
                        start_x_position = puzzle_x_position
                        start_y_position = puzzle_y_position
                        word_direction = fit_direction


    if fit == 0:  #Set the first word
        start_x_position, start_y_position, word_direction = find_random_position(
            puzzle, current_word)

    return start_x_position, start_y_position, word_direction


def write_word(puzzle, current_word, start_x_position, start_y_position,
               word_direction):
    #Writes the current_word in the puzzle
    x_activator, y_activator = set_direction_parameters(word_direction)

    for word_position in range(len(
            current_word)):  #Loops through position within the array

        puzzle[start_y_position + (word_position * y_activator)][
            start_x_position + (word_position * x_activator)] = current_word[
                word_position]

    return puzzle


def create_puzzle(words):
    # creates an array with " " symbols to be the field and loops through the words being written
    puzzle = [[" " for x in range(COLUMN_COUNT)]
              for y in range(LINE_COUNT)]  #Creates array filled with " "

    for word_index in range(len(
            words)):  #loops through every word in the words list

        if word_index == 0:  #Set the first word
            start_x_position, start_y_position, word_direction = find_random_position(
                puzzle, words[word_index])
            word_direction = directions.HORIZONTAL
            start_y_position = 3
            start_x_position = 2
            puzzle = write_word(puzzle, words[word_index], start_x_position,
                                start_y_position, word_direction)

        else:  #For every word after the first one
            start_x_position, start_y_position, word_direction = find_best_fit(
                puzzle, words[word_index])
            if start_x_position == -1:  #means the word cant be fit
                print("The word " + words[word_index] +
                      " could not be fit in the puzzle")

            else:  #A fit has beeen found
                puzzle = write_word(puzzle, words[word_index],
                                    start_x_position, start_y_position,
                                    word_direction)

    return puzzle


define_field_size()
words = word_input()
puzzle = create_puzzle(words)
print_puzzle(puzzle)

fill_choice = ""
while fill_choice != "Y" and fill_choice != "N":

    fill_choice = input("Do you want to fill the puzzle with randoms? (Y/N)")
    fill_choice = fill_choice.upper()
    if fill_choice == "Y":

        puzzle = fill_field_with_randoms(puzzle)
        print_puzzle(puzzle)
    elif fill_choice == "N":
        break
    else:
        print("Input not valid")
