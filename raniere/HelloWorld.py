import sys

args = sys.argv
name = "World"

if len(args) > 1 : name = args[1]

print("Hello, {}!".format(name))