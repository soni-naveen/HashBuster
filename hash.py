import hashlib
import os
import sys
import time
from termcolor import colored
#importing the required libraries

print (f'''\033[1;97m_  _ ____ ____ _  _    ___  _  _ ____ ___ ____ ____
|__| |__| [__  |__|    |__] |  | [__   |  |___ |__/
|  | |  | ___] |  |    |__] |__| ___]  |  |___ |  \\  \n''' )

time.sleep(1)
print("HashBuster (v1.1) starting...")
time.sleep(1.4)
supported_hashes = '''
\n
[--Supported Hash Types--]
        *MD5
        *SHA-1
        *SHA-256
        *SHA-512
\n
'''
#printing the supported hash types...--///

print(colored(supported_hashes, 'green'))


if len(sys.argv) != 4:
    print(colored("[*]Usage python3 hash.py <hash-value> <hash-type> <path-to-password-file>\n", 'white', attrs=['reverse', 'blink']))
    sys.exit(0)
    #Checking for correct number of arguments

hash_value = sys.argv[1]
hash_type = sys.argv[2]
pass_file = sys.argv[3]
#Receiving the neccessary arguments for cracking the hash value...

if os.path.exists(pass_file) == False:
    print(colored("[!]Password File Not Found...exiting now", "red", attrs=['bold']))
    sys.exit(0)
#Check if the specified password file exists or not...

with open(pass_file, 'r', encoding='latin-1') as file:
    for line in file.readlines():
        #open and read the file containig passwords to check with
        if hash_type == 'md5':
            #condition to check if the hash type is MD5
            hash_object = hashlib.md5(line.strip().encode())
            hashed = hash_object.hexdigest()
            if hashed == hash_value:
                #if the hash_value given equals the hashed_value from passwords at any point print the cracked hash value and exit the program
                print("[*]Initializing HashBuster. . . . .")
                print(colored(f"\n\n[+]MD5 Hash Cracked Successfully------Value = {line.strip()}\n\n", 'green', attrs=['bold']))
                sys.exit(0)

        elif hash_type == 'sha1':
            #condition to check if the hash type is SHA-1
            hash_object = hashlib.sha1(line.strip().encode())
            hashed = hash_object.hexdigest()
            if hashed == hash_value:
                #if the hash_value given equals the hashed_value from passwords at any point print the cracked hash value and exit the program
                print("[*]Initializing HashBuster. . . . .")
                print(colored(f"\n\n[+]SHA-1 Hash Cracked Successfully------Value = {line.strip()}\n\n", 'green', attrs=['bold']))
                sys.exit(0)
        
        elif hash_type == 'sha256':
            #condition to check if the hash type is SHA-256
            hash_object = hashlib.sha256(line.strip().encode())
            hashed = hash_object.hexdigest()
            if hashed == hash_value:
                #if the hash_value given equals the hashed_value from passwords at any point print the cracked hash value and exit the program
                print("[*]Initializing HashBuster. . . . .")
                print(colored(f"\n\n[+]SHA-256 Hash Cracked Successfully------Value = {line.strip()}\n\n", 'green', attrs=['bold']))
                sys.exit(0)

        elif hash_type == 'sha512':
            #condition to check if the hash type is SHA-512
            hash_object = hashlib.sha512(line.strip().encode())
            hashed = hash_object.hexdigest()
            if hashed == hash_value:
                #if the hash_value given equals the hashed_value from passwords at any point print the cracked hash value and exit the program
                print("[*]Initializing HashBuster. . . . .")
                print(colored(f"\n\n[+]SHA-512 Hash Cracked Successfully------Value = {line.strip()}\n\n", 'green', attrs=['bold']))
                sys.exit(0)
        
    print(colored("\n[*]Please Consider Changing your wordlist of passwords\n", 'red', attrs=['bold']))
    print(print(colored("\n\n[!]Incorrect or Unsupported Hash Type or Password Not Found \n\n", 'red', attrs=['bold'])))
    print(print(colored("\n[*]Please Recheck the arguments you gave\n", 'red', attrs=['bold'])))
    sys.exit(0)
    #this is really annoying --- check your arguments--!Oh!

