#A program to quiz me on chapter four material

print("Welcome to the Grokking Deep Learning Book chapter four quiz.")
print("")
print("Enter 1 to begin.")

for retry in range(5):
    begin = int(input())
    if begin == 1:
        print("")
        print("Great! Let's begin.")
        break
    else:
        print("")
        print("Enter 1 when you are ready.")
else:
    print("")
    print("I guess you are not ready. Please try again later.")
    quit()

print("")
print("Problem One:")
print("Is error always positive or negative?")
print("")

for retry in range(5):
    answer = input()
    if answer == "positive":
        print("")
        print("Correct. Let's continue.")
        break
    else:
        print("")
        print("Incorrect. Try again")
else:
    print("")
    print("Study harder and try again!")
    quit()

print("")
print("Problem Two:")
print("Write a simple program that has variables: weight, input, and goal_pred. Make a prediction and use mean squared error to make the error positive and print the error.")
print("")

answer = input()

cor_answer = "weight, input, goal_pred = (0.5, 0.5, 0.8) \n pred = input * knob_weight \n error = (pred - goal_pred) ** 2 \n print(error)"
print("")
print(cor_answer)

print("")
print("Problem Three:")
print("Which line of code from the above example forces the error to be positive? \n How is this achieved? \n Write your answer down on a sheet of paper and compare the answer to the one below.")
print("")
print("Press 1 to compare answers")
