import random
import os
import subprocess
import pyfiglet

clsc = "cls" if os.name == "nt" else "clear"
subprocess.run(clsc, shell=True, check=True)

banner = pyfiglet.figlet_format("Halloween Keyer", font= 'doom')

print(banner)

def generate_code():
    return ''.join(random.sample('1234', 4))

while True:
    code = generate_code()
    print(f"\nInput number seq: {code}")

    while True:
        guess = input("Michael Input: ")
        if guess == code:
            print("Correct")
            break
        else:
            print("Incorrect, try again.")