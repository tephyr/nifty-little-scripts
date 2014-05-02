import subprocess

# get all current windows
command = 'wmctrl -l'
output = system.exec_command(command, getOutput=True)
stlines = []
for line in output.split("\n"):
    if "Sublime Text" in line:
        stlines.append(line)

#dialog.info_dialog(title="stlines", message="stlines.count: {0}".format(len(stlines)))
if len(stlines) == 0:
    # sublime text not running
    subprocess.Popen(["sublime_text"])
else:
    # an instance of Sublime Text is running
    winClass = window.get_active_class()

    if "sublime_text" not in winClass:
        # if current window class is not "sublime_text.Sublime_text", then activate "Sublime"
        # doesn't matter how many instances are running; just activate one
        window.activate("Sublime", switchDesktop=True)
    elif "sublime_text" in winClass and len(stlines) > 1:
        # multiple windows, Sublime Text already active, move to next
        current_title = window.get_active_title()
        stinfolines = []
        # strip first 3 columns of each line 
        # beware: may be multiple spaces
        for line in stlines:
            # take out multiple spaces in 1st 16 characters
            if "  " in line[:16]:
                line = line.replace("  ", " ", 1)
            stinfolines.append(line.split(" ", 3)[3])
        
        #dialog.info_dialog("Sublime Text window info",
        #    "current window: {0}\nother windows\n{1}".format(window.get_active_title(),
        #        "\n".join(stinfolines)
        #    ))

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
