import time,os,sys,math,random,pdb,shutil
try:
    import curses
except:
    import wcurses as curses

def startm(sent):
    start=len(sent)
    another_mode = False
    win = curses.initscr()
    win.nodelay(True)
    i = 1
    while True:
        start = shutil.get_terminal_size().columns
        ch = win.getch()
        if ch == 113:
            break
        if i%start == 0:
            
            another_mode = not another_mode

        if another_mode:
            c ="\r{}{}".format(sent[(i%start):]," "*(i%start)) 
        else:
            c = "\r{}{}".format(" "*(start-(i%start)),sent[:i%start])
        
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
        i = i + 1


sent='Thank you for checking out this marquee. Press q to stop. '
os.system('setterm -cursor off')
try:
    startm(sent)
except:
    
    os.system('setterm -cursor on')
else:
    os.system('setterm -cursor on')
sys.stdout.write('\r%%%%----Seeya Later----%%%%')
sys.stdout.flush()
