#!/usr/bin/env python3
import os

class data_save():
    def read_cmd():
        pipe = 'resp.txt'

        modif = os.path.getmtime(pipe)
        prev = modif
        while True:
            modif = os.path.getmtime(pipe)
            if modif != prev:
                break
        return

    def startup():
        os.system('cls' if os.name == 'nt' else "printf '\033c'")
        print("1. save data\n2. load data\n3. delete data\n4. exit\n")
        user_in = input("what would you like to do?")
        if user_in == '1':
            data_save.one()
        elif user_in == '2':
            data_save.two()
        elif user_in == '3':
            data_save.three()
        return
    
    def one():
        os.system('cls' if os.name == 'nt' else "printf '\033c'")
        name = input("what is the name you would like the file to be: ")
        user_in = 'y'
        lines = []
        while user_in == 'y':
            line = input("what is the first line you would like to save? ")
            user_in = input("would you like to continue adding lines (y/n)? ")
            lines.append(line)
        pipe = open('pipe.txt', 'w')
        pipe.write(f'save\n{name}\n')
        for line in lines:
            pipe.write(f'{line}\n')
        pipe.close()
        data_save.startup()
        
    def two():
        os.system('cls' if os.name == 'nt' else "printf '\033c'")
        name = input("what is the name you would like to load: ")
        pipe = open('pipe.txt', 'w')
        pipe.write(f'load\n{name}')
        pipe.close()
        data_save.read_cmd()
        print(f"data in {name}.txt\n")
        with open('resp.txt', 'r') as resp:
            for line in resp:
                print(line.removesuffix('\n'))
        resp.close()
        input('\ninput to leave: ')
        data_save.startup()

    def three():
        os.system('cls' if os.name == 'nt' else "printf '\033c'")
        name = input("what is the name you would like to delete: ")
        pipe = open('pipe.txt', 'w')
        pipe.write(f'delete\n{name}')
        pipe.close()
        data_save.read_cmd()
        resp = open('resp.txt', 'r')
        print(resp.readline())
        resp.close()
        input('\ninput to leave: ')
        data_save.startup()

if __name__ == "__main__":
    data_save.startup()