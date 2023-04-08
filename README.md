# Tkinter Project

This project is focused around the use of the `tkinter` module in python that is used to make GUIs with Python code. This is my first attempt to learn GUI creation with Python. 

# Basic Calculator

My basic calculator is my first `tkinter` project that took some time to write up and get to look the way that I want. It is similar to a standard calculator that you might have installed already on your computer but more basic. It can add, subtract, multiply, divide, and switch between negative and positive numbers. I changed the layout of the numbers away from the traditional 3x3 grid and towards a 2x5 grid so that all of the numbers fit in two rows. I also color coordinated the button types so that similar button types were grouped together by color, which is not typical on a standard calculator. Overall, I think that the project was a success. I have never been able to turn Python code into a GUI application until today, so that is a big improvement. 

Here is a screenshot of what the calculator looks like:

![Screenshot of basic calculator](https://github.com/bexcoding/python-tkinter-project/blob/main/calculator-screenshot.png)

Of course it looks very basic, but this can be improved on over time. While I am proud of this calculator, here are some of the improvements that I would make if I did it again:

1. Use class-based code. I think that some of the aspects of this program could be simplified or improved if I had access to the benefits of a class. I wrote all of the code in the `main()` function but this could make it hard to tell sections of the code apart from each other. For example, the button creation, styling, and functionality all exists inside one function. 
2. Separate logic from design. For cleanliness, I would prefer that the design and implementation of the buttons and input areas remain separate from the logic (i.e., the functions that act on the buttons). This would make my docstrings and documentation less distracting from the designing and placement of the buttons.
3. Add more buttons. It would be cool to have all of the buttons of a standard calculator. The reason that I didn't try to implement all of the buttons is that I know that a standard calculator would look better and be more reliable than a calculator that I could make with `tkinter`. I would rather spend the time on a project that creates something that I don't have access to yet.

# Password Generator

My second `tkinter` project is a random password generator. I had created a password generator already and have a repository on my main GitHub with the code, but this program had to be run on the terminal. I wanted to make something so easy to use that even my wife could use it (like many others, she does not know how to use a terminal). I created this GUI version of the password generator where a user can choose the size of the password that they want to make and can decide what elements to include in the password. This would be useful, for example, if you had to make a new password for your banking website that was 10 characters long and needed to include numbers, symbols, and uppercase and lowercase letters. The nice part about this application is that I didn't have to worry so much about the kinds of input that I would receive from the user. Because there are a limited number of options for password size with the slider, I didn't have to watch out for negative or float numbers. This simplification allowed me to write a more simple password class for this app. Eventually, I would like to have a component on the app that shows the strength of the password based on the chosen options. 

Here is a screenshot of how the app looks when launched:

![Screenshot of main screen](https://github.com/bexcoding/python-tkinter-project/blob/main/rpg-home.png)

A protective section that I wrote into the password generation was accounting for pressing `Create Password` before choosing any options. This could have the potential to crash the program. In this case, the program will create a password using lowercase letters and numbers:

![Screenshot of running without choosing options](https://github.com/bexcoding/python-tkinter-project/blob/main/rpg-no-options.png)

I allowed enough space with the original window sizing to make six passwords in the case that someone wanted to choose from a list of options. Going beyond six passwords is fine too. The window can be resized to see the other passwords that are generated. Below, you can see what it looks like to create several different passwords using a length of 15 characters and all character types:

![Screenshot with all options chosen](https://github.com/bexcoding/python-tkinter-project/blob/main/rpg-all-options.png)
