#Builtin commands in Stack Mode

This is a list of valid commands in Stack Mode in Vayrio

##Keywords

`!` pushes the boolean opposite of the top item on the stack

`=` pushes the boolean that the first item on the stack equals the second

`≠` pushes the boolean that the first item on the stack does not equal the second

##Math Operands

`∆` toggles the `all` command. If it is on, the following commands happen to all items in the stack.

`-+/*%<>` do all the normal commands. Divide pushes the floor division as Valyrio doesn't use floats

`^` is the exponent command

`±` pushes the top two items added and subtracted

`√` pushes the integer square root to the stack

`a` pushes the absolute value of the top item

`≤≥` are fairly obvious

`µ` converts to value to `x * 1000000`

`‰` divided value by 1000

`~` pushes the negative value of the first item to the stack

`S` pushes the sum of the range of the top of the first item in the stack

`l` pushes the `log x (y)` when `x` is the second value on the stack and `y` is the first

`t` pushes the `log 10 (x)` when `x` is the first value on the stack

`∑` pushes the sum of the whole stack

`R` pushes the range from 1 to the first item on the stack + 1

`x` pushes the product of the stack

`p` tests if the top item is prime or not

`f` pushes the factorial of the top of the stack

`P` pushes the prime range of the first item on the stack

##Base Conversions

The `all` command is still applicable for these commands

`u` converts to unary

`b` converts to binary

`t` converts to tenary

`å` converts to octary

`h` converts to hexadecimal

`B` converts the first item to the base of the second

##Number Commands

`π` pushes `pi` to the stack

`r` pushes a random number between 0 and the top of the stack to the stack

`∞` pushes infinite to the stack

`e` pushes e to the stack

`F` prints FizzBuzz up to the top number on the stack

`X` pushes 10 to the stack

`L` pushes 50 to the stack

`C` pushes 100 to the stack

`D` pushes 500 to the stack

`T` pushes 1000 to the stack

`Ω` pushes 1 million to the stack

##String Commands

`´` pushes `"Hello, World!"` to the stack

`ß` pushes the total of the `ord` value of `Valyrio`

##Stack Commands

`»` duplicates the top of the stack

`«` pops the top of the stack

`…` converts the stack to ascii characters

`Z` reverses the stack

`—` pushes the length of the stack

`s` sorts the stack

`J` makes the stack a set of itself

`m` pushes the minimum of the stack

`M` pushes the maximum of the stack

`c` clears the stack

`y` pushes a copy of the stack

##Input and Output

`o` outputs the first item on the stack

`O` outputs the whole stack

`ø` outputs the first item on the stack as a Unicode character

`Ø` outputs the whole of the stack as a Unicode interpretation

`Ó` outputs the first item as the uppercase equivilent of the Unicode character

`Ô` outputs the whole stack as Unicode characters in uppercase

`Ò` outputs the first item in lowercase

`` outputs the whole stack in lowercase

`I` takes input and pushes to the stack

`Í` takes input, converts to lower and pushes to stack

`Î` takes input, converts to upper and pushes to stack

`Ï` takes input, converts to an integer and pushes to stack

`i` takes input, evaluates it and pushes result to the stack

`w` outputs an error

`W` outputs a random error taken from a list of preset errors

`Æ` takes input and immediately outputs it

##Other Commands

`§` outputs `s ∫ main [§]`, making it a rudimentary quine program

`©` outputs the credits

`q` or `Q` quits

`v` or `V` outputs the Valyrio Help
