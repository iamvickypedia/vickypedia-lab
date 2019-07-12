import time, os, sys, transpositionEncrypt, transpositionDecrypt, argparse

help_text = "Open or Close file, and maybe check status\nfile.py [filename] [mode]\nCurrently accepting modes ---- \nopen\nclose\nstatus"
parser = argparse.ArgumentParser(description=help_text,add_help=True,formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument(dest='myMode',nargs='*')
args = parser.parse_args()
magic = "Ac3s$F!L3"
params = args.myMode
# import pdb;pdb.set_trace()
if args.myMode and len(params) > 0:
    filename, *myMode = params
    if not os.path.exists(filename):
        print("please enter proper file name")
        sys.exit()
    if len(myMode) == 0:
        myMode = 'status'
    else:
        myMode = myMode[0]
else:
    myMode = None
def write_to_file(outputFilename,translated,mode):
    outputFileObj = open(outputFilename, 'w')
    if mode == 'close':
        outputFileObj.write(magic)
    outputFileObj.write(translated)
    outputFileObj.close()

def get_status(content):
    if content[:len(magic)] != magic:
        return 'open'
    else:
        return 'closed'

def main():
    global myMode
    Filename = 'credsninfo.txt'

    if not myMode:
        myMode = 'status'

    myKey = 10
    if not os.path.exists(Filename):
        print(f'The file {Filename} does not exist. Quitting...')
        sys.exit()

    fileObj = open(Filename)
    content = fileObj.read()
    fileObj.close()

    if myMode == 'close':
        if get_status(content) == 'closed':
            print("File already closed")
            sys.exit()
        translated = transpositionEncrypt.encryptMessage(myKey, content)
    elif myMode == 'open':
        if get_status(content) == 'open':
            print("File already open")
            sys.exit()
        translated = transpositionDecrypt.decryptMessage(myKey, content[len(magic):])

    elif myMode == 'status':
        # print("Status")
        if content[:len(magic)] != magic:
            print('file is open')
        else:
            print('file is closed')
        sys.exit()
    else:
        print(help_text)
        sys.exit()

    write_to_file(Filename,translated,myMode)
    print(f'{Filename} is now {myMode}')

if __name__ == '__main__':
    pass
    main()
