
import argparse
parser = argparse.ArgumentParser(description='Running health checks everyday')
parser.add_argument('--prod', dest='isprod', const=True, help='If prod records are to be evaluated',nargs='?')

parser.set_defaults(isprod=False)
isprod = parser.parse_args().isprod
isprod = True if isprod or isprod == "" else False
print("Is Prod",isprod)
