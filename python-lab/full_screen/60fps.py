from time import time,sleep
import curses, datetime
import shutil, os, math

def printFrame(data):
    for i,row in enumerate(data):
        row_data = "".join(map(str,row))
        stdscr.addstr(i,0,row_data)

    stdscr.refresh()
    # print(statement,end="\r")

def getScreenData(num,frame,c,r):
    body = [
    [i for i in range(0,10)],
    ["▏","▎","▍","▌","▋","▊","▉","▊","▋","▌","▍","▎"],
    ['⠋','⠙','⠹','⠸','⠼','⠴','⠦','⠧','⠇','⠏'],
    ["▁","▃","▄","▅","▆","▇","▆","▅","▄","▃"],
    ["✶","✸","✹","✺","✹","✷"],
    ]
    data,rdata =  body[int(num/2)], body[int(num/2)][::-1]

    if num%2 == 0:
        return map(lambda rw : map(lambda x:data[(x+frame)%(len(rdata) - 1)], range(c)),range(r))
    else:
        return map(lambda rw : map(lambda x:data[(x+frame)%(len(data) - 1)] if rw%2 else rdata[(x-frame)%(len(data) - 1)], range(c)),range(r))


if __name__ == "__main__":
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    frame = 0
    start = time()
    c,r = shutil.get_terminal_size()
    # c,r = int(c/2),r-1
    c,r = c,r-1
    # screen[rm][cm] = 0
    screen_no = 1
    try:
        os.system('setterm -cursor off')
        while True:
            frame += 1
            if frame%100 == 0:
                screen_no = (screen_no % (4*2)) + 1
            screen = getScreenData(screen_no, frame,c,r)
            printFrame(screen)
            sleep(1/30) # 60 fps
            # sleep(1)
    finally:
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        os.system('setterm -cursor on')
        print("Thank you")

