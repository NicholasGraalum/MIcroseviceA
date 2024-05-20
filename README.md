# MIcroseviceA

![UML](https://github.com/NicholasGraalum/MIcroseviceA/assets/129789294/d71eceef-db43-4cba-ab6e-16a76a676df3)

## To request data
### from this system you must use the pipe.txt file to communicate to the data_save.py file
### This requires a specific fromat inside of the pipe.txt:

### commands save, load, delete<>
### name of file to be or already existing file<>
### if the file is save, add as many lines you want to save<>

Example of saving:
save
gerald
played a game 
bought a game
made a game

To recieve data from the microservice you must check the resp.txt file.
When calling the data for loading, it will return it in the format you sent it as, excluding the name and command.

Example of load response with gerald:
played a game 
bought a game
made a game
