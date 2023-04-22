# osrs-basic-botting
A few python scripts for simple botting in OSRS.

# Miner.py

This script is set to mine iron ore from the Al Kharid mine, then once your inventory is full, it paths back to the Al Kharid bank to deposit, and then paths back and repeats. You can edit it for any other mine by changing the X and Y ranges in Main. Fully functional, but you __might__ run into some bugs. At some point, I'll add a video tutorial for setup and configuration.

To use this, you'll need the following RuneLite plugins - Object Markers, Ground Markers, Status Socket, Shortest Path, Camera Points


Object Markers is used to mark the bank and ore, Ground Markers is used to mark out the path, Camera Points is used to setup the camera for each stage, and Status Socket is a plugin that sends info to a local server, and is used to update the current tile. You'll need to run server.py to collect that info.


1. Use Object Markers to mark the following:

  Ore - Pure Pink = (Red - 255, Green - 0, Blue - 255)

  Bank - Pure Red = (Red - 255, Green - 0, Blue - 0)

  Also, in the Object Markers settings, select Highlight Clickbox only, and set Border Width to 3.

2. Use Ground Markers to mark the following:

  Tiles - Pure Blue = (Red - 0, Green - 0, Blue - 255)


3. Next, you'll need to use Ground Markers to mark out your path:

  In Ground Markers settings, set Border Width to 5, Fill Opacity to 100, and check Draw Tiles On Minimap.

  You can use Shortest Path to find the most efficient pathing. For this script, simply stand next to the Al Kharid bank stall, open the world map, right click where   the iron ore is, and click Set Target. You'll see a red line leading you to the tile you selected, simply mark the starting tile, then follow the path marking tiles about every 10 tiles or so (just need to have every next tile viewable from the minimap). Once your path is set, you're good to go!


4. For Camera Points, set it up like the following image:

![Camera Points](https://user-images.githubusercontent.com/31822308/233776351-c4e74da2-7234-460a-9beb-691b5b9e00e1.PNG)



Also, make sure you do the following:

1. Line 10 - Make sure your pytesseract path is correct

2. Line 12 - Replace UsernameHere with your username

Then, all you need to do is run server.py, then run miner.py.


# Fighter.py

This script simply fights cows and eats lobsters when low. Rough script, works but it's messy. I'll likely rewrite this soon.

For this you'll need the following Runelite plugins - Object Marker, Health Notifications

1. Use Object Markers to mark the cows in Pure Red (Red - 255, Green - 0, Blue - 0)

2. In Health Notifications, set the Hitpoint Threshold to whatever you think is best (for leveling combat on new accounts and fighting cows, I set this to 4). Also, set the Overlay Color to Pure Blue (Red - 0, Green - 0, Blue - 255), and check Disable Notification.

Then, run the script.


