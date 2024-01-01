import argparse
import sys

def calc(args):
    if args.o == 'add':
        return args.f + args.s
    elif args.o == 'diff':
        return args.f - args.s
    else:
        return args.o

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--f', type=float, default=1.0, help=r"Help for --first number")
    parser.add_argument('--s', type=float, default=0.0, help=r"Help for --second number")
    parser.add_argument('--o',type=str, default="None", help="Performs operation add/diff")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))