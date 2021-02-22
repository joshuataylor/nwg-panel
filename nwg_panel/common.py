#!/usr/bin/env python3

import os
sway = False

if os.getenv('SWAYSOCK') is not None:
    from i3ipc import Connection
    i3 = Connection()

ipc_data = None

outputs = {}
windows_list = []
taskbars_list = []
scratchpads_list = []
controls_list = []
config_dir = ""
app_dirs = []

dependencies = {
    "pyalsa": False,
    "psutil": False,
    "netifaces": False,
    "amixer": False
}

icons_path = ""  # "icons_light", "icons_dark" or "" (GTK icons)

commands = {
    "get_bt_name": "bluetoothctl show | awk '/Name/{print $2}'",
    "get_bt_status": "bluetoothctl show | awk '/Powered/{print $2}'",
    "get_brightness": "light -G",
    "get_host": "uname -n",
    "get_ssid": "iwgetid -r",
    "get_user": "echo $USER",
    "get_volume_alt": "amixer sget Master",
    "set_brightness": "light -S",
    "set_volume_alt": "amixer sset Master",
    "systemctl": "systemctl",
    "playerctl": "playerctl"
}
