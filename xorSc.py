#!/usr/bin/env python3
'''
    Author: Nik Alleyne
    Author Blog: www.securitynik.com
    Filename: xorSc.py

    Script simply performs an XOR on each byte within shellcode.
'''

import subprocess as sp

def main():
    sp.call('clear')
    print('[*] XOR Encoder / Decoder')
    print('[*] Author: Nik Alleyne')
    print('[*] Blog: www.securitynik.com')
    
    # Create a storage place for each XOR'd byte
    xor_encoded_bytes = []
    '''
    Shellcode from objdump.
    replace my shellcode with yours if you are using this. 
    Put your shellcode between the two quotes (') after the 'b' and before the closing bracket
    '''
    raw_sc = bytearray(b'\xeb\x17\x31\xc0\xb0\x04\x31\xdb\xb3\x01\x59\x31\xd2\xb2\x19\xcd\x80\x31\xc0\xb0\x01\x31\xdb\xcd\x80\xe8\xe4\xff\xff\xff\x48\x65\x6c\x6c\x6f\x20\x53\x65\x63\x75\x72\x69\x74\x79\x4e\x69\x6b\x57\x6f\x72\x6c\x64\x21')
    
    '''  
    Specify your xor key to use. 
    I use the last value of my shellcode which is 
    new line and where my shell code ends
    '''
    xor_key = 0x0A

    print('[*] XORing {} bytes of Shellcode with key {}'.format(len(raw_sc), hex(xor_key)))

    # Begin the xoring process of each byte in the byte array 'raw_sc'
    for raw_byte in raw_sc:
        xor_encoded_bytes.append(raw_byte^xor_key)
        print('*', end='')

    print('\n[*] Finished encoding all {} bytes'.format(len(raw_sc)))

    print('\n[*] XORd data in decimal \n {}'.format(xor_encoded_bytes))
    
    print('\n[*] XORd data in comma separated bytes')
    for xord_byte in xor_encoded_bytes:
        print(hex(xord_byte), end=',')

    print('\n\033[1;31;40m [!] DO NOT COPY THE FINAL",". Thanks! \033[0m')
    
    print('\n[*] XORd data in hex stream')
    for xord_byte in xor_encoded_bytes:
        print(format(xord_byte, 'x'), end='')
    
    print('\n\n[*] XORd data in escaped format')
    print('\\x', end='')
    for escaped_byte in xor_encoded_bytes:
        print(format(escaped_byte, 'x'), end='\\x')
    
    print('\n\033[1;31;40m [!] DO NOT COPY THE FINAL "\\x". Thanks! \033[0m')


if __name__ == '__main__':
    main()
