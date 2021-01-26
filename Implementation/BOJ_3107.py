# IPv6 - G5

import sys


def fill_zero(address):
    for i in range(len(address)):
       while len(address[i])<4:
           address[i]='0'+address[i]

    return address

def IPv6(address):
    if len(address)>8:
        zero=address.index('')
        address.pop(zero)

    zero=address.index('')
    address[zero]='0000'

    while True:
        if len(address)==8:
            break
        address.insert(zero,'0000')

    address=fill_zero(address)
    return address

if __name__=="__main__":
    ip=sys.stdin.readline().rstrip()
    ip_address=ip.split(':')

    if len(ip_address)==8:
        ip_address=fill_zero(ip_address)
    else:
        ip_address=IPv6(ip_address)

    print(':'.join(ip_address))