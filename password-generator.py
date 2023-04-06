"""
Title: Password Generator
Description: GUI version of a password generator
Last Updated: April 5, 2023
Developer: Alexander Beck
Email: beckhv2@gmail.com
Github: https://github.com/bexcoding
"""


import tkinter


class Password():
    def __init__(self, pass_size, upper=False, lower=False, number=False, symbol=False):
        self.pass_size = pass_size
        self.include_upper = upper
        self.include_lower = lower
        self.include_number = number
        self.include_symbol = symbol



class Application():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("400x400")
        self.root.title("Random Password Generator")
    def create_slider_frame(self):
        self.slider_frame = tkinter.LabelFrame(self.root)
        self.slider_label = tkinter.Label(self.slider_frame, text="Password Length:")
        self.slider = tkinter.Scale(self.slider_frame, from_=4, to=15, orient="horizontal")
    def create_inclusion_frame(self):
        self.inclusion_frame = tkinter.LabelFrame(self.root)
        self.inclusion_label = tkinter.Label(self.inclusion_frame, text="Include these types:")
        self.upper_letter_check = tkinter.Checkbutton(self.inclusion_frame, text="Uppercase Letters (A,B,C...)")
        self.lower_letter_check = tkinter.Checkbutton(self.inclusion_frame, text="Lowercase Letters (a,b,c...)")
        self.number_check = tkinter.Checkbutton(self.inclusion_frame, text="Numbers (0,1,2...)")
        self.symbol_check = tkinter.Checkbutton(self.inclusion_frame, text="Symbols (!,?,+...)")
    def create_button_frame(self):
        self.button_frame = tkinter.LabelFrame(self.root)
        self.button = tkinter.Button(self.button_frame, text="Create Password")
    def create_result_frame(self):
        self.result_frame = tkinter.LabelFrame(self.root)
        self.result = tkinter.Label(self.result_frame, text="V*34Hho!")
    def display_slider(self):
        self.slider_frame.grid(row=0)
        self.slider_label.grid(column=0, row=0)
        self.slider.grid(column=0, row=1)
    def display_checkboxes(self):
        self.inclusion_frame.grid(row=1)
        self.inclusion_label.grid(row=0)
        self.upper_letter_check.grid(row=1, sticky="w")
        self.lower_letter_check.grid(row=2, sticky="w")
        self.number_check.grid(row=3, sticky="w")
        self.symbol_check.grid(row=4, sticky="w")
    def display_button(self):
        self.button_frame.grid(row=2)
        self.button.grid()
    def display_result(self):
        self.result_frame.grid(row=3)
        self.result.grid()
    def run_program(self):
        self.root.mainloop()
        
if __name__ == "__main__":
    app = Application()

    app.create_slider_frame()
    app.display_slider()

    app.create_inclusion_frame()
    app.display_checkboxes()

    app.create_button_frame()
    app.display_button()

    app.create_result_frame()
    app.display_result()

    app.run_program()