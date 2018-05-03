import hashlib
import sys
import getpass
import pyperclip

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

pswd = getpass.getpass("Password: ")
secondInputChar = pswd[1]

pswd = hashlib.md5(pswd).hexdigest()

#print pswd[:19] + secondInputChar

# command to copy the output string to your clipboard
pyperclip.copy(pswd[:19] + secondInputChar)
print bcolors.OKGREEN + "Copied to clipboard!" + bcolors.ENDC
