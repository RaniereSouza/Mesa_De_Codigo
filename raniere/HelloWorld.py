import sys

args    = sys.argv
name    = "World"
message = "Hello, {}!"

if len(args) > 1 : name = args[1]

print(message.format(name))