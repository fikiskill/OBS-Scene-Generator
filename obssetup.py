from obswebsocket import obsws, requests
import os,math
import obsSettings as config
import extraSettings as extraconfig

for i in open(os.path.dirname(os.getcwd()) + "\\settings.ahk", "r"):
    if "rows" in i:
        rows = int(i[14:].split(";")[0].strip())
    if "cols" in i:
        cols = int(i[14:].split(";")[0].strip())
    if "fullscreen :=" in i:
        fullscreen = str(i[20:].split(";")[0].strip())
    if "useSingleSceneOBS" in i:
        ss = str(i[27:].split(";")[0].strip())

ws = obsws(config.host, config.port, config.password)
ws.connect()

if ss == "True":
    ws.call(requests.CreateScene(config.main_scene))
    sspos = {"x": 0, "y": 0}
    ssbounds = {"type": "OBS_BOUNDS_STRETCH", "x": ws.call(requests.GetVideoInfo()).getBaseWidth(), "y": ws.call(requests.GetVideoInfo()).getBaseHeight()}
    minipos = {"x": extraconfig.miniposx, "y": extraconfig.miniposy}
    minibounds = {"type": "OBS_BOUNDS_STRETCH", "x": extraconfig.minix, "y": extraconfig.miniy}
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
for i in range(rows * cols, 0, -1):
    possettings = {"y": math.floor((i - 1) / cols) * boundsettings["y"], "x": (i - 1) % cols * boundsettings["x"]}
    settings = {'window': f"Minecraft* - Instance {i}:GLFW30:javaw.exe"}
    gamesettings = {'anti_cheat_hook': False, 'capture_mode': 'window', 'hook_rate': 3, 'window': f"Minecraft* - Instance {i}:GLFW30:javaw.exe"}
    if fullscreen == "True":
        ws.call(requests.CreateSource(f"{extraconfig.wall_source_format}{i}", "game_capture", config.wall_scene_name, gamesettings))
    else:
        ws.call(requests.CreateSource(f"{extraconfig.wall_source_format}{i}", "window_capture", config.wall_scene_name, settings))
    ws.call(requests.SetSceneItemProperties(scene_name = config.wall_scene_name, item = f"{extraconfig.wall_source_format}{i}", bounds = boundsettings, position = possettings))
