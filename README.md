# OBS-Scene-Generator
Python script to automatically create/transform any possibly necessary scenes/sources for wall macros using the obs-websocket-py python library
# Instructions
1) Install [Python 3.7+](https://www.python.org/downloads/) and [OBS websocket](https://obsproject.com/forum/resources/obs-websocket-remote-control-obs-studio-from-websockets.466/)
2) Open up command prompt, and paste this command: `pip install obs-websocket-py`
3) Aftet that drag the script into your wall/scripts folder with the extraSettings.py file
4) Make sure that obsSettings.py, extraSettings.py and settings.ahk are configured
5) After following these instructions run OBS and run the script (you dont need to have your instances open). Everything should work fine but if you have any issues see [issues](#Issues)
6) Note that if you are using hotkeys for scene switching in obs (which you shouldnt because obs websocket switching is better and you already set it up for this script okayge) the macro will not create those hotkeys for you. The library is just unable to do that
# Issues
## Some sources didnt create
If you are trying to create a source that already exists with the name you set in your settings it won't work. To avoid this rename sources that already exist or create a completely fresh scene collection
## Nothing happened
If nothing created at all it might be the issue above or your the script not being able to connect to your obs. Try dragging in [this script](https://cdn.discordapp.com/attachments/979162301582155856/980354974372495370/wstest.py) into your wall scripts folder and running it through cmd. If it doesnt throw any errors then the macro was able to succesfully connect to your obs. If there was an error try reading it and checking if your obssettings.py are correctly configured
## If you have any other rarer issues dm me on discord fikiskill#9693
## Credits

- Me okayge
- Javacord people for the source position equation
- Specnr's Tech Support team for helping with other stuff
