"""
Title: Password Generator
Description: GUI version of a password generator
Last Updated: April 7, 2023
Developer: Alexander Beck
Email: beckhv2@gmail.com
Github: https://github.com/bexcoding
"""


import tkinter
import random
import string


class Password():
    """
    Description
    ----------
    Allows a user to generate a random password. The length and different
    types of characters can be chosen when the class is instantiated.

    Assumptions
    ----------
    There is no explicit type checking for this class so it is assumed that the
    password will be generated using the Application class button.
    """

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
    """
    Description
    ----------
    Create a tkinter window with several widgets. The included button uses
    the Password class to generate a random password.
    """
    
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("400x400")
        self.root.title("Random Password Generator")
        self.slider_result = tkinter.IntVar()
        self.check_result_up = tkinter.IntVar()
        self.check_result_low= tkinter.IntVar()
        self.check_result_num = tkinter.IntVar()
        self.check_result_sym = tkinter.IntVar()
    def generate_password(self):
        u = self.check_result_up.get()
        l = self.check_result_low.get()
        n = self.check_result_num.get()
        s = self.check_result_sym.get()        
        for x in [u, l, n, s]:
            if x == 1:
                x = True
        self.random_password = Password(self.slider_result.get(), upper=u, lower=l, number=n, symbol=s).create_password()
        self.result = tkinter.Label(self.result_frame, text=self.random_password)
        self.result.grid()
    def create_widgets(self):
        self.slider_frame = tkinter.LabelFrame(self.root)
        self.slider_label = tkinter.Label(self.slider_frame, text="Password Length:")
        self.slider = tkinter.Scale(self.slider_frame, from_=4, to=15, orient="horizontal", variable=self.slider_result)

        self.inclusion_frame = tkinter.LabelFrame(self.root)
        self.inclusion_label = tkinter.Label(self.inclusion_frame, text="Include these types:")
        self.upper_letter_check = tkinter.Checkbutton(self.inclusion_frame, text="Uppercase Letters (A,B,C...)", variable=self.check_result_up)
        self.lower_letter_check = tkinter.Checkbutton(self.inclusion_frame, text="Lowercase Letters (a,b,c...)", variable=self.check_result_low)
        self.number_check = tkinter.Checkbutton(self.inclusion_frame, text="Numbers (0,1,2...)", variable=self.check_result_num)
        self.symbol_check = tkinter.Checkbutton(self.inclusion_frame, text="Symbols (!,?,+...)", variable=self.check_result_sym)

        self.button_frame = tkinter.LabelFrame(self.root)
        self.button = tkinter.Button(self.button_frame, text="Create Password", command=self.generate_password)

        self.result_frame = tkinter.LabelFrame(self.root)
        
    def display_widgets(self):
        self.slider_frame.grid(row=0)
        self.slider_label.grid(column=0, row=0)
        self.slider.grid(column=0, row=1)

        self.inclusion_frame.grid(row=1)
        self.inclusion_label.grid(row=0)
        self.upper_letter_check.grid(row=1, sticky="w")
        self.lower_letter_check.grid(row=2, sticky="w")
        self.number_check.grid(row=3, sticky="w")
        self.symbol_check.grid(row=4, sticky="w")

        self.button_frame.grid(row=2)
        self.button.grid()

        self.result_frame.grid(row=3)
        
        
if __name__ == "__main__":
    app = Application()
    app.create_widgets()
    app.display_widgets()
    app.root.mainloop()