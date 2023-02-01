#
from random import randrange
import os, sys

FILE = 'patterns'

def read_again():
    global FILE, bytebeat, lastime
    
    with open(FILE,'r') as file:
        seq = file.read()

    pattern = eval(seq)
    bytebeat=bytes()

    for step in pattern:
        with open(f'{step}.raw','rb') as file:
            thesebytes = file.read()
        
        bytebeat += thesebytes
    
    lastime = os.stat(FILE).st_ctime

read_again()

while True:
    
    if os.stat(FILE).st_ctime != lastime: read_again()
    #print(bytebeat.decode('cp437'),end='')
    sys.stdout.buffer.write(bytebeat)    

