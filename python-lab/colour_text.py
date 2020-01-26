import argparse, random, time

parser = argparse.ArgumentParser(description='Description')

parser.add_argument('-s',dest="style",type=int,required=False,help="style , range 0-9")
parser.add_argument('-f',dest="fg",type=int,required=False,help="fg , range 30-38")
parser.add_argument('-b',dest="bg",type=int,required=False,help="bg , range 40-48")

args = parser.parse_args()
if args.style and args.fg and args.bg:
    style=args.style
    fg=args.fg
    bg=args.bg
else:
    pass

def random_colour():
    fg, bg = 1, 1
    while (fg%10) == (bg%10):
        style,fg,bg = random.randint(0,9),random.randint(30,38), random.randint(40,48)
    return print_color(style,fg,bg)

def print_color(style,fg,bg):
    format_text = '\x1b[{};{};{}m Sample Text \x1b[0m'.format(style,fg,bg)
    return format_text

#res = print_color(style,fg,bg)
for _ in range(15):
    res = ""
    for _ in range(10):
        print(random_colour(),end="\t")
        time.sleep(0.05)
        #res += random_colour()
        
    print()
