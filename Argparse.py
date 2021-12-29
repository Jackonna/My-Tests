import argparse

parser = argparse.ArgumentParser()
groupe = parser.add_mutually_exclusive_group()

groupe.add_argument("-s", "--simple", help="Print words", action="store_true")
groupe.add_argument("-e", "--elabore", help="Print a sentence with words", action="store_true")
# action = "store_true" necessary to write only -s or -e

parser.add_argument("object", help="The object")
parser.add_argument("-c", "--color", help="The color of the object")
args = parser.parse_args()

if args.elabore:
    if args.color is None:
        args.color = ""
    print("This is a {} {}.".format(args.object, args.color))
elif args.simple:
    print("Color:", args.color, "Name:", args.object)
else:
    if args.color is None:
        args.color = ""
    print(args.color, args.object "\t", args)
    # Output : green bottle 	 Namespace(color='green', object='bottle')
    print(type(args.color), type(args.object), type(args))
    # Output : <class 'str'> <class 'str'> <class 'argparse.Namespace'>

