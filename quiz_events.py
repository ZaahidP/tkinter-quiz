import tkinter as tk


def question_1(question, btn1, btn2, btn3, btn4, feedback):
        question.configure(text="Question 1:  How many hours are in a day?")
        btn1.configure(text="24", command=lambda: q_correct(feedback))
        btn2.configure(text="10", command=lambda: q1_wrong(feedback))
        btn3.configure(text="25", command=lambda: q1_wrong(feedback))
        btn4.configure(text="16", command=lambda: q1_wrong(feedback))
        
        print("Q1 Selected")
        
       
def question_2(question, btn1, btn2, btn3, btn4, feedback):
        question.configure(text="Question 2: How many days are there in a week? ")
        btn1.configure(text="5", command=lambda: q2_wrong(feedback))
        btn2.configure(text="7", command=lambda: q_correct(feedback))
        btn3.configure(text="10", command=lambda: q2_wrong(feedback))
        btn4.configure(text="2", command=lambda: q2_wrong(feedback))
        print("Q2 Selected")

      

def question_3(question, btn1, btn2, btn3, btn4, feedback):
        question.configure(text="Question 3: How many days in the month of May")
        btn1.configure(text="30", command=lambda: q3_wrong(feedback))
        btn2.configure(text="31", command=lambda: q_correct(feedback))
        btn3.configure(text="28", command=lambda: q3_wrong(feedback))
        btn4.configure(text="32", command=lambda: q3_wrong(feedback))
        print("Q3 Selected")

     

def question_4(question, btn1, btn2, btn3, btn4, feedback):
        question.configure(text="Question 4: How many minutes in 10 hours")
        btn1.configure(text="6000", command=lambda: q4_wrong(feedback))
        btn2.configure(text="650", command=lambda: q4_wrong(feedback))
        btn3.configure(text="600", command=lambda: q_correct(feedback))
        btn4.configure(text="360", command=lambda: q4_wrong(feedback))
        print("Q4 Selected")


def q_correct(feedback):
        feedback.configure(text="Correct!")

def q1_wrong(feedback):
        feedback.configure(text="Incorrect sorry! The correct answer was 24!")

def q2_wrong(feedback):
        feedback.configure(text="Incorrect sorry! The correct answer was 7!")

def q3_wrong(feedback):
        feedback.configure(text="Incorrect sorry! The correct answer was 31!")

def q4_wrong(feedback):
        feedback.configure(text="Incorrect sorry! The correct answer was 600!")

