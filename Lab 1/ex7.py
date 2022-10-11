def first_number_found(text):
     number = ""
     for ch in text:
        if '0' <= ch <= '9':
            number += ch
        else:
            if number:
                return int(number)

print(first_number_found("abc1233abc7"))