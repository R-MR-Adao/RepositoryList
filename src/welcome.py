from termcolor import colored
import time

ascii_welcome = ['   ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ██╗',
                 '   ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ██║',
                 '   ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ██║',
                 '   ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ╚═╝',
                 '   ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ██╗',
                 '   ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ╚═╝']

ascii_thankyou = [' ████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗  ██╗░░░██╗░█████╗░██╗░░░██╗██╗',
                  ' ╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝  ╚██╗░██╔╝██╔══██╗██║░░░██║██║',
                  ' ░░░██║░░░███████║███████║██╔██╗██║█████═╝░  ░╚████╔╝░██║░░██║██║░░░██║██║',
                  ' ░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░  ░░╚██╔╝░░██║░░██║██║░░░██║╚═╝',
                  ' ░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗  ░░░██║░░░╚█████╔╝╚██████╔╝██╗',
                  ' ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░╚═╝']

def print_list(**kargs):
    for i in kargs['l']:
        if 'color' in kargs:
            print(colored(i, kargs['color']))
        else:
            print(i)


def center(s):
    return ' ' * round((text_width - len(s))/2) + s


def blink(s,n):
    for i in range(n):
        print(s, end='\r')
        time.sleep(0.6)
        print(' ', end='\r')
        time.sleep(0.4)


def type_write(s):
    sent = ''
    for letter in s:
        if letter == '~':  # new line
            print(sent)
            sent = ''
        else:
            sent += letter
            print(sent, end='\r')
        if letter in '.!?,:':
            time.sleep(0.5)
        else:
            time.sleep(0.035)
    print(sent)


def line_break(s):
    if len(s) > text_width:
        ss = ' '.join(s[:text_width] .split(' ')[:-1])
        return ss + '~' + line_break(s[len(ss):])
    else:
        return s


text_width = 73

print('\n')
print_list(l=ascii_welcome, color='green')
time.sleep(0.5)
print('')
print(colored(center(' To my GitHub Repository list!'), 'cyan'))
print('')
time.sleep(0.5)
blink(colored(center(' Press any key to start'), 'yellow'), 4)

type_write(line_break(' Thank you for visiting this page!'))
type_write(line_break(' My name is ' + colored('Ricardo Adão', 'cyan') + ' and I\'m a software developer!'))
type_write(line_break(' Most of the contents listed on this repository were developed during my PhD, which means that'
                      ' Intellectual Property ownership rights prevent me from sharing some of my codes publicly'
                      '...'))
print('')
type_write(line_break(' But don\'t loose hope! I am still able to share my code privately, as long as it is not used'
                      ' for commercial purposes 😊'))
time.sleep(1)
print('')
type_write(line_break(' All you need to do is contact me through my linkedin:'))
type_write(line_break(' https://www.linkedin.com/in/rmradao/'))
time.sleep(1)
print('')
type_write(line_break(' So have fun exploring the documentation below, and don\'t hesitate to contact me if you\'re'
                      ' interested in any of my software!'))
time.sleep(2)
print('')
type_write(line_break(' And once again,'))
time.sleep(0.5)
print('')
print_list(l=ascii_thankyou, color='green')
time.sleep(9)
print('')
