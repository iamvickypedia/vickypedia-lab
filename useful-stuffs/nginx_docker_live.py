import subprocess, argparse, sys, os

parser = argparse.ArgumentParser(description="Description", add_help=True)
parser.add_argument("-v", dest="vol", required=True, help="docker volume path")
parser.add_argument("-p", dest="port", required=False, help="Port to open docker on")
args = parser.parse_args()


def main():

    if args.vol:
        vol = args.vol
        if args.port:
            con_port = args.port
        else:
            con_port = 80
        if not os.path.exists(vol):
            print("Invalid volume path")
            sys.exit()
    else:
        print("Please enter volume location")
        sys.exit()
    run_clean = "docker stop docker-nginx; docker rm docker-nginx"
    run_cmd = "docker run --restart unless-stopped --name docker-nginx -p {}:80 -d -v {}:/usr/share/nginx/html nginx".format(
        con_port, vol
    )
    print("Cleaning existing setup ...")
    clean = subprocess.run(run_clean, stdout=subprocess.PIPE, shell=True)
    print(clean.stdout.decode())
    print(f"Starting new setup on port {con_port} ...")
    p1 = subprocess.run(run_cmd, stdout=subprocess.PIPE, shell=True)
    # print(run_cmd)
    print(p1.stdout.decode())


if __name__ == "__main__":
    main()

