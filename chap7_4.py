numbers = [7, 10, 12, 21]


while True:
    answer = input("Guess the hidden number or type q to quit: ")
    if answer == 'q':
        break
    answer = int(answer)
    if answer in numbers:
        print("Correct!")
    else:
        print("Wrong")


numbers = [11, 32, 33, 15, 1]

while True:
    answer = input("Guess a number or type q to quit.")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("please type a number or q to quit.")
    if answer in numbers:
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly!")
