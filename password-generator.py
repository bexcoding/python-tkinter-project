"""
Title: Password Generator
Description: GUI version of a password generator
Last Updated: April 6, 2023
Developer: Alexander Beck
Email: beckhv2@gmail.com
Github: https://github.com/bexcoding
"""


import tkinter
import random
import string


class Password():
    def __init__(self, pass_size, upper=False, lower=False, number=False, symbol=False):
        self.pass_size = pass_size
        self.include_upper = upper
        self.include_lower = lower
        self.include_number = number
        self.include_symbol = symbol
        self.uppers = list(string.ascii_uppercase)
        self.lowers = list(string.ascii_lowercase)
        self.nums = list(string.digits)
        self.symbols = list(string.punctuation)
    def check_inclusion(self):
        if not (self.include_upper or self.include_lower or self.include_number or self.include_symbol):
            self.include_lower = True
            self.include_number = True
        character_types = []
        if self.include_upper:
            character_types.append("u")
        if self.include_lower:
            character_types.append("l")
        if self.include_number:
            character_types.append("n")
        if self.include_symbol:
            character_types.append("s")
        return character_types
    def choose_character(self, character_list):
        random.shuffle(character_list)
        return random.choice(character_list)
    def create_password(self):
        character_types = self.check_inclusion()
        new_password = []
        current_list_index = 0
        while self.pass_size > 0:
            current_list = character_types[current_list_index]
            if current_list == "u":
                random_character = self.choose_character(self.uppers)
            elif current_list == "l":
                random_character = self.choose_character(self.lowers)
            elif current_list == "n":
                random_character = self.choose_character(self.nums)
            elif current_list == "s":
                random_character = self.choose_character(self.symbols)
            new_password.append(random_character)
            current_list_index += 1
            if current_list_index >= len(character_types):
                current_list_index = 0
            self.pass_size -= 1
        random.shuffle(new_password)
        return "".join(new_password)


class Application():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("400x400")
        self.root.title("Random Password Generator")
    def generate_password(self):
        # need to pull information from slider and checkboxes
        self.random_password = Password(10, upper=True, lower=True, number=True, symbol=True).create_password()
        self.result = tkinter.Label(self.result_frame, text=self.random_password)
        self.result.grid()
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
        self.button = tkinter.Button(self.button_frame, text="Create Password", command=self.generate_password)
    def create_result_frame(self):
        self.result_frame = tkinter.LabelFrame(self.root)
        
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