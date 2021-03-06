# Your assignment is to get the last line to print without changing any
# of the code below. Instead, wrap each line that throws an error in a
# try/exept block.

try:
    print("Infinity looks like + " + str(10 / 0) + ".")
except ZeroDivisionError:
    print("Woops. Can't do that.")

try:
    print("I think her name was + " + name + "?")
except NameError:
    print("Oh, I forgot to define 'name'. D'oh.")

try:
    print("Your name is a nonsense number. Look: " + int("Gabriel"))
except ValueError:
    print("Drat. 'Gabriel' isn't a number?")

print("I made it through the gauntlet. The message survived!")
