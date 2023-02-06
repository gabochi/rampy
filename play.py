import os, sys

FILE = 'out.raw'

def read_again():
    global FILE, bytebeat, lastime
    
    with open(FILE,'rb') as file:
        bytebeat = file.read()
        
    lastime = os.stat(FILE).st_ctime

read_again()

while True:
    
    if os.stat(FILE).st_ctime != lastime: read_again()
    sys.stdout.buffer.write(bytebeat)    

