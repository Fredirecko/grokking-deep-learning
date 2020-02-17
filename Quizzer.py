#Quizzer is a program that is used to input question and answer pairs. The user is then quizzed on the inputs.
#The user uses paper and pencil to work out the problems.
#Once the user has answered the question they can reveal the answer and compare.
#They will be asked if there answer was sufficiently correct. If their answer was correct they will be given credit for the answer.
#At the end of the quiz they will be given a score and can see a list of the questions they answered correctly/incorrectly.


class Quizzer:
    """ Class for inputting questions and answer pairs for future quizzing. """

    print("Hello! Welcome to Quizzer!")

    question_bank = {}
    answer_bank = {}

    def newQuestionAnswer(self):
        """ Input question and answer pairs which are stored as a dictionary """

        self.question = ""
        self.answer = ""
        self.q = 1


        while True:
            print("")
            print("Enter question number " + str(self.q) + " below.")
            self.question = input()
            self.new_Q = {(self.q): self.question}

            print("")
            print("Enter answer for question " + str(self.q) + " below.")
            self.answer = input()
            self.new_A = {(self.q): self.answer}

            #updates dictionary with inputs
            self.question_bank.update(self.new_Q)
            self.answer_bank.update(self.new_A)
            self.q += 1

            y = self.anotherQuestion()

            if y:
                continue
            else:
                break

    def anotherQuestion(self):

        while True:
            print("")
            print("Enter 1 if you have another question to add. Enter 0 if you are done adding questions.")

            try:
                self.x = int(input())
            except ValueError:
                print("")
                print("Invalid option.")
                continue
            else:
                if self.x == 1:
                    return True
                elif self.x == 0:
                    print("")
                    print("Thank you")
                    return False
