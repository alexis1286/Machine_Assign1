import sys

# input via the command line interface. Reads in user input and places the values on a list
user_input = list(sys.argv[1:])
conv_list = []


# -------------------------------------------------------------------------------------------------------------------
# convert - this does the mathematical calculations based on the value that is passed into the function
def convert(x):
    b = str('')
    while x != 0:
        if (x % 2) == 0:
            k = str('0')
            x /= 2
            b = k + b
        else:
            k = str('1')
            x = (x - 1) / 2
            b = k + b
    # format value
    b = '{:0>4}'.format(b)
    return b


# -------------------------------------------------------------------------------------------------------------------
# negative convert - this functions converts the negatives values that a user would input
def negative_con(n):
    neg_temp = str(n)
    neg_temp = neg_temp.replace("0", "2")
    neg_temp = neg_temp.replace("1", "0")
    neg_temp = neg_temp.replace("2", "1")

    return neg_temp


# -------------------------------------------------------------------------------------------------------------------
# decimal conversion - this function handles decimals if a user were to input a decimal value to be converted
def decimal(dec):
    d_bin = str('')
    while dec != 0:
        dec *= 2
        if dec >= 1:
            d_bin += '1'
            dec -= 1
        else:
            d_bin += '0'
    # format decimal for any repeats
    d_bin = d_bin[:8]
    return d_bin


# -------------------------------------------------------------------------------------------------------------------
# final for loop - this for loop handles all of the traversing and calls functions to handle the conversion.
for i in range(len(user_input)):
    cur = user_input[i]

    cur = float(cur)
    flag = None
    # flags to handle values less than 0
    if cur < 0:
        flag = True
        cur = abs(cur)
    else:
        flag = False
    # while number and decimal number declared as int values
    w = int(cur)
    d = cur - int(cur)
    # handle 0s
    if w == 0:
        if flag is True:
            fin_w = '1'
        else:
            fin_w = '0'
    else:
        if flag is True:
            fin_w = convert(w)
            fin_w = negative_con(fin_w)
        else:
            fin_w = convert(w)
    # declaring the final values for whole number and decimal for output
    fin_w = str(fin_w)
    final = (fin_w + '.' + decimal(d))
    conv_list.append(final)

# -------------------------------------------------------------------------------------------------------------------
# print the table - this is the table output, the for loop will traverse through and output the
# original value that the user inputted, and the converted value on the right hand side of the table
print('|       Base 10      |        Base 2      |')
print('|:-------------------|:-------------------|')
for j in range(len(conv_list)):
    print('|{: <20}|{: <20}|'.format(user_input[j], conv_list[j]))
