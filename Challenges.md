# Challenges

Here I document some of the challenges I faced when making this bot.

## Starting
Having the bot start the game was pretty simple. Using the [webbrowser](https://docs.python.org/3/library/webbrowser.html) module, I'm able to easily open up the page for the game and using [pyautogui](https://pyautogui.readthedocs.io/en/latest/) I'm able to manually move to mouse to positions on the screen in order to start the game.

## Mouse positions
Now having the capability of moving the mouse wherever I want, I need a quick way to get some working dimensions so I know where to direct the mouse. The [coords](https://addons.mozilla.org/en-US/firefox/addon/coords/) extension for Firefox made this a lot simpler.

## Tile recognition
Ok, now we can move the mouse and we know where to move it, what next? Well we need to figure out what to do when a mouse gets to a tile, and the first step is to first figure out what tile the mouse was one. 
