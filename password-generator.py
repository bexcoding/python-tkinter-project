"""
Title: Password Generator
Description: GUI version of a password generator
Last Updated: April 8, 2023
Developer: Alexander Beck
Email: beckhv2@gmail.com
Github: https://github.com/bexcoding
"""


import tkinter
import random
import string


FONT = ("Helvetica", 18, "bold")
COLOR1 = "#f7faff"
COLOR2 = "#011029"
COLOR3 = "#7ebecf"


class Password():
    """
    Description
    ----------
    Allows a user to generate a random password. The length and different
    types of characters can be chosen when the class is instantiated.

    Assumptions
    ----------
    There is no explicit type checking for this class so it is assumed that the
    password will be generated using the button in the Application class.
    """

    def __init__(self, pass_size, upper=False, lower=False, number=False, 
                symbol=False):
        self.pass_size = pass_size
        self.include_upper = upper
        self.include_lower = lower
        self.include_number = number
        self.include_symbol = symbol
        # these contain all of the options for all four character types
        self.uppers = list(string.ascii_uppercase)
        self.lowers = list(string.ascii_lowercase)
        self.nums = list(string.digits)
        self.symbols = list(string.punctuation)

    def check_inclusion(self):
        """
        Description
        ----------
        Checks which character types the user wants in their password.

        Return
        ----------
        Returns list of character types to include when making the password.
        These types are represented by the strings "u", "l", "n", and "s".
        """

        # if no character types were chosen, selects lowercase and number types
        if not (self.include_upper or self.include_lower or self.include_number 
                or self.include_symbol):
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
        """
        Description
        ----------
        Shuffles the given list and chooses a random character.

        Return
        ----------
        Returns a single, random string character from the list.

        Parameters
        ----------
        character_list: list
            List from which a character should be chosen.
        """

        random.shuffle(character_list)
        return random.choice(character_list)
    
    def create_password(self):
        """
        Description
        ----------
        Creates a random password using the inclusion criteria and the length
        that the user wants.

        Return
        ----------
        Returns a string of random characters.

        Assumptions
        ----------
        self.pass_size > 0
        """

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
        self.root.geometry("395x600")
        self.root.title("Random Password Generator")
        # sets and stores variables for slider and checkboxes
        self.slider_result = tkinter.IntVar()
        self.check_result_up = tkinter.IntVar()
        self.check_result_low= tkinter.IntVar()
        self.check_result_num = tkinter.IntVar()
        self.check_result_sym = tkinter.IntVar()

    def generate_password(self):
        """
        Description
        ----------
        Gets user choices from checkboxes and slider. Uses results to create a
        random password with the Password class. Puts the results in the results
        frame at bottom of the app.
        """

        # get current values of checkboxes
        u = self.check_result_up.get()
        l = self.check_result_low.get()
        n = self.check_result_num.get()
        s = self.check_result_sym.get()
        # switches values from 1 or 0 to boolean
        for x in [u, l, n, s]:
            if x == 1:
                x = True
            else:
                x = False
        self.random_password = Password(self.slider_result.get(), upper=u, 
                                        lower=l, number=n, 
                                        symbol=s).create_password()
        self.result = tkinter.Label(self.result_frame, 
                                    text=self.random_password,
                                    font=FONT, bg=COLOR1, fg=COLOR2, padx=5, 
                                    pady=5)
        self.result.pack(padx=5, pady=5)
        
    def create_widgets(self):
        """
        Description
        ----------
        Creates all of the widgets for the program.
        """

        # create slider
        self.slider_frame = tkinter.LabelFrame(self.root, bg=COLOR1, fg=COLOR2,
                                               padx=10, pady=10)
        self.slider_label = tkinter.Label(self.slider_frame, 
                                          text="Password Length:",
                                          font=FONT, bg=COLOR1, fg=COLOR2,
                                          padx=5, pady=5)
        self.slider = tkinter.Scale(self.slider_frame, from_=4, to=15, 
                                    orient="horizontal", 
                                    variable=self.slider_result,
                                    font=FONT, bg=COLOR1, fg=COLOR2)
        # create checkboxes
        self.inclusion_frame = tkinter.LabelFrame(self.root, bg=COLOR1, 
                                                  fg=COLOR2, padx=10, pady=10)
        self.inclusion_label = tkinter.Label(self.inclusion_frame, 
                                             text="Include these types:",
                                             font=FONT, bg=COLOR1, fg=COLOR2,
                                             padx=5, pady=5)
        self.upper_letter_check = tkinter.Checkbutton(self.inclusion_frame, 
                                            text="Uppercase Letters (A,B,C...)", 
                                            variable=self.check_result_up,
                                            font=FONT, bg=COLOR1, fg=COLOR2)
        self.lower_letter_check = tkinter.Checkbutton(self.inclusion_frame, 
                                            text="Lowercase Letters (a,b,c...)", 
                                            variable=self.check_result_low,
                                            font=FONT, bg=COLOR1, fg=COLOR2)
        self.number_check = tkinter.Checkbutton(self.inclusion_frame, 
                                                text="Numbers (0,1,2...)", 
                                                variable=self.check_result_num,
                                                font=FONT, bg=COLOR1, fg=COLOR2)
        self.symbol_check = tkinter.Checkbutton(self.inclusion_frame, 
                                                text="Symbols (!,?,+...)", 
                                                variable=self.check_result_sym,
                                                font=FONT, bg=COLOR1, fg=COLOR2)
        # create button
        self.button_frame = tkinter.LabelFrame(self.root, bg=COLOR1, fg=COLOR2,
                                               padx=10, pady=10)
        self.button = tkinter.Button(self.button_frame, text="Create Password", 
                                     command=self.generate_password,
                                     font=FONT, bg=COLOR3, fg=COLOR2, padx=5, 
                                     pady=5)
        # create area for results
        self.result_frame = tkinter.LabelFrame(self.root, bg=COLOR1, fg=COLOR2)
        
    def display_widgets(self):
        """
        Description
        ----------
        Shows all of the created widgets.
        """

        # show slider
        self.slider_frame.grid(row=0, sticky="we")
        self.slider_label.pack()
        self.slider.pack()
        # show checkboxes
        self.inclusion_frame.grid(row=1, sticky="we")
        self.inclusion_label.grid(row=0)
        self.upper_letter_check.grid(row=1, sticky="w")
        self.lower_letter_check.grid(row=2, sticky="w")
        self.number_check.grid(row=3, sticky="w")
        self.symbol_check.grid(row=4, sticky="w")
        # show button
        self.button_frame.grid(row=2, sticky="we")
        self.button.pack()
        # show result
        self.result_frame.grid(row=3, sticky="we")
        
        
if __name__ == "__main__":
    app = Application()
    app.create_widgets()
    app.display_widgets()
    app.root.mainloop()