from random import randint

#input

words = ["one", "two", "three", "four", "five", "six"]
user_input = ""

"""while 1 == 1:
    user_input = input("Word: ")
    if user_input.lower() == "done":
        break
    words.append(user_input)"""

# creating the puzzle
## horizontals
line = randint(0,10)
lines_used = []
puzzle = [["$" for x in range(10)] for y in range(10)]
for word in range(0, len(words)):
    lines_used.append(line)
    word_position = 0
    #print(len(words[word]))
    start_position = randint(0, 10-len(words[word]))
    end_position = start_position+len(words[word])
    for array_position in range(start_position, end_position):
        puzzle[line][array_position] = words[word][word_position]
        word_position += 1
    line = randint(0,10)
    while line in lines_used:
        line = randint(0,10)
print(words)

#puzzle[2][1] = 1
#print(puzzle[2]) prints the entire second line
#Prints the puzzle
for line in range(10):
    for position in range(10):
        print(str(puzzle[line][position]) + " ", end="") #Prints character in current position
    print() #Prints Newline
