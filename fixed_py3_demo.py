import math
import re


# Global
Green   = '\033[1;32;40m'
Yello   = '\033[0;33;40m'
Cyan    = '\033[1;36;40m'
Red     = "\033[0;31;40m"
Lowkey  = "\033[0;2m"
# Reset   = '\033[0m' 
Reset   = '\033[0;0m' 
Formula = Cyan + 'applied: ' + Yello + 'n*(1<<8):' + Reset


# Fpv printer
def fpv(n) -> None:
    print(f'{Green}testing:{Yello} {n} {Reset}')
    print(f'{Lowkey}type   : {str(type(n))[8:-2]} {Reset}')

    if type(n) is int:
        bin_num = format(n, '0{}_b'.format(4))
        print(f'{Cyan}binary :{Reset} {bin_num}')
    else:
        print(f'{Red}no binary representation for non-int{Reset}')

    m = n * (1 << 8)
    m = round(m)
    bin_num = format(m, '{}_b'.format(4))
    print(Formula)
    if type(n) is float:
        print(f'{Red}round() applied for float {n}{Reset}')
    print(f'\tresult: {m}')
    print(f'\tbinary: {bin_num} \n\n------8<--------\n')


# Default tests
fpv(42)
fpv(1)
fpv(333)
fpv(math.pi)
fpv(196883)
fpv(math.tau)
fpv(123.4567)

# Test your own input
print("Test your own input:" )
infile = ''
while (True):
    infile = input().strip()
    if not re.findall('^[0-9\.]+$', infile):
        break
    res = int(infile) if '.' not in infile else float(infile)
    fpv(res)
