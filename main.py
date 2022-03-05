# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
msg = 'yc bfv g'
msg = ''
msg = msg + 'yc bfv g'
msg = msg + 'nj dvzsg'
msg = msg + 'pbg kngm'
msg = msg + 'swqkf yo '
msg = msg + 'r wgdpjq'
msg = msg + 'rzgb ims'
msg = msg + 'xkbt cw '
msg = msg + 'scaiwek '
msg = msg + 'cle cimc'
msg = msg + 'ljgd'

#msg = 'ynpsrrxscl'
#msg = 'qyfwigynigcnqbylyhinuffcmumcnmyygm'
dict = 'abcdefghijklmnopqrstuvwxyz'

for i in range (26):
    newStr = ''
    for k in range(len(msg)):
        tmpChar=msg[k]
        for n in range(len(dict)):
            if tmpChar == dict[n]:
                idx = n - i
                if idx < 0:
                    idx = idx + len(dict)
                newChar = dict[idx]
        #if tmpChar == ' ':
        #    newChar = ' '
        newStr = newStr + newChar
    print(i,newStr)