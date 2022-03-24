# Challenges

Here I document some of the challenges I faced when making this bot.

## Starting
Having the bot start the game was pretty simple. Using the [webbrowser](https://docs.python.org/3/library/webbrowser.html) module, I'm able to easily open up the page for the game and using [pyautogui](https://pyautogui.readthedocs.io/en/latest/) I'm able to manually move to mouse to positions on the screen in order to start the game.

## Mouse positions
Now having the capability of moving the mouse wherever I want, I need a quick way to get some working dimensions so I know where to direct the mouse. The [coords](https://addons.mozilla.org/en-US/firefox/addon/coords/) extension for Firefox made this a lot simpler.

## Tile recognition
Ok, now we can move the mouse and we know where to move it, what next? Well we need to figure out what to do when a mouse gets to a tile, and the first step is to first figure out what tile the mouse was on. I first tried lining up the mouse on the exact pixel where the color of the number was, using the `pyautogui.screenshot()` function, then analyzing the pixel where my mouse was. This was bad for several reasons.
1. I hadn't realized it at the time but `pyautogui.screenshot()` screenshots the entire screen which I don't need and is probably time consuming
2. I was relying that my tiny mouse pointer would land exactly on the tiny part of the tiny square where there was color
3. The color of the number (or any pixel shape really) fades near the edges so results weren't always accurate


Clearly there's a lot that can be improved upon here, so here some solutions:
1. Instead of taking a screenshot of the entire screen, I can take a screenshot of just the one square using `pyautogui.screenshot(region=)`. Now we're not grabbing the entire screen
2. Once I have this small screen shot, I can use the `PIL.image.getcolors()` function to obtain an unsorted list of every distinct color in screenshot along with their pixel frequency (which would be at max 23x23 pixels wide, not very big relatively speaking).
3. Once I get the colors, I can filter out the faded edges of the number by removing the lower pixel frequencies to get the most dominate colors for each tile. This would either be just the background color, just the grass color or a combination of background and number.
4. After that, I wrote a small function to determine the nature of the tile, and now we have tile recognition!

## Difficult numbers
I'm lazy and don't want to make a replica of Google minesweeper, but I also need to ensure that the mouse is able to detect every number, even the ones that don't show up very often like 6, 7 and 8. However, it's very hard to test for something that happens very rarely that you also can't control. 

Thankfully, [others](https://www.reddit.com/r/Minesweeper/comments/s10ek7/got_a_7_and_a_6_google_minesweeper/) on the internet have encountered these numbers and have been kind enough to [document them](https://www.reddit.com/r/Minesweeper/comments/oxyatz/my_first_8_tile/). 

Now I can screenshot a game I have in progress and using photo editing software like [Gimp](https://www.gimp.org/) can easily test that these values work and refine my algorithm when they don't.

## Outside the board
Should a tile be uncovered near the edge of the board, there's a chance that at some point the bot will find enough empty tiles and start flagging or uncovering the adjacent tiles. This is great if it's inside the board but this also brings the chance of the bot clicking outside the board

I implemented a small function to check if coordinates to click on are valid.
