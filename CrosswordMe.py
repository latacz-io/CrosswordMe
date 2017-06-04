from random import randint
from random import sample

def print_puzzle():
    #Prints the puzzle puzzle on a board
    for line in range(line_count):
        for position in range(column_count):
            print(str(puzzle[line][position]) + " ", end="") #Prints character in current position
        print() #Prints Newline

def word_input():
    #Collects the words for the puzzle
    global words
    words = ["YEAHAA"] * 5
    #, "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    user_input = ""
    """while 1 == 1:
        user_input = input("Word: ")
        if user_input.lower() == "done":
            break
        words.append(user_input)"""
    return words

def calculate_field_size():
    global line_count
    line_count = 12
    global column_count
    column_count = 12
    return line_count, column_count

def write_horizontal(word):
    if word >= 0:
        start_position = randint(0, column_count-len(words[word])) #int for start_position
        end_position = start_position+len(words[word]) #int for end_position
        line = randint(0, line_count-1)
        word_position = 0 #resets the word_position. this is needed beacuse word_position counts through the length of every word being written
        for array_position in range(start_position, end_position): #Loops through position within the array

            puzzle[line][array_position] = words[word][word_position] #Writes the word at random position of the array
            word_position += 1 #Fake loop for the word position

def write_vertical(word):
    if word >= 0:
        start_position = randint(0, line_count-len(words[word])) #int for start_position
        end_position = start_position+len(words[word]) #int for end_position
        column = randint(0, column_count-1)
        word_position = 0 #resets the word_position. this is needed beacuse word_position counts through the length of every word being written
        for array_position in range(start_position, end_position): #Loops through position within the array

            puzzle[array_position][column] = words[word][word_position] #Writes the word at random position of the array
            word_position += 1 #Fake loop for the word position

def write_diagonal(word):
    if word >= 0:
        start_x_position = randint(0, column_count-len(words[word])) #int for start_position
        start_y_position = randint(0, line_count-len(words[word])) #int for start_position
        end_x_position = start_x_position+len(words[word]) #int for end_position
        end_y_position = start_y_position+len(words[word]) #int for end_position
        word_position = 0 #resets the word_position. this is needed beacuse word_position counts through the length of every word being written
        for x_position, y_position in zip(range(start_x_position, end_x_position), range(start_y_position, end_y_position)): #Loops through position within the array

            puzzle[y_position][x_position] = words[word][word_position] #Writes the word at random position of the array
            word_position += 1 #Fake loop for the word position

def create_puzzle():
    # creating the puzzle
    global puzzle
    puzzle = [["$" for x in range(column_count)] for y in range(line_count)] #Creates array filled with "$"

    for word in range(len(words)): #loops through every word in the words list




        word_direction = randint(0,2)
        if word_direction == 0:
            write_horizontal(word)
        elif word_direction == 1:
            write_vertical(word)
        elif word_direction == 2:
            write_diagonal(word)










    return puzzle

words = word_input()
line_count, column_count = calculate_field_size()
puzzle = create_puzzle()
print_puzzle()
