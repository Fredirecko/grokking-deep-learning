#Quizzer is a program that is used to input question and answer pairs. The user is then quizzed on the inputs.
#The user uses paper and pencil to work out the problems.
#Once the user has answered the question they can reveal the answer and compare.
#They will be asked if there answer was sufficiently correct. If their answer was correct they will be given credit for the answer.
#At the end of the quiz they will be given a score and can see a list of the questions they answered correctly/incorrectly.



class Quizzer:
    """ Class for inputting questions and answer pairs for future quizzing. """

    question_bank = {}
    answer_bank = {}

    def newQuiz(self):
        """ Create a new quiz. Input question and answer pairs which are stored as a dictionary """

        self.first_name = "None"
        self.last_name = "None"
        self.quiz_name = "Untitled"
        self.description = "No description provided."
        self.question = ""
        self.answer = ""
        self.q = 1

        print("")
        print("-----New Quiz------")
        print("")
        print("Enter your first name: ")
        self.first_name = input()
        print("")
        print("Enter your last name: ")
        self.last_name = input()
        print("")
        print("Enter quiz title: ")
        self.quiz_name = input()
        print("")
        print("Enter quiz description: ")
        self.description = input()

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

            self.y = self.anotherQuestion()

            if self.y:
                continue
            else:
                break

    def anotherQuestion(self):

        while True:
            print("----------------------------------------------")
            print( "Enter 1 if you have another question to add.")
            print(  "Enter 0 if you are done adding questions.")
            print("----------------------------------------------")
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
                    return False

    def startQuiz(self):

        print("Quiz Name: " + self.quiz_name)
        print("Description: " + self.description)
        print("Name: " + self.first_name + " " + self.last_name)
        print("")

        for i in self.question_bank:
            print("Problem: " + self.question_bank[i])
            print("")
            print("Enter 1 to show answer")
            proceed = int(input())
            if proceed == 1:
                for j in self.answer_bank:
                    print("")
                    print("Answer: " + self.answer_bank[j])

    def saveQuiz(self):
        pass

    def loadQuiz(self):
        pass

    def score(self):
        pass

    def listQA(self):
        pass

    def quitQuizzer(self):
        pass

class Start(Quizzer):
    """ Class for menu items and methods. """

    def mainMenu(self):
        print("*************************************")
        print("        Welcome to Quizzer!          ")
        print("*************************************")
        print("")

        while True:
            print("")
            print("------------- MAIN MENU -------------")
            print("")
            print("      Enter 1 to create new quiz     ")#new quiz will ask for name, quiz name, quiz description
            print("      Enter 2 to begin quiz          ") #start quiz
            print("")
            print("      Enter 3 to load quiz           ") #load file with saved quiz from txt file
            print("      Enter 4 to save current quiz   ") #save quiz to txt file
            print("      Enter 5 to exit                ") # exit program
            print("")
            print("-------------------------------------")
            try:
                self.selection = int(input())
            except ValueError:
                print("")
                print("Invalid option. Please try again.")
                continue
            if self.selection == 1:
                self.newQuiz()
            elif self.selection == 2:
                self.startQuiz()
            elif self.selection == 3:
                print("success")
            elif self.selection == 4:
                print("success")
            elif self.selection == 5:
                break


#---------------Main Program------------------------------------

edward = Start()
edward.mainMenu()
