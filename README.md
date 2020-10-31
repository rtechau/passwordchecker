# passwordchecker
Simple password checker to see if the entered password has been hacked.

This script will take the user intput password and hash it. 
Then check the first 5 characters of the hashed password against the pwnedpasswords api. 
It will then return the number of times those characters appear in the database and suggest to change the password or that it was not found in the database.

Uses Tkinter to create GUI instead of using as a commandline tool. 
