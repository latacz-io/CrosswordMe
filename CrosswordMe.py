from random import randint
from random import sample

def print_puzzle(puzzle, line_count, column_count):
    #Prints the puzzle puzzle on a board
    for line in range(line_count):
        for position in range(column_count):
            print(str(puzzle[line][position]) + " ", end="") #Prints character in current position
        print() #Prints Newline

def word_input():
    #Collects the words for the puzzle
    words = ["one"] * 100
    #, "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    user_input = ""
    """while 1 == 1:
        user_input = input("Word: ")
        if user_input.lower() == "done":
            break
        words.append(user_input)"""
    return words

def calculate_field_size(words):
    line_count = len(words)
    column_count = 10
    return line_count, column_count

def create_puzzle(words, line_count, column_count):
    # creating the puzzle
    ## horizontals
    line_order = sample(range(line_count), line_count)
    puzzle = [["$" for x in range(column_count)] for y in range(line_count)] #Creates 10x10 array filled with "$"

    for word in range(len(words)): #loops through every word in the words list
        word_position = 0 #resets the word_position. this is needed beacuse word_position counts through the length of every word being written
        line = line_order[0] #TEMP
        if word == 0:
            start_position = randint(0, 10-len(words[word])) #int for start_position
            end_position = start_position+len(words[word]) #int for end_position

            for array_position in range(start_position, end_position): #Loops through position within the array

                puzzle[line][array_position] = words[word][word_position] #Writes the word at random position of the array
                word_position += 1 #Fake loop for the word position

        else:
            for array_position in range(column_count-len(words[word])+1):
                if puzzle[line][array_position:array_position+len(words[word])-1] == words[word]: #Bisher drin: Wenn das Wort komplett gleich ist. Es fehlt: Wenn das wort zum Teil gleich ist. Mit "in" lösen?
                     puzzle[line][array_position:array_position+len(words[word])-1] = words[word]





    return puzzle

words = word_input()
line_count, column_count = calculate_field_size(words)
puzzle = create_puzzle(words, line_count, column_count)
print_puzzle(puzzle, line_count, column_count)
