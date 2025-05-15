import tkinter as tk



class QuizLabels(tk.Label):
    def __init__(self, parent, label_text):
        super().__init__(parent)

        self.configure(text=label_text)
        
        self.grid(sticky="nsew", padx=10, pady=10)


class Option_Button(tk.Button):
    def __init__(self, parent, btn_text, action):
      super().__init__(parent)

      self.configure(text=btn_text,
                     command=action)

      self.grid(sticky="nsew")


class QuestionButtons(tk.Button):
    def __init__(self, parent, butn_text):
        super().__init__(parent)

        self.configure(text=butn_text)

        self.grid(sticky="nsew")

class VerticalFrame(tk.Frame):
    def __init__(self, parent, bag):
        super().__init__(parent)

        self.configure(bg=bag)
        self.grid(sticky="nsew")
        
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 2)
        self.columnconfigure(2, weight = 2)
        self.columnconfigure(3, weight = 1)
        
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 2)
        self.rowconfigure(2, weight = 2)
        self.rowconfigure(3, weight = 1)
                       
        



print("tester")
