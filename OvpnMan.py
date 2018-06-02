#!/usr/bin/env python
# -*- coding: utf-8 -*-
#    OvpnMen - 2018
#    Penaxr  - penaxr@protonmail.com
#    Github  - https://github.com/Penaxr
#
#    Version:
#
#    Wrote this because I wanted a way to chose between my openvpn configs
#    using a menu. (will be adding more as I learn.)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import time
# Prog settings
__version__ = "0.0.1"
__author__  = "penaxr - https://github.com/penaxr"
__date__    = "02.06.2018"
__mail__    = "penaxr@protonmail.com"

from colorama import init, Fore, Style

colors = {
	"":        "",
	"red":     Fore.RED,
	"cyan":    Fore.CYAN,
	"blue":    Fore.BLUE,
	"green":   Fore.GREEN,
	"white":   Fore.WHITE,
	"yellow":  Fore.YELLOW,
	"magenta": Fore.MAGENTA,
	"bright":  Style.BRIGHT
}

def banner():
	print colors["bright"] + colors["red"] + """
    ██████╗ ██████╗ ██╗   ██╗███╗   ██╗███╗   ███╗ █████╗ ███╗   ██╗
    ██╔═══██╗██╔══██╗██║   ██║████╗  ██║████╗ ████║██╔══██╗████╗  ██║
    ██║   ██║██████╔╝██║   ██║██╔██╗ ██║██╔████╔██║███████║██╔██╗ ██║
    ██║   ██║██╔═══╝ ╚██╗ ██╔╝██║╚██╗██║██║╚██╔╝██║██╔══██║██║╚██╗██║
    ╚██████╔╝██║      ╚████╔╝ ██║ ╚████║██║ ╚═╝ ██║██║  ██║██║ ╚████║
    ╚═════╝ ╚═╝       ╚═══╝  ╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                    [OpenVPN Connection Manager]
"""


menu_action = {}

# Menu de base
def base_menu():
    os.system('clear')
    banner()

    print "\t-------------------------------------------------------"
    print colors["white"] + "\n[01] start openvpn session"
    print "[02] list ovpn profiles"
    print "[03] Check Updates"
    print "\n[99] Quit"
    choice = raw_input("[-] Choose: ")
    exec_menu(choice)

    return

# Commandes du menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['base_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Invalid Option.\n"
            menu_actions['base_menu']()
    return

# menu ovpn
def sess_menu():
    os.system('clear')
    banner()
    print colors["white"] + "Select Ovpn Config!!\n"
    for file in os.listdir("ovpnconfs/"):
      if file.endswith(".ovpn"):
         print colors["magenta"] + (os.path.join(file))

         print colors["white"] + "\n[9] Back"
    choice = raw_input("[-] Choose: ")
    if choice == "penaxr.ovpn":
        ovpn_penaxr()
    #exec_menu(choice)
    return

# menu liste ovpn
def list_ovpn():
    os.system('clear')
    banner()
    print colors["white"] + "These are the available OpenVPN profiles\n"
    for file in os.listdir("ovpnconfs/"):
      if file.endswith(".ovpn"):
         print colors["magenta"] + (os.path.join(file))

    print colors["white"] + "\n[9] Back"
    choice = raw_input("[-] Choose: ")
    exec_menu(choice)
    return
# ont retourne a base menu
def retour():
    menu_actions['base_menu']()

# Quiter le prog
def userquit():
    sys.exit()
# defs des profiles vpn
def ovpn_penaxr():
    os.system("openvpn --config ovpnconfs/penaxr.ovpn")
# defs des menu
menu_actions = {
    'base_menu': base_menu,
    '1': sess_menu,
    '2': list_ovpn,
    '9': retour,
    '99': userquit,
}

# OvpnMen
if __name__ == "__main__":
    banner()
    base_menu()
