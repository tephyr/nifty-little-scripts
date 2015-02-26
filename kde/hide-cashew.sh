#!/bin/sh
## To hide the KDE "cashew" (toolbox icon) run this script & reboot.
## This will need to be re-run after any KDE system upgrade.
## Other possible ways documented here: http://askubuntu.com/questions/24867/how-do-i-remove-the-kde-4-plasma-tool-box-cashew-icon-from-the-desktop

sudo chmod 600 /usr/lib/kde4/plasma_toolbox_desktoptoolbox.so
