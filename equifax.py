import hashlib
import sys
import getpass

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
lastInputChar = pswd[8]

pswd = hashlib.md5(pswd).hexdigest()
secondHashCharCap = pswd[1].upper()

#print pswd[0] + secondHashCharCap + pswd[2:19] + lastInputChar

# command to copy the output string to your clipboard
pyperclip.copy(pswd[0] + secondHashCharCap + pswd[2:19] + lastInputChar)
print bcolors.OKGREEN + "Copied to clipboard" + bcolors.ENDC
