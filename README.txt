For this save data system to work, the person implementing the microservice with have to save send commands through the pipe in a very specific way.

Here is the format of the commands:
'<command>:
 <data name>
 <data if applicable>'

there will be 3 commands implemented:
* Delete: remove the specified <data name>
* Load: load the specified <data name>
* Save: save teh specified <data name>

The formatting of the data will be loaded in the same way that it was saved, format and all. Except it will not send the command line through the text file.
If the data under that name already exists, it will overwrite the previous data