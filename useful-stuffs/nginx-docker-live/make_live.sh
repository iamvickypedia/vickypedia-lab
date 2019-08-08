# Activate python virtualenv 
if [ -z "$1" ]
then
    VOL="yolo" # needs default wrong value
else
    VOL=$1
fi
if [ -z "$2" ]
then
    PORT="80"
else
    PORT=$2
fi

# Change to python file location
python nginx_docker_live.py -v $VOL -p $PORT