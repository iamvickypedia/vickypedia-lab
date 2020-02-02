import hashlib,sys,os


algos = {
        "1":hashlib.md5,
        "2":hashlib.sha1,
        "3":hashlib.sha256,
        "4":hashlib.sha512,
        }

def checksum(fname,mode):
    if os.path.isfile(fname):
        checksum = algos.get(mode,None)()
        with open(fname,"rb") as f: 
            for chunk in iter(lambda: f.read(4096) , b''):
                checksum.update(chunk)
            return checksum.hexdigest()
    else:
        raise FileNotFoundError("Not a File")

fname = ""
while fname == "":
    fname = input("Enter file path : ")

algo = ""
while algo == "" or algo not in ["1","2","3","4","5"]:

    algo = input("""
Enter checksum algorithm :
1. md5
2. sha1
3. sha256
4. sha512
5. exit
""")


if algo != "5":
    print(checksum(fname,algo))
else:
    print("Exiting...")