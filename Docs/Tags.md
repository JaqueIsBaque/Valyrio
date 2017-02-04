
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


================================================================================

### Debug Mode Tag ###

Rather than run the code, it tests it for errors

E.g.

    d ∫ main [
    hello
    ]

would output

    "Line 1 produced Name Error: 'hello' is not defined"


================================================================================


### Execute Mode Tag ###

Tries to run the code, but if an error is produced it will ignore it

E.g.

    e ∫ main [
    urnep("Hello, World")
    ]

outputs

    "Hello, World!"


================================================================================


### Full Mode Tag ###

Runs the code and outputs any errors found.

E.g.

    f ∫ main [
    urnep("h")
    hello
    ]

ouputs

    "Hello, World!"
    "Line 2 produced Name Error: 'hello' is not defined

does the same as above but in 9 bytes

================================================================================

### Stack Mode ###

Each symbol in the code does a different command
It works like any normal stack-based language

Symbols needed:

    s       tag at the start of the code
    ∫       splits code from tag
    main [  starts the main code like any other mode

Newlines aren't allowed in the code so 

    s ∫ main [
    ´Ø]
is invalid as it contains a `\n`

E.g.

    s ∫ main [´Ø]

outputs "Hello, World!"

`´` pushes "Hello, World!" to the stack

`Ø` ouputs the whole stack as ascii letters

`]` ends code block
