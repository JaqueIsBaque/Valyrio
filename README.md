# Valyrio

Valyrio is both a variable- and a stack-based language. Each program is prefixed with a letter that determines the mode and the symbol ` ∫ ` to tell the program it is the tag

There are 4 different modes in Valyrio

    d   Debugging:  Rather than running the code, it finds any errors and prints them
    e   Executing:  Runs the code while ignoring any errors
    f   Full mode:  Runs the code, then outputs any errors found
    s   StackMode:  Converts to stack mode. Numbers and characters enclosed in " marks are parsed separately. 
                    Otherwise each character does a different command. If the letter isn't implemented as a command,
                    it raises an error.
                    
The code must follow this template, otherwise a SyntaxError is raised: `mode ∫ main [ code ]`
At the moment the code is run by entering the below code into the command line

    $ Valyrio 1 <file-name>
    
The `1` tells the code to use version 1, the only version currently runnable

###Comments

There are two different ways of doing comments that depend on the mode

    stack mode  : ‹Comment›         The › is needed to close the comment
    normal mode : ==> Comment       In this mode, the comment isn't needed to be closed

##Example programs

##Note: The majority of programs are easier to code in stack mode as its fully implemeted. It also has loops under development.
        However the execute modes don't have loops just yet and so find a lot of things difficult to code.

###Hello, World!

    s ∫ main [´Ø] ‹ Stack Mode › 
    
    e ∫ main [
    urnep("Hello, World!")  ==> Prints the string "Hello, World!"
    ]
    
###Prime Checker

    s ∫ main [Ïpo] ‹ Ï takes an integer input, p pushes its primality to the stack and o outputs the first item in the stack ›
    
###Quine

This is the shortest quine in stack mode

    s ∫ main [§]
    
###FizzBuzz

    s ∫ main [ÏF]
    
This takes an integer input and outputs that many iterations of FizzBuzz

OR

    s ∫ main [iF]
    
Takes an input, evaluates it and outputs FizzBuzz up to that number
