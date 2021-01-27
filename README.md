# xorSc
Script to perform XOR operations on each byte within shellcode

# Usage
Simply copy the shellcode within the byte array in the code file.

Expected input, shellcode from objdump. You can follow this link from commandlinefu.com to learn more.
https://www.commandlinefu.com/commands/view/6051/get-all-shellcode-on-binary-file-from-objdump

Replace my shellcode with yours if you are using this by putting shellcode between the two quotes (') after the 'b' and before the closing bracket

# raw_sc = bytearray(b'\xeb\x17\x31\xc0\xb0\x04\x31\xdb\xb3\x01\x59\x31\xd2\xb2\x19\xcd\x80\x31\xc0\xb0\x01\x31\xdb\xcd\x80\xe8\xe4\xff\xff\xff\x48\x65\x6c\x6c\x6f\x20\x53\x65\x63\x75\x72\x69\x74\x79\x4e\x69\x6b\x57\x6f\x72\x6c\x64\x21')
    
Once you replace tbe bytes, specify your key in the variable below if needed. There is nothing wrong with using the one I have there.
# xor_key = 0x0A

Once you run the code, your output will look as shown below.

# Sample Output

[*] XOR Encoder / Decoder

[*] Author: Nik Alleyne

[*] Blog: www.securitynik.com

[*] XORing 53 bytes of Shellcode with key 0xa
*****************************************************
[*] Finished encoding all 53 bytes

[*] XORd data in decimal 
 [225, 29, 59, 202, 186, 14, 59, 209, 185, 11, 83, 59, 216, 184, 19, 199, 138, 59, 202, 186, 11, 59, 209, 199, 138, 226, 238, 245, 245, 245, 66, 111, 102, 102, 101, 42, 89, 111, 105, 127, 120, 99, 126, 115, 68, 99, 97, 93, 101, 120, 102, 110, 43]

[*] XORd data in comma separated bytes
0xe1,0x1d,0x3b,0xca,0xba,0xe,0x3b,0xd1,0xb9,0xb,0x53,0x3b,0xd8,0xb8,0x13,0xc7,0x8a,0x3b,0xca,0xba,0xb,0x3b,0xd1,0xc7,0x8a,0xe2,0xee,0xf5,0xf5,0xf5,0x42,0x6f,0x66,0x66,0x65,0x2a,0x59,0x6f,0x69,0x7f,0x78,0x63,0x7e,0x73,0x44,0x63,0x61,0x5d,0x65,0x78,0x66,0x6e,0x2b,
 [!] DO NOT COPY THE FINAL",". Thanks! 

[*] XORd data in hex stream
e11d3bcabae3bd1b9b533bd8b813c78a3bcabab3bd1c78ae2eef5f5f5426f6666652a596f697f78637e734463615d6578666e2b

[*] XORd data in escaped format
\xe1\x1d\x3b\xca\xba\xe\x3b\xd1\xb9\xb\x53\x3b\xd8\xb8\x13\xc7\x8a\x3b\xca\xba\xb\x3b\xd1\xc7\x8a\xe2\xee\xf5\xf5\xf5\x42\x6f\x66\x66\x65\x2a\x59\x6f\x69\x7f\x78\x63\x7e\x73\x44\x63\x61\x5d\x65\x78\x66\x6e\x2b\x
 [!] DO NOT COPY THE FINAL "\x". Thanks! 
 
 
 Have fun!
 
