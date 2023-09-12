# Machine Learning Reading Digits
With machine learning from sklearn and UI from pygame, this program can guess the number you draw on the canvas, learn from your drawings and analysis the machine learning model. This program uses supervised support vector machine to guess your digital numbers from 0 to 9. Please draw in the centre of the canvas for better results. This program was developed by Vincent Tang to explore Python and machine learning.

# How to run
The current Python version used in this program is 3.10.9 (64-bit).
Clone the repository with:
```
git clone "https://github.com/megarcrazy/Machine-Learning-Reading-Digits.git"
```

It is important to create a virtual environment when running a Python project. Create a virtual environment in a folder named ".venv" with:
```
python -m venv .venv
```
Activate the environment with:
```
.venv\scripts\activate
```
Install the required packages with:
```
pip install -r requirements.txt
```
Run the application with:
```
python run_application.py
```

# Notable libraries
* :robot: scikit-learn: https://scikit-learn.org/stable/
  * Machine learning modelling
  * Statistic modelling
* :joystick: pygame: https://www.pygame.org/
  * Desktop Application with GUI
* :abacus: numpy: https://numpy.org/
  * Array mathematical calculations
# Linters and Formatter
Linter: Flake8 https://flake8.pycqa.org/en/latest/

Formatter: https://black.readthedocs.io/en/stable/

# How to use
In this program, there is is a training and non-training mode. Training mode is where you can input more data for fitting the model. Non-training mode is where you can draw a number on the canvas and the computer will guess what the number is.
Please allow the program time to fit or evaluate the machine learning model. <br />
Controls: <br />
Escape to menu: Esc <br />
Submit canvas: Space <br />
Reset canvas: R <br />
Draw: Left Click <br />
Erase: Right Click <br />
