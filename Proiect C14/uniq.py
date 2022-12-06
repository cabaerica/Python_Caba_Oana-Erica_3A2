import sys
from os import path
import uniq_functions

#types of commands:
informational_commands = ["--help", "--version"]
long_commands = ["--skip-fields", "--skip-chars", "--check-chars"]
short_commands_without_num = ["-c", "-d", "-D", "-i", "-u", "-z", "--count", "--repeated", "--ignore-case", "--unique", "--zero-terminated"]
short_commands_with_num = ["-f", "-s", "-w"]
method_commands = ["--all-repeated",  "--group"]

#if(len(sys.argv) == 2):
#    command_line = sys.argv[1]
#    if command_line not in informational_commands and not path.isfile(command_line):
#        raise Exception("Input not valid")
#    
#    if command_line == "--help":
#        print(uniq_functions.help())
#        exit()
#    elif command_line == "--version":
#        print(uniq_functions.version())
#        exit()
#    else:
#        try:
#            with open(command_line, "r") as f:
#                print(uniq_functions.uniq(f.read().splitlines()))
#                exit()
#        except IOError:
#            print("Error while opening the input file")
#
#if(len(sys.argv) == 3):
#    first_command = sys.argv[1]
#    second_command = sys.argv[2]
#    #if first_command.split("=")[0] not in long_commands and first_command not in short_commands_without_num and not path.isfile(first_command):
#    #    raise Exception("First argument is invalid")
#    #elif first_command.split("=")[0] in long_commands and (not int(first_command.split("=")[1] or not path.isfile(first_command)) or len(first_command.split("=")) > 2):
#    #    raise Exception("Input not of type [LONG_COMMAND]=N [INPUT]")
#    #elif first_command in short_commands_without_num and not path.isfile(second_command):
#    #    raise Exception("Input not valid")
#    #elif first_command.split("=")[0] in method_commands and 
#    
#    if path.isfile(first_command):
#        try:
#            with open(first_command, "r") as f:
#                uniq_functions.uniq(f.read().splitlines())
#                exit()
#        except IOError:
#            print("Error while opening the input file")
#    
#    if first_command in short_commands_without_num and path.isfile(second_command):
#        print(uniq_functions.uniq_with_short_command(first_command, second_command))
#        exit()
#    elif first_command.split("=")[0] in long_commands and path.isfile(second_command):
#        if len(first_command.split("=")) > 2:
#            raise Exception("Number in command not valid")
#        print(uniq_functions.uniq_with_long_command(first_command.split("=")[0], second_command, int(first_command.split("=")[1])))
#        exit()
#    elif first_command.split("=")[0] in method_commands and path.isfile(second_command):
#            if len(first_command.split("=")) == 1:
#                print(uniq_functions.uniq_with_long_command(first_command, second_command))
#                exit()
#            elif len(first_command.split("=")) == 2:
#                print(uniq_functions.uniq_with_long_command(first_command.split("=")[0], second_command, first_command.split("=")[1]))
#                exit()
#            else:
#                raise Exception("Method not valid")
#    raise Exception("Invalid input")
if(len(sys.argv)) < 2:
    raise Exception("Invalid input")

input = ""
output = ""
args = sys.argv
del args[0]

if len(args) >=2 and path.isfile(args[-2]): 
    input = args[-2]
    output = args[-1]
    del args[-2]
    del args[-1]
    
elif path.isfile(sys.argv[-1]):
    input = sys.argv[-1]
    del args[-1]

fin = open(input, "r")
list = fin.read().splitlines()
if not args:
    list = uniq_functions.uniq(list)

count = False

for i in range(0, len(args)):
    if args[i] in short_commands_without_num:
        if i+1 == len(args):
            list = uniq_functions.uniq_with_short_command(args[i], list)
        elif i+1 != len(args) and type(args[i+1]) == str:
            if args[i] != "-c" and args[i] != "--count":
                list = uniq_functions.uniq_with_short_command(args[i], list)
            else: count = True

    elif args[i] in informational_commands:
        if(args[i] == "--help"):
            list = uniq_functions.help()
        elif(args[i] == "--version"):
            list = uniq_functions.version()
        break

    elif args[i].split("=")[0] in long_commands:
        if len(args[i].split("=")) != 2:
            raise Exception("Invalid input")
        list = uniq_functions.uniq_with_long_command(args[i].split("=")[0], list, args[i].split("=")[1])

    elif args[i].split("=")[0] in method_commands:
        if len(args[i].split("=")) == 1:
            list = uniq_functions.uniq_with_long_command(args[i].split("=")[0], list)
        elif len(args[i].split("=")) == 2:
            list = uniq_functions.uniq_with_long_command(args[i].split("=")[0], list, args[i].split("=")[1])
        else:
            raise Exception("Invalid input")

    elif args[i] in short_commands_with_num:
        if i+1 == len(args):
            raise Exception("Invalid input")
        elif i+1 != len(args) and type(args[i+1]) == int:
            list = uniq_functions.uniq_with_long_command(args[i], list, args[i+1])
            i += 1
    else: raise Exception("Invalid input")

if count:
    list = uniq_functions.uniq_with_short_command("-c", list)

if output:
    fout = open(output, "w")
    fout.write(str(list))

print(list)
