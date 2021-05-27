"""
Task is to
Convert number 0-9999 to word (4-digit)
"""

num = 809

digits = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 0: 'zero'}
before_twenty = {10:'ten',11: 'eleven', 12: 'twelve', 13: 'thirteen', 15: 'fifteen'}
rank_2 = {2: 'twen', 3: 'thir', 4: 'for', 5: 'fif'}
ranks = ['thousand', 'hundred', 'ty', '']


def find_len(num):
    length = 0
    digit_list = []
    for i in range(4):
        digit_list.append(0)
    i = 0
    while num >= 10:
        mod = num % 10
        num = num // 10
        length += 1
        digit_list[i] = mod
        i += 1
    length += 1
    digit_list[i] = num
    return length, digit_list


def split_to_digits(num):
    length, digit_list = find_len(num)
    return digit_list[::-1]

digit_list = split_to_digits(num)
out = ''
for i in range(2):
    dig = digit_list[i]
    if dig!=0:
        out += digits[dig]+' '+ranks[i]+' '

decimal=digit_list[2]
unit=digit_list[3]
two_digit_num= 10 * decimal + unit

if decimal==1:
    if two_digit_num in before_twenty:
        out += before_twenty[two_digit_num]
    else:
        ending='teen'
        if unit==8:
            ending='een'
        out += digits[unit] + ending
elif decimal==0:
    out+=digits[unit]
elif decimal in rank_2:
    out+=rank_2[decimal]+ranks[2]
    if unit!=0:
        out+=' '+digits[unit]
else:
    ending = 'ty'
    if decimal == 8:
        ending = 'y'
    out += digits[decimal] + ending + ' ' + digits[unit]

print(out)

# length, digit_list = find_len(num)
