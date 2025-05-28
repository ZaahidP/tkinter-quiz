import tkinter as tk
from quiz_widgets import QuizLabels, Option_Button, QuestionButtons, VerticalFrame, OptionFrames, EntryBox
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
        

        self.base_frames()            
#Frame for top

        self.create_widgets()

        # Frames
    def base_frames(self):
        #Option Frames
        self.frame1 = OptionFrames(self, "red")
        self.frame1.grid(row=0, column=0)

        self.frame2 = OptionFrames(self, "blue")
        self.frame2.grid(row=2, column=0)
        
        self.frame3 = OptionFrames(self, "yellow")
        self.frame3.grid(row=0, column=2)
        
        self.frame4 = OptionFrames(self, "green")
        self.frame4.grid(row=2, column=2)
        
        # Mid frames
        self.mid_frame = tk.Frame(self, bg="black")
        self.mid_frame.grid(row=1, column=0, columnspan=3, sticky="nsew")
        
        self.mid_frame.columnconfigure(0, weight = 1)

        self.mid_frame.rowconfigure(0, weight = 1)
        self.mid_frame.rowconfigure(1, weight = 1)

        self.border_mid = tk.Frame(self.mid_frame, bg="black")
        self.border_mid.grid(column=0, row=0, columnspan=3, sticky="nsew")

        self.mid_bot_frame = tk.Frame(self.mid_frame, bg="orange")
        self.mid_bot_frame.grid(column=0, row=1, columnspan=3, sticky="nsew",
                               padx=10, pady=10
                                                    )
        # Vertical Frames
        self.bottom_frame = VerticalFrame(self,"grey")
        self.bottom_frame.grid(row=2, column=1)

        self.top_frame = VerticalFrame(self, "grey")
        self.top_frame.grid(row=0, column=1)
        
        # Widgets
    def create_widgets(self):
      # Option buttons  
        self.btn1 = Option_Button(self.frame1, "Option 1",
                              self.option_one)
        self.btn1.grid(row=1, column=1)
        
        self.btn2 = Option_Button(self.frame2, "Option 3",
                                 self.option_one)
        self.btn2.grid(row=1, column=1)

        self.btn3 = Option_Button(self.frame3, "Option 2",
                                 self.option_one)
        self.btn3.grid(row=1, column=1)
        
        self.btn4 = Option_Button(self.frame4,"Option 4",
                                 self.option_one)
        self.btn4.grid(row=1, column=1)

        self.question = QuizLabels(self.mid_frame, "Select a question to begin!", "Arial")
        self.question.grid(column=0, row=0)

        self.feedback = QuizLabels(self.mid_frame, "Good luck!", "Arial")
        self.feedback.configure(bg="orange")
        self.feedback.grid(column=0, row=1)

        # Question buttons
        
        self.ques_1 = QuestionButtons(self.top_frame, "Question 1")
        self.ques_1.configure(command=lambda: question_1(self.question, self.btn1, self.btn2, self.btn3, self.btn4, self.feedback))
        self.ques_1.grid(column=1, row=1, sticky="nsew")

        self.ques_2 = QuestionButtons(self.top_frame, "Question 2")
        self.ques_2.configure(command=lambda: question_2(self.question, self.btn1, self.btn2, self.btn3, self.btn4, self.feedback))
        self.ques_2.grid(column=2, row=1, sticky="nsew")

        self.ques_3 = QuestionButtons(self.top_frame, "Question 3")
        self.ques_3.configure(command=lambda: question_3(self.question, self.btn1, self.btn2, self.btn3, self.btn4, self.feedback))
        self.ques_3.grid(column=1, row=2, sticky="nsew")

        self.ques_4 = QuestionButtons(self.top_frame, "Question 4")
        self.ques_4.configure(command=lambda: question_4(self.question, self.btn1, self.btn2, self.btn3, self.btn4, self.feedback))
        self.ques_4.grid(column=2, row=2, sticky="nsew")
    
    def option_one(self):
        print("No question selected")

    

root = quiz_grid()
root.mainloop()

