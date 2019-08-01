import subprocess,argparse,sys,os

parser = argparse.ArgumentParser(description="Description",add_help=True)
parser.add_argument('-p',dest='port',required=True,help="Port to open docker on")
parser.add_argument('-v',dest='vol',required=True,help="docker volume path")
args = parser.parse_args()
if args.port and args.vol:
    con_port = args.port
    vol = args.vol
    if not os.path.exists(vol):
        print("Invalid volume path")
        sys.exit()

run_cmd = "docker run --restart unless-stopped --name docker-nginx -p {}:80 -d -v {}:/usr/share/nginx/html nginx".format(con_port,vol)
p1 = subprocess.run(run_cmd,stdout=subprocess.PIPE,shell=True)
#print(run_cmd)
print(p1.stdout.decode())

