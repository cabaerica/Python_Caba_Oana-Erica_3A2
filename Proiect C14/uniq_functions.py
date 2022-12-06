all_repeated_methods = ["none", "prepend", "separate"]
group_method = ["separate", "prepend", "append", "both"]

#def uniq(file, file_w = None):
#    lines = file.read().splitlines()
#    if len(lines) == 0:
#        return []
#
#    output = [lines[i-1] for i in range(1,len(lines)) if lines[i-1] != lines[i]]
#    if len(output) == 0:
#        return lines[-1]
#
#    if output[-1] != lines[-1]:
#        output.append(lines[-1]) 
#    if(file_w is None):
#        return output
#    else:
#        w = open(file_w, "w")
#        w.write('\n'.join(output))

def help():
    text = open("help.txt", "r")
    return text.read()

def version():
    text = open("version.txt", "r")
    return text.read()

def uniq_with_short_command(command, list):
    if command in ["-c", "--count"]:
        return uniq_count(list)
    elif command in ["-d", "--repeated"]:
        return uniq_duplicate(list)
    elif command in ["-D"]:
        return uniq_all_duplicates(list)
    elif command in ["-i", "--ignore-case"]:
        return uniq_ignore_case(list)
    elif command in ["-u", "--unique"]:
        return uniq_unique(list)
    else: raise Exception("Invalid command")

def uniq_with_long_command(command, list, number = None):
    if command in ["-f", "--skip-fields"]:
        return uniq_field(list, number)
    if command in ["--all-repeated"]:
        return uniq_all_repeated(list, number)
    if command in ["-w", "--check-chars"]:
        return uniq_chars(list, number)
    if command in ["-s", "--skip-chars"]:
        return uniq_skip_chars(list, number)
    if command in ["--group"]:
        return uniq_group(list, number)
    else: raise Exception("Invalid command")

#def uniq_count(input, file_w = None):
#    file = open(input, "r")    
#    count = 1
#    output = []
#    lines = file.read().splitlines()
#    if len(lines) == 0:
#        return []
#
#    for i in range(1, len(lines)):
#        if lines[i] == lines[i - 1]:
#            count += 1
#        else:
#            output.append([count, lines[i - 1]])
#            count = 1
#
#    if len(output) == 0:
#        return lines[-1]
#
#    if output[-1][1] != lines[-1]:
#        output.append([1, lines[-1]]) 
#    else:
#        output[-1][0] += 1
#    if(file_w is None):
#        return output
#    else:
#        w = open(file_w, "w")
#        w.write('\n'.join(output))

def uniq_duplicate(input):
    count = 1
    output = []
    if len(input) <= 1:
        return []
    
    for i in range(1, len(input)):
        if input[i] == input[i - 1]:
            count += 1
        else:
            if count > 1:
                output.append(input[i - 1])
            count = 1
    if not output:
        return []
    if input[-1] == input[-2] and input[-1] != output[-1]:
        output.append(input[-1])
    return output

def uniq_all_duplicates(input):
    count = 1
    output = []
    if len(input) <= 1:
        return []
    
    for i in range(1, len(input)):
        if input[i] == input[i - 1]:
            count += 1
        else:
            if count > 1:
                output += [input[i - 1] for j in range(0, count)]
            count = 1
    if not output:
        return []
    if input[-1] == input[-2]:
        print("Hello")
        output.append(input[-1])
    return output

def uniq(input):
    if not input or len(input) == 1:
        return input
    output = [input[0]]
    groups = list(zip(input, input[1:]))
    for group in groups:
        for i in group:
            if output[-1] != i:
                output += [i]
    return output

def uniq_count(input):
    if not input:
        return input
    elif len(input) == 1:
        return (1, input[0])

    output = []
    idx_start = 0
    for i, word in enumerate(input[1:]):
        if input[idx_start] != word:
            output.append((int(input[idx_start : i + 1].count(input[idx_start])), input[idx_start]))
            idx_start = i + 1
        if i + 1 == len(input) - 1:
            output.append((int(input[idx_start : len(input)].count(input[idx_start])), input[idx_start]))
    return output

