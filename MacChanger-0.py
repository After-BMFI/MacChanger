"""
You are Required to Keep this document File(and Arbitration Agreement and Warranty Disclaimer)-
-with the Product at all times for Download or redistribution.
MacChanger was created as part of the ECE(Evil Clown Empire) Products Group By Jeff Rogers.
Do Not Let the name fool You the Products Group was Created for Ethical Hacking, Blue Team and Educational Lab Testing Purposes.
https://github.com/BMFI/MacChanger-3.py/blob/main/MacChanger-3.py is now MachChanger-0.py(Name changed)

MacChanger-3.py, MacChanger-0.py and MachChanger.py
After-BMFI valid binding permanent arbitration agreement and warranty disclaimer: You can use the code for free alter then redistribute the code any way you want.
Warranty Disclaimer: Use at your own risk!
After-BMFI or any person associated, affiliated or part of After-BMFI is not accountable or responsible for any harm done by you for using this code.
This code was created by BMFI Jeff Rogers.
You are required to keep this file with the code for download or redistribution.
"""
#!/usr/bin/ python

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m","--mac", dest="new_mac", help="new MAC address")

parser.parse_args()

interface = input(" interface > ")
new_mac = input(" new Mac >")

print("[+] Changing Mac address for " + interface + " to " + new_mac)

# Less secure
#subprocess.call("ifconfig" + interface + "down", shell=True)
#subprocess.call("ifconfig" + interface + " hw ether " + new_mac, shell=True)
#subprocess.call("ifconfig" + interface + " up ", shell=True)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface,"hw", "ether", new_mac])
subprocess.call(["ifconfig", interface,"up"])
