import tkinter as tk
from quiz1_widgets import QuizLabels, Option_Button, QuestionButtons
from quiz_events import *

question_selected = 0

class quiz_grid(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz")
        self.geometry("900x700")


        # Root intialisation
        for i in range(3):
            self.columnconfigure(i, weight = 1)                 
            self.rowconfigure(i, weight = 1)

        self.create_frames()            
#Frame for top

        self.create_widgets()

        # Frames
    def create_frames(self):
        self.frame1 = tk.Frame(self, bg="red")
        self.frame1.grid(row=0, column=0, sticky="nsew",
                         padx=5, pady=5)
        for i in range(3):
            self.frame1.columnconfigure(i, weight = 1)
            self.frame1.rowconfigure(i, weight = 1)

        self.frame2 = tk.Frame(self, bg="blue")
        self.frame2.grid(row=2, column=0, sticky="nsew",
                         padx=5, pady=5)
        for i in range(3):
            self.frame2.columnconfigure(i, weight = 1)
            self.frame2.rowconfigure(i, weight = 1)

        self.frame3 = tk.Frame(self, bg="yellow")
        self.frame3.grid(row=0, column=2, sticky="nsew",
                         padx=5, pady=5)
        for i in range(3):
            self.frame3.columnconfigure(i, weight = 1)
            self.frame3.rowconfigure(i, weight = 1)

        self.frame4 = tk.Frame(self, bg="green")
        self.frame4.grid(row=2, column=2, sticky="nsew",
                         padx=5, pady=5)
        for i in range(3):
            self.frame4.columnconfigure(i, weight = 1)
            self.frame4.rowconfigure(i, weight = 1)

        self.mid_frame = tk.Frame(self, bg="black")
        self.mid_frame.grid(row=1, column=0, columnspan=3, sticky="nsew")
        
        self.mid_frame.columnconfigure(0, weight = 1)

        self.mid_frame.rowconfigure(0, weight = 1)
        self.mid_frame.rowconfigure(1, weight = 1)

        self.border_mid = tk.Frame(self.mid_frame, bg="black")
        self.border_mid.grid(column=0, row=0, columnspan=3, sticky="nsew")

        self.bottom_frame = tk.Frame(self.mid_frame, bg="orange")
        self.bottom_frame.grid(column=0, row=1, columnspan=3, sticky="nsew",
                               padx=10, pady=10
                                                    )
        self.bottom_frame = tk.Frame(self, bg="grey")
        self.bottom_frame.grid(row=2, column=1, sticky="nsew")

        for i in range(3):
            self.bottom_frame.columnconfigure(i, weight = 1)
            self.bottom_frame.rowconfigure(i, weight = 1)

        self.top_frame = tk.Frame(self, bg="grey")
        self.top_frame.grid(row=0, column=1, sticky="nsew")

        self.top_frame.columnconfigure(0, weight = 1)
        self.top_frame.columnconfigure(1, weight = 2)
        self.top_frame.columnconfigure(2, weight = 2)
        self.top_frame.columnconfigure(3, weight = 1)

        self.top_frame.rowconfigure(0, weight = 1)
        self.top_frame.rowconfigure(1, weight = 2)
        self.top_frame.rowconfigure(2, weight = 2)
        self.top_frame.rowconfigure(3, weight = 1)

        
        # Widgets
    def create_widgets(self):

        self.btn1 = Option_Button(self.frame1, "Option 1",
                              self.option_func)
        self.btn1.grid(row=1, column=1)
        
        self.btn2 = Option_Button(self.frame2, "Option 3",
                                 self.option_func)
        self.btn2.grid(row=1, column=1)

        self.btn3 = Option_Button(self.frame3, "Option 2",
                                 self.option_func)
        self.btn3.grid(row=1, column=1)
        
        self.btn4 = Option_Button(self.frame4,"Option 4",
                                 self.option_func)
        self.btn4.grid(row=1, column=1)

        self.question = QuizLabels(self.mid_frame, "Select a question to begin!")
        self.question.grid(column=0, row=0)

        self.feedback = QuizLabels(self.mid_frame, "Feedback")
        self.feedback.configure(bg="orange")
        self.feedback.grid(column=0, row=1)
        
        self.answer = tk.Button(self.bottom_frame, text="Submit")
        self.answer.grid(column=1, row=1, sticky="nsew")

        self.ques_1 = QuestionButtons(self.top_frame, "Question 1")
        self.ques_1.configure(command=lambda: question_1(self.question, self.btn1, self.btn2, self.btn3, self.btn4))
        self.ques_1.grid(column=1, row=1, sticky="nsew")

        self.ques_2 = QuestionButtons(self.top_frame, "Question 2")
        self.ques_2.configure(command=lambda: question_2(self.question, self.btn1, self.btn2, self.btn3, self.btn4))
        self.ques_2.grid(column=2, row=1, sticky="nsew")

        self.ques_3 = QuestionButtons(self.top_frame, "Question 3")
        self.ques_3.configure(command=lambda: question_3(self.question, self.btn1, self.btn2, self.btn3, self.btn4))
        self.ques_3.grid(column=1, row=2, sticky="nsew")

        self.ques_4 = QuestionButtons(self.top_frame, "Question 4")
        self.ques_4.configure(command=lambda: question_4(self.question, self.btn1, self.btn2, self.btn3, self.btn4))
        self.ques_4.grid(column=2, row=2, sticky="nsew")

    # Option button functionalities

    def option_func(self):
        options = ["one", "two", "three", "four"]
        for i in options:
            if i == question_selected:
                self.feedback.configure(text="bruh")
                print(i)
            else:
                print("didnt work")

     
        
       
    

 










root = quiz_grid()
root.mainloop()

