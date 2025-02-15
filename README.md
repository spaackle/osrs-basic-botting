Pretty sure this isn't functional anymore, as you need the Status Socket plugin, and it didn't look like it was still available for Runelite when I briefly checked recently. You'd have to find a way to get that running, or OCR the tile data from another plugin.
Also, if you have any issues with "live_data.json", just create a blank file called that in the same folder as server.py and it should run, it's just writing to that file iirc.

Also if you're trying to use this thinking you're going to bot with it you're missing the point. This is just to provide examples of color bot implementation for anyone looking to learn to code with OSRS.

# osrs-basic-botting
A few python scripts for simple botting in OSRS. I would recommend running these on a virtual machine so they can run in the background while you do other things. Have used these pretty extensively and as far as I know they're undetectable, but use at your own risk.

# Miner.py 

This script is set to mine iron ore from the Al Kharid mine, then once your inventory is full, it paths back to the Al Kharid bank to deposit, and then paths back and repeats. Fully functional, but you __might__ run into some bugs. At some point, I'll add a video tutorial for setup and configuration.

You can find a video of the script in action here: https://www.youtube.com/watch?v=p-4p_eerk34&ab_channel=spackle

To use this, you'll need the following RuneLite plugins - Object Markers, Ground Markers, Status Socket, Shortest Path, Camera Points


Object Markers is used to mark the bank and ore, Ground Markers is used to mark out the path, Camera Points is used to setup the camera for each stage, Shortest Path is used initially to help with marking out the most efficient tile path, and Status Socket is a plugin that sends info to a local server, and is used to update the current tile. You'll need to run server.py to collect that info.

1. Use Object Markers to mark the following:

  Ore - __Pink__ = (Red - 255, Green - 0, Blue - 255)

  Bank - __Red__ = (Red - 255, Green - 0, Blue - 0)

  Also, in the Object Markers settings, select Highlight Clickbox only, and set Border Width to 3.


2. Next, you'll need to use Ground Markers to mark out your path:

  For the settings, set color to __Blue__ = (Red - 0, Green - 0, Blue - 255), set Border Width to 5, Fill Opacity to 100, and check Draw Tiles On Minimap.

  You can use Shortest Path to find the most efficient pathing. For this script, simply stand next to the Al Kharid bank stall, open the world map, right click where   the iron ore is, and click Set Target. You'll see a red line leading you to the tile you selected, simply mark the starting tile, then follow the path marking tiles about every 10 tiles or so (just need to have every next tile viewable from the minimap). Once your path is set, you're good to go!


3. For Camera Points, set it up like the following image:

![Camera Points](https://user-images.githubusercontent.com/31822308/233782849-cd761bf8-b480-47a8-8bc8-d4a5ab447f1b.PNG)

Also, make sure you do the following:

1. Line 10 - Make sure your pytesseract path is correct

2. Line 12 - Replace UsernameHere with your username

Then, all you need to do is run server.py, then run miner.py.

# Smelter.py

Smelting script for iron ore. Will withdraw iron ore from Al Kharid bank, smelt it, then repeat.

For this you'll need the following Runelite plugins - Object Marker, Ground Markers, Camera Points

1. Use Object Markers to mark the smelter in __Yellow__ (Red - 255, Green - 255, Blue - 0) and mark the bank in __Red__ (Red - 255, Green - 0, Blue - 0)

2. Use Ground Markers to mark the space directly in front of the bank booth, a space in between the bank and the smelter, and the spot directly in front of the smelter. Mark these in __Green__ (Red - 0, Green - 255, Blue - 0)

3. For Camera Points, set it up like the following image:

![Camera Points](https://user-images.githubusercontent.com/31822308/233782849-cd761bf8-b480-47a8-8bc8-d4a5ab447f1b.PNG)

Then you're good to go, just run the script!


# Fighter.py



__TEMP REMOVED. WILL REWRITE AND REUPLOAD SOON.__


This script simply fights cows and eats lobsters when low. Rough script, works but it's messy. I'll likely rewrite this soon.

For this you'll need the following Runelite plugins - Object Marker, Health Notifications

1. Use Object Markers to mark the cows in __Red__ (Red - 255, Green - 0, Blue - 0)

2. In Health Notifications, set the Hitpoint Threshold to whatever you think is best (for leveling combat on new accounts and fighting cows, I set this to 4). Also, set the Overlay Color to __Blue__ (Red - 0, Green - 0, Blue - 255), and check Disable Notification.

Then, run the script.


