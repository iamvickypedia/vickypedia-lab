import sys
import base64
print(sys.argv[-2:])
if len(sys.argv) > 2:
 _, s,m = sys.argv
elif len(sys.argv) == 1:
 print("No value to process")
 sys.exit()
else:
 s,m = sys.argv[1],"e"
if m.lower() == "e":
    print(base64.b64encode(s.encode('utf-8')).decode())

if m.lower() == "d":
    print(base64.b64decode(s.encode('utf-8')).decode())
    
