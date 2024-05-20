#!/usr/bin/env python3
import os
curr_dir = os.getcwd()

class data_save():
    def startup():
        os.chdir(curr_dir)
        pipe = 'pipe.txt'

        modif = os.path.getmtime(pipe)
        prev = modif
        while True:
            modif = os.path.getmtime(pipe)
            if modif != prev:
                break
        data_save.read_cmd()
    
    def read_cmd():
        os.chdir(curr_dir)
        logs = open('pipe.txt', 'r')
        cmd = logs.readline()
        name = logs.readline()
        name = name.removesuffix('\n')
        if 'save' in cmd:
            data_save.save_cmd(name)
        elif 'load' in cmd:
            data_save.load_cmd(name)
        elif 'delete' in cmd:
            data_save.delete_cmd(name)
        else:
            print('error command not recognized')
        logs.close()
        data_save.startup()
    
    def save_cmd(name):
        #try to open the file, if it exists, send warning that all data will be overwritten
        print('command recieved, saving data')
        try:
            os.chdir('sv_db')
            file = open(name + '.txt', 'r')
        except:
            os.chdir(curr_dir)
            resp = open('resp.txt', 'w')
            resp.writelines(f'saving {name}')
        else:
            print('file already exist, will overwrite data')
        
        #starting to save the data and read the data from the pipe

        with open('pipe.txt', 'r') as pipe:
            data_lines = []
            pipe.readline()
            pipe.readline()
            for line in pipe:
                data_lines.append(line)
        pipe.close()

        #saves the data in the saved data directory with the current name of txt file
        os.chdir('sv_db')
        new_file = open(f'{name}.txt', 'w')
        for lines in data_lines:
            new_file.writelines(lines)
        new_file.close()
        os.chdir(curr_dir)
        print(data_lines)
        return
        
    def load_cmd(name):
        #attempting to load the requested data
        print('command recieved, loading data')
        os.chdir('sv_db')
        print(os.getcwd())
        try:
            file = open(f'{name}.txt', 'r')
        except:
            #if the file does not exist, write to the response text, that it doesn't exist
            os.chdir(curr_dir)
            print('file does not exist, sending response')
            resp = open('resp.txt', 'w')
            resp.writelines(f"couldn't open file {name}")
            resp.close()
            return
        file.close()
        print(f'loading {name}')
        
        #open the file that they are trying to access and return the data in the response
        with open(f'{name}.txt', 'r') as data:
            data_lines = []
            for line in data:
                data_lines.append(line)
        data.close()
        os.chdir(curr_dir)

        #write the data to the response file
        resp = open('resp.txt', 'w')
        for lines in data_lines:
            resp.writelines(lines)
        resp.close()
        return
    
    def delete_cmd(name):
        #attempt to open the path to the file 
        print('command received, deleting data')
        os.chdir(curr_dir)
        file_path = os.path.join('sv_db', f'{name}.txt')

        #if it doesn't exist return that to the response file
        if not os.path.exists(file_path):
            resp = open('resp.txt', 'w')
            resp.writelines(f'File {name} does not exist')
            return

        #attempt to delete the file if it is in the correct location
        try:
            os.remove(file_path)
        except Exception as e:
            print(f'Error deleting {name}.txt:', e)
            return
        resp = open('resp.txt', 'w')
        resp.writelines(f'Deleted {name}.txt')
    
if __name__ == "__main__":
    data_save.startup()