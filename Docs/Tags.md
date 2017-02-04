
### Code Golf Tag ###

Each command used uses a single byte.

E.g.

c ∫ main [
urnep("h")
]

Uses 8 bytes

c           Takes one byte
 ∫           Takes one byte
main [      Takes one byte
\n          Takes one byte
urnep("h")  Takes two bytes: urnep() and "h"
\n          Takes one byte
]           Takes one byte


################################################################################


### Debug Mode Tag ###

Rather than run the code, it tests it for errors

E.g.

d ∫ main [
hello
]

would output

"Line 1 produced Name Error: 'hello' is not defined"


################################################################################


### Execute Mode Tag ###

Tries to run the code, but if an error is produced it will ignore it

E.g.

e ∫ main [
urnep("h")
]

outputs

"Hello, World!"

as h is a built-in variable that contains the string "Hello, World!"

urnep() will test to see if the string contained is also a variable and will print is value if it is


################################################################################


### Full Mode Tag ###

Runs the code and outputs any errors found.
An optional c or s can be added to change the mode to
code golf or stack mode

E.g.

f ∫ main [
urnep("h")
hello
]

ouputs

"Hello, World!"
"Line 2 produced Name Error: 'hello' is not defined

E.g.

fc ∫ main [
urnep("h")
hello
]

does the same as above but in 9 bytes

################################################################################

### Stack Mode ###

Each symbol in the code does a different command
It works like any normal stack-based language

Symbols needed:

s tag at the start of the code
 ∫ splits code from tag
main [ stats the main code like any other mode

Newlines aren't allowed in the code

E.g.

s ∫ main [´Ø]

outputs "Hello, World!"

´ pushes "Hello, World!" to the stack
Ø ouputs the whole stack as ascii letters
] ends code block
