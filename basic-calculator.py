"""
Title: Basic Calculator
Description: Uses tkinter module to make calculator GUI
Last Updated: April 5, 2023
Developer: Alexander Beck
Email: beckhv2@gmail.com
Github: https://github.com/bexcoding
"""


import tkinter


def main():
    root = tkinter.Tk()
    root.title("Basic Calculator")
    # create functions for calculator
    def click_button(number):
        current_length = len(entry_area.get())
        entry_area.insert(current_length, number)
    def clear_entry():
        current_length = len(entry_area.get())
        entry_area.delete(0, current_length)
    # create entry area
    entry_area = tkinter.Entry(root, width=50, borderwidth=5)
    # create number buttons
    number0 = tkinter.Button(root, text="0", command=lambda: click_button(0), padx=40, pady=20)
    number1 = tkinter.Button(root, text="1", command=lambda: click_button(1), padx=40, pady=20)
    number2 = tkinter.Button(root, text="2", command=lambda: click_button(2), padx=40, pady=20)
    number3 = tkinter.Button(root, text="3", command=lambda: click_button(3), padx=40, pady=20)
    number4 = tkinter.Button(root, text="4", command=lambda: click_button(4), padx=40, pady=20)
    number5 = tkinter.Button(root, text="5", command=lambda: click_button(5), padx=40, pady=20)
    number6 = tkinter.Button(root, text="6", command=lambda: click_button(6), padx=40, pady=20)
    number7 = tkinter.Button(root, text="7", command=lambda: click_button(7), padx=40, pady=20)
    number8 = tkinter.Button(root, text="8", command=lambda: click_button(8), padx=40, pady=20)
    number9 = tkinter.Button(root, text="9", command=lambda: click_button(9), padx=40, pady=20)
    # create special buttons
    add_button = tkinter.Button(root, text="+", padx=40, pady=20, bg="yellow")
    minus_button = tkinter.Button(root, text="-", padx=40, pady=20, bg="yellow")
    mult_button = tkinter.Button(root, text="*", padx=40, pady=20, bg="yellow")
    div_button = tkinter.Button(root, text="/", padx=40, pady=20, bg="yellow")
    decimal_button = tkinter.Button(root, text=".", padx=40, pady=20, bg="yellow")
    negative_button = tkinter.Button(root, text="(-)", padx=33, pady=20, bg="yellow")
    clear_button = tkinter.Button(root, text="clear", command=clear_entry, padx=25, pady=48, bg="red")
    equals_button = tkinter.Button(root, text="Enter", padx=26, pady=48, bg="green")

    # position entry area
    entry_area.grid(column=0, row=0, columnspan=5, padx=5, pady=5)
    # position number buttons
    number0.grid(column=0, row=1)
    number1.grid(column=1, row=1)
    number2.grid(column=2, row=1)
    number3.grid(column=3, row=1)
    number4.grid(column=4, row=1)
    number5.grid(column=0, row=2)
    number6.grid(column=1, row=2)
    number7.grid(column=2, row=2)
    number8.grid(column=3, row=2)
    number9.grid(column=4, row=2)
    # position special buttons
    add_button.grid(column=0, row=3)
    minus_button.grid(column=1, row=3)
    mult_button.grid(column=0, row=4)
    div_button.grid(column=1, row=4)
    clear_button.grid(column=3, row=3, rowspan=2)
    equals_button.grid(column=4, row=3, rowspan=2)
    decimal_button.grid(column=2, row=3)
    negative_button.grid(column=2, row=4)
    # run program loop
    root.mainloop()





if __name__ == "__main__":
    main()
