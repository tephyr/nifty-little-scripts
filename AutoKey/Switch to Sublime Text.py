import subprocess

# get current window class
winClass = window.get_active_class()

# if current window class is not "sublime_text.Sublime_text", then activate "Sublime"
if False: #"sublime_text" not in winClass:
    window.activate("Sublime", switchDesktop=True)
else:
    # if it is, then search for other windows (wmctrl -l)
    command = 'wmctrl -l'
    output = system.exec_command(command, getOutput=True)
    stlines = []
    for line in output.split("\n"):
        if "Sublime Text" in line:
            stlines.append(line)

    #dialog.info_dialog(title="stlines", message="stlines.count: {0}".format(len(stlines)))
    if len(stlines) == 0:
        # sublime text not running
        #result = dialog.input_dialog(title="Sublime Text not running", message="Launch Sublime Text now?")
        #dialog.info_dialog(title="?", message="Result: {0}".format(result))
        #subprocess.Popen(["/usr/bin/firefox"])
        subprocess.Popen(["sublime_text"])
    elif len(stlines) == 1:
        window.activate("Sublime", switchDesktop=True)
    elif len(stlines) > 1:
        # multiple windows, move to next
        current_title = window.get_active_title()
        stinfolines = []
        # strip first 3 columns of each line 
        # beware: the spaces may be multiple
        for line in stlines:
            # take out multiple spaces in 1st 16 characters
            if "  " in line[:16]:
                line = line.replace("  ", " ", 1)
            stinfolines.append(line.split(" ", 3)[3])
        
        dialog.info_dialog("Sublime Text window info",
            "current window: {0}\nother windows\n{1}".format(window.get_active_title(),
                "\n".join(stinfolines)
            ))

        # find *next* line to activate
        if stinfolines[-1] == current_title:
            # activate first line
            window.activate(stinfolines[0], True)
        else:
            target = 0
            for line in stinfolines:
                target += 1
                if current_title == line:
                    # use next
                    break
                    
            window.activate(stinfolines[target], True)
