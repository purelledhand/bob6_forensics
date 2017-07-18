import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--file", help="read file")
args = parser.parse_args()
if args.file:
  f=open(args.file, 'r')
  line = f.readlines()
  for i in line:
    print i
  f.close()