def uniq_field(input, num):
    num = int(num)
    input_fields = []
    output = []
    for word in input:
        fields = word.split()
        if num > len(fields):
            input_fields.append("")
        else:

            input_fields.append(' '.join(fields[num :]))
    counted = uniq_count(input_fields)
    count = 0
    for word in counted:
        output.append(input[count])
        count += word[0]  # type: ignore
    return output

def uniq_all_repeated(input, method = None):
    assert type(method) != str and type(method) != None
    output = ""
    if(method == "none" or method == None):
        return uniq_all_duplicates(input)
    elif(method == "prepend"):
        duplicates = uniq_all_duplicates(input)
        for i in range (1, len(duplicates)):
            output += '\n'
            output += duplicates[i-1]
            if duplicates[i-1] != duplicates[i]:
                output += '\n'
            if i == len(duplicates) - 1:
                output += '\n'
                output += duplicates[i]
        return output
    elif(method == "separate"):
        duplicates = uniq_all_duplicates(input)
        for i in range (1, len(duplicates)):
            output += duplicates[i-1]
            output += '\n'
            if duplicates[i-1] != duplicates[i]:
                output += '\n'
            if i == len(duplicates) - 1:
                output += duplicates[i]
        return output
    else: raise Exception("Method not valid for --all-repeated command")

def uniq_ignore_case(input):
    if not input or len(input) == 1:
        return input
    output = [input[0]]
    groups = list(zip(input, input[1:]))
    for group in groups:
        for i in group:
            if output[-1].lower() != i.lower():
                output += [i]
    return output

def uniq_unique(input):
    count = 1
    output = []
    if len(input) <= 1:
        return []
    
    for i in range(1, len(input)):
        if input[i] == input[i - 1]:
            count += 1
        else:
            if count == 1:
                output.append(input[i - 1])
            count = 1
    if input[-1] != input[-2]:
        output.append(input[-1])
    if not output:
        return []
    return output

def uniq_chars(input, num):
    num = int(num)
    input_fields = []
    output = []
    for word in input:
        if num > len(word):
            input_fields.append("")
        else:
            field = word[:num]
            input_fields.append(field)
    counted = uniq_count(input_fields)
    count = 0
    for word in counted:
        output.append(input[count])
        count += word[0]  # type: ignore
    return output

def uniq_skip_chars(input, num):
    num = int(num)
    input_fields = []
    output = []
    for word in input:
        if num > len(word):
            input_fields.append("")
        else:
            field = word[num:]
            input_fields.append(field)
    counted = uniq_count(input_fields)
    count = 0
    for word in counted:
        output.append(input[count])
        count += word[0]  # type: ignore
    return output

def uniq_group(input, method = None):
    assert type(method) != str and type(method) != None 
    output = ""
    if(method == "prepend"):
        for i in range (1, len(input)):
            output += '\n'
            output += input[i-1]
            if input[i-1] != input[i]:
                output += '\n'
            if i == len(input) - 1:
                output += '\n'
                output += input[i]
        return output
    elif(method == "separate" or method == None):
        for i in range (1, len(input)):
            output += input[i-1]
            output += '\n'
            if input[i-1] != input[i]:
                output += '\n'
            if i == len(input) - 1:
                output += input[i]
        return output
    elif method == "append":
        for i in range (1, len(input)):
            output += input[i-1]
            output += '\n'
            if input[i-1] != input[i]:
                output += '\n'
            if i == len(input) - 1:
                output += input[i]
                output += '\n'
        return output
    elif method == "both":
        output += '\n'
        for i in range (1, len(input)):
            output += input[i-1]
            output += '\n'
            if input[i-1] != input[i]:
                output += '\n'
            if i == len(input) - 1:
                output += input[i]
                output += '\n'
        return output
    else: raise Exception("Method not valid for --group command")
