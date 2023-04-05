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
