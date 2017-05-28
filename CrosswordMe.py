#input

words = []
user_input = ""

while 1 == 1:
    user_input = input("Word: ")
    if user_input.lower() == "done":
        break
    words.append(user_input)

# creating the puzzle

puzzle = [[[0 for x in range(10)] for y in range(10)] ]


print(puzzle)
