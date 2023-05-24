# Scrypt
Scrypt is a simple scripting language that is interpreted by a python file.
To start scripting with Scrypt, clone the repository and edit the core.scrypt file.
When you're done writing your code, drag your file onto the `interpreter.py` and watch it run.

# Usage:

## The `out` statement
Using `out`, you can print out messages to the console, e.g:
```
out This is a text, written from a Scrypt.
```
This will return something like:
```
This is a text, written from a Scrypt.
```
You can use colors with the *variable container* in your scrypt.
```
out Here's an ${RED} Colored ${BLUE} text.
```

## The `wait` statement
With `wait`, you can add timeouts to your workflow. The usage is very simple:
```
wait 0.5
```
This code will wait for half a second and then will continue the workflow.

## The `do` statement
Using `do`, you can do everything you like in your Scrypt. `do` will execute a line of python code. Plenty of examples are listed below.
```
do import requests
```
```
do print("Hello World!")
```
```
do sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```

## The `set` statement
This will be added soon. Not available now.

## Spice ups
### Comments
Using comments, you can give instructions to your team members or to viewers on GitHub, etc.
You can also use it to list some information about the project, like your name.
You can take use of them with two slashes in a line, e.g:
```
// This will not be interpreted by the language.
// Author: NoahOnFyre
```