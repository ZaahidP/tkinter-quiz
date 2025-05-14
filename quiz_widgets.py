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
        



print("tester")
