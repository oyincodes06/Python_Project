# A quiz program containing multiple choice questions and options and with correct answers assigned below
# import all the questions from the questions.py file
from questions import questions
class Quiz:
    def __init__(self):
        #List of all the questions, answers and options
        self.questions = questions
        # initial_score is 0
        self.scores = 0
        
    # main quiz program
    def run_quiz(self):
        print("Welcome to Quiz")
        print("You're to answer each questions which the number of each answers")
        
        #looping through all the questions and answers and options
        for i, q in enumerate(self.questions):
            print(f"\nQuestions{i+1}: {q['question']}")
            print("Options Are: ")
            for option in q['options']:
                print(f"\n{option}")
            
            # getting userss answers
            answer= input("\nAnswer: ")
            
            # checking if answers is correct
            if answer == q['answers']:
                print("\nCorrect")
                self.scores +=1
                print(f"You won ${self.scores}, Score = {self.scores}")
            else:
                print("Wrong Answer")
                self.scores +=0
                print(f"No Score")
                
        # the function below to calculate the result
        self.show_result()  
        
    # displaying results after the quiz ended
    def show_result(self):
        print("\nQuiz Complete")
        print(f"Your final Score is {self.scores}/{len(self.questions)}")
        
        # checking the person grade for each user
        if self.scores >= len(self.questions) * 0.75:
            print("Congratulations you passed the quiz")
        else:
            print("Better luck next time! You failed the quiz.You did not get all the questions")
        

#running the quiz 
quiz = Quiz()
quiz.run_quiz()