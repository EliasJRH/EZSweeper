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

## Ignoring tiles
The Google minesweeper board on hard difficulty is 24 tiles wide by 20 tiles tall. Doing the math that's 480 total tiles. If I was to check every single tile every time I scanned the board, it would take a while, so I needed to find a way to optimize this. 

I created a list of each tile index to keep track of the tiles I still have to search. Right off the bat, I know that I don't need to search background (dirt) tiles or tiles that have been flagged because I know I'm not going to do anything with them. I'll need to always search grass tiles because they may end up being useful later on, and obviously the uncovered tiles, but only while they have information to give.

Once an uncovered tiles has either flagged all surrounding tiles or clicked all surrounding tiles, there's no need to search it again because it won't offer any new information. All of it's surrounding tiles have been either clicked or flagged so I can ignore them going forward.

Great, now I have a way to speed things up. My initial implementation for this was to use a while loop with a list of coordinates and remove them in transit as tiles became uncovered, but I encountered an unexpected problem. For some reason, tiles that weren't supposed to be removed from this list we're getting removed. I tried several debugging solutions but was never able to replicate this in a controlled environment. Eventually, I chalked this issue up to the bot simply moving to fast, perhaps it was removing things before they could be entirely processed, I'm not sure but I've spent too much time on this to care.

My first solution was to change the way I was removing tiles. instead of constantly removing things from a list which is known to be an O(n) operation for lists, I would simply add each tile I still need to search to a new list, amortized O(1), and replace the searching list on each completion of the bot searching the board. 

That's nice, now I have a slightly faster way of searching, but I was still getting this weird behaviour of prematurely removing tiles. I felt at this point that my only options was to slow down the bot, which wouldn't have been acceptable since this bot needs to be blazing fast (🚀). I figured that if I couldn't beat the bug, I would work around it.

I setup a boolean that would track if a change had been made on the board (flagging or clicking tiles). I initially set it to false everytime the bot begins a scan of the board and then set it to true whenever a change is made. If the bot was to go through the whole board without making any changes, then perhaps it removed a tile that it shouldn't have. If this happened, I set the list of tiles to search back to the entire game board. 

I admit that this isn't an amazing solution - perhaps I could waste more time looking into why it was prematurely ignoring tiles, but if this is happening once every so often, I feel like I can afford the time to rescan the board if it means that the bot will always be correct.
