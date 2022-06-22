import os,math

if os.system("pip help --quiet") != 0:
    print("reinstall python and make sure to check the box that says ""add python to PATH""")
    input("")
try:
    from obswebsocket import obsws, requests
except:
    os.system("pip install obs-websocket-py --quiet")
    from obswebsocket import obsws, requests
try:
    import obsSettings as config
except:
    print("obsSettings not found! make sure you drag this script into your TheWall/scripts folder")
    input("")
    
ws = obsws(config.host, config.port, config.password)
try:
    ws.connect()
except:
    print("error while connecting, make sure your obs is on and that your obssettings are correct")
    input("")

for i in open(os.path.dirname(os.getcwd()) + "\\settings.ahk", "r"):
    if "rows" in i:
        rows = int(i[14:].split(";")[0].strip())
    if "cols" in i:
        cols = int(i[14:].split(";")[0].strip())
    if "fullscreen :=" in i:
        fullscreen = str(i[20:].split(";")[0].strip())
    if "useSingleSceneOBS" in i:
        ss = str(i[27:].split(";")[0].strip())


if ss == "True":
    minix = input("enter the X resolution of your mini sources, for the default one enter nothing:\n")
    if not len(minix):
        minix = 560
    miniy = input("enter the Y resolution of your mini sources, for the default one enter nothing:\n")
    if not len(miniy):
        minix = 560
    miniposx = input("enter the X position of your mini sources, for the default one enter nothing:\n")
    if not len(miniposx):
        minix = 560
    miniposy = input("enter the X position of your mini sources, for the default one enter nothing:\n")
    if not len(miniposy):
        minix = 560
    ws.call(requests.CreateScene(config.main_scene))
    sspos = {"x": 0, "y": 0}
    ssbounds = {"type": "OBS_BOUNDS_STRETCH", "x": ws.call(requests.GetVideoInfo()).getBaseWidth(), "y": ws.call(requests.GetVideoInfo()).getBaseHeight()}
    minipos = {"x": miniposx, "y": miniposy}
    minibounds = {"type": "OBS_BOUNDS_STRETCH", "x": minix, "y": miniy}
    for i in range(rows * cols, 0, -1):
        settings = {'window': f"Minecraft* - Instance {i}:GLFW30:javaw.exe"}
        gamesettings = {'anti_cheat_hook': False, 'capture_mode': 'window', 'hook_rate': 3, 'window': f"Minecraft* - Instance {i}:GLFW30:javaw.exe"}
        if fullscreen == "True":
            ws.call(requests.CreateSource(f"{config.mc_source_format}{i}", "game_capture", config.main_scene, gamesettings))
        else:
            ws.call(requests.CreateSource(f"{config.mc_source_format}{i}", "window_capture", config.main_scene, settings))
        ws.call(requests.SetSceneItemProperties(scene_name = config.main_scene, item = f"{config.mc_source_format}{i}", bounds = ssbounds, position = sspos))
    for i in range(rows * cols, 0, -1):
        settings = {'window': f"Minecraft* - Instance {i}:GLFW30:javaw.exe"}
        ws.call(requests.CreateSource(f"{config.bg_mc_source_format}{i}", "window_capture", config.main_scene, settings))
        ws.call(requests.SetSceneItemProperties(scene_name = config.main_scene, item = f"{config.bg_mc_source_format}{i}", bounds = minibounds, position = minipos))
    ws.call(requests.CreateSource(config.wall_scene_name, "scene", config.main_scene))
else:
    ws.call(requests.CreateScene(config.wall_scene_name))
    multiscenebounds = {"type": "OBS_BOUNDS_STRETCH", "x": ws.call(requests.GetVideoInfo()).getBaseWidth(), "y": ws.call(requests.GetVideoInfo()).getBaseHeight()}
    multiscenepos = {"x": 0, "y": 0}
    for i in range(1, rows * cols + 1):
        settings = {'window': f"Minecraft* - Instance {i}:GLFW30:javaw.exe"}
        gamesettings = {'anti_cheat_hook': False, 'capture_mode': 'window', 'hook_rate': 3, 'window': f"Minecraft* - Instance {i}:GLFW30:javaw.exe"}
        ws.call(requests.CreateScene(f"{config.scene_name_format}{i}"))
        if fullscreen == "True":
            ws.call(requests.CreateSource(f"{config.mc_source_format}{i}", "game_capture", f"{config.scene_name_format}{i}", gamesettings))
        else:
            ws.call(requests.CreateSource(f"{config.mc_source_format}{i}", "window_capture", f"{config.scene_name_format}{i}", settings))
        ws.call(requests.SetSceneItemProperties(scene_name = f"{config.scene_name_format}{i}", item = f"{config.mc_source_format}{i}", bounds = multiscenebounds, position = multiscenepos))

boundsettings = {"type": "OBS_BOUNDS_STRETCH", "x": ws.call(requests.GetVideoInfo()).getBaseWidth() / cols, "y": ws.call(requests.GetVideoInfo()).getBaseHeight() / rows}
wall_source_format = input("enter the name of the sources that will be on your verifiaction/wall scene")
for i in range(rows * cols, 0, -1):
    possettings = {"y": math.floor((i - 1) / cols) * boundsettings["y"], "x": (i - 1) % cols * boundsettings["x"]}
    settings = {'window': f"Minecraft* - Instance {i}:GLFW30:javaw.exe"}
    gamesettings = {'anti_cheat_hook': False, 'capture_mode': 'window', 'hook_rate': 3, 'window': f"Minecraft* - Instance {i}:GLFW30:javaw.exe"}
    if fullscreen == "True":
        ws.call(requests.CreateSource(f"{wall_source_format}{i}", "game_capture", config.wall_scene_name, gamesettings))
    else:
        ws.call(requests.CreateSource(f"{wall_source_format}{i}", "window_capture", config.wall_scene_name, settings))
    ws.call(requests.SetSceneItemProperties(scene_name = config.wall_scene_name, item = f"{wall_source_format}{i}", bounds = boundsettings, position = possettings))
