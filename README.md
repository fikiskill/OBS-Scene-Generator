# OBS-Scene-Generator
Python script to automatically create/transform any possibly necessary scenes/sources for wall macros using the obs-websocket-py python library
# Instructions
1) Install [Python 3.7+](https://www.python.org/downloads/) and [OBS websocket](https://obsproject.com/forum/resources/obs-websocket-remote-control-obs-studio-from-websockets.466/)
2) After that drag obssetup.py into your wall/scripts
4) Make sure that obsSettings.py and settings.ahk are configured
5) After following these instructions run OBS and run the script (you dont need to have your instances open)
6) Note that if you are using hotkeys for scene switching in obs (which you shouldnt because obs websocket switching is better and you already set it up for this script okayge) the macro will not create those hotkeys for you. The library is just unable to do that
# Issues
## Some sources didnt create
If you are trying to create a source that already exists with the name you set in your settings it won't work. To avoid this rename sources that already exist or create a completely fresh scene collection
## Error messages
I included some common error messages in the script. Make sure to read them carefully and follow what they say. After that restart your script
## If you have any other rarer issues dm me on discord fikiskill#9693
## Credits

- Me okayge
- Javacord people for the source position equation
- Specnr's Tech Support team for helping with other stuff
