# EZSweeper

**This project is still a work in progress**

A side project of mine. A bot that plays Google minesweeper.

Made using [pyautogui](https://pyautogui.readthedocs.io/en/latest/install.html)

This bot should work well on monitors with resolution 1920x1080*

## Cloning instructions

0. Install pipenv as this project uses pipenv to track library installs, run scripts and what not

`pip install pipenv`
1. Clone the repository using `git clone`


`git clone https://github.com/EliasJRH/ezsweeper.git`

2. cd into the cloned directory
3. Install required libraries and set up pipenv virtual environment

`pipenv install`

## Running the bot
You should be able to run the bot right after completing the steps above. Run the main script using:

`pipenv run main`

## Misc
If you want to make any changes to the bot for yourself, you can easily format files using [black](https://github.com/psf/black) with the following command

`pipenv run format`


\* This will only work on monitors with a 1920 x 1080 resolution
