import sys
import math
import random

class Stack(list):

    def __init__(self,*values):
        self.push(*values)

    def push(self,*values,unpack=True):
        for i in values:
            if isinstance(i,str):
                if unpack:
                    if len(i) != 1:
                        if len(self) == 0:
                            self.append(ord(i[0]))
                        else:
                            self.insert(0,ord(i[0]))
                        for j in i[1:]:
                            self.insert(0,ord(j))
                    else:
                        self.insert(0,ord(i))
                else:
                    self.insert(0,i)
                    
            elif i in [math.inf,math.pi,math.e]:
                self.insert(0,i)
                
            else:
                self.insert(0,int(i))

    def __repr__(self):
        return ' '.join(list(map(str,reversed(self))))

stack = Stack()
apply = True

def ApplyAll():
    global apply
    apply = not apply

ApplyAll()

def Not():
    if apply:
        for i in range(len(stack)):
            stack[i] = not stack[i]
    else:
        stack[0] = not stack[0]

def Is():
    stack.push(stack[0] == stack[1])

def NotEqual():
    stack.push(stack[0] != stack[1])

''' Math Operands '''

def _Operand(oper):
    exec('''
if apply:
    x = stack[0]
    for i in range(len(stack)):
        stack[i] {0}= x
else:
    stack.push(stack[0] {0} stack[1])'''.format(oper))

def Minus():
    _Operand('-')

def Add():
    _Operand('+')

def Divide():
    _Operand('//')

def Times():
    _Operand('*')

def Modulo():
    _Operand('%')

def Exponent():
    _Operand('**')

def PlusMinus():
    stack.push(stack[0]+stack[1],stack[0]-stack[1])

def Sqrt():
    stack.push(int(math.sqrt(stack[0])))

def Abs():
    stack.push(abs(stack[0]))

def Less():
    stack.push(stack[0] < stack[1])

def Greater():
    stack.push(stack[0] > stack[1])

def LessEqual():
    stack.push(stack[0] <= stack[1])

def GreaterEqual():
    stack.push(stack[0] >= stack[1])

def ConvertMillion():
    if apply:
        for i in range(len(stack)):
            stack[i] *= 1000000
    else:
        stack.push(stack[0] * 1000000)

def DivThousand():
    if apply:
        for i in range(len(stack)):
            stack[i] //= 1000
    else:
        stack.push(stack[0] // 1000)

def Negative():
    if apply:
        for i in range(len(stack)):
            stack[i] = -stack[i]
    else:
        stack.push(-stack[0])

def SumRange():
    stack.push(sum(range(1,stack[0]+1)))

def Log():
    stack.push(int(math.log(stack[0],stack[1])))

def LogTen():
    stack.push(int(math.log10(stack[0])))

def Sum():
    stack.push(sum(stack))

def Range():
    stack.push(*range(1,stack[0]+1))

def Product():
    x = 0
    for i in stack:
        x *= i
    stack.push(x)

def IsPrime():
    x = stack[0]
    if x in [0,1]:
        var = True
    for i in range(2,x):
        if x % i == 0:
            var = True
    else:
        var = False
    stack.push(var)

def _IsPrime(x):
    if x in [0,1]:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

def Factorial():
    stack.push(math.factorial(stack[0]))

def PrimeRange():
    stack.push(*list(filter(_IsPrime,range(stack[0]))))

''' Base Conversions '''

def _Unary(x):
    return '..'+'1'*x

def _Base(x,b):
    base = b
    letters = '0123456789ABCDEF'
    num = x ; del x
    if num > base:
        y = num%base
        x = num//base
        L = [x,y]
        final = ''
        for power in range(num):
            if base**power > num:
                break
        for j in range(power-1):
            while L[j] > base:
                L.insert(1,L[j]%base)
                L[j] //= base
        for l in L:
            final += letters[l]
    else:
        final = letters[num]
    return '..'+final

def _Tenary(x):
    return _Base(x,3)

def _Convert(base):
    exec('''
if apply:
    for i in range(len(stack)):
        stack[i] = {0}(stack[i])[2:]
else:
    stack.push({0}(stack[0])[2:],unpack=False)'''.format(base))

def Unary():
    _Convert('_Unary')

def Binary():
    _Convert('bin')

def Tenary():
    _Convert('_Tenary')

def Oct():
    _Convert('oct')

def Hex():
    _Convert('hex')

def Base():
    if apply:
        for i in range(len(stack)):
            stack[i] = _Base(stack[i],stack[0])
    else:
        stack[0] = _Base(stack[0],stack[1])

''' Number Commands '''

def PushPi():
    stack.push(math.pi)

def Random():
    stack.push(random.randint(stack[0],stack[1]))

def Infinite():
    stack.push(math.inf)

def PushE():
    stack.push(math.e)

def FizzBuzz():
    for i in range(1,stack.pop(0)+1):
        if i % 3 == 0 and i % 5 == 0:
            stack.push(*'FizzBuzz\n')
        elif i % 3 == 0:
            stack.push(*'Fizz\n')
        elif i % 5 == 0:
            stack.push(*'Buzz\n')
        else:
            stack.push(i)
        if len(stack) != 1:
            InOut.AsciiAllOut()
        else:
            InOut.AllOut()
        stack.clear()

def Push10():
    stack.push(10)

def Push50():
    stack.push(50)

def Push100():
    stack.push(100)

def Push500():
    stack.push(500)

def PushThou():
    stack.push(1000)

def PushMill():
    stack.push(1000000)

''' String Commands '''

def HelloWorld():
    stack.push("Hello, World!")
    
def Score():
    num = 0
    for i in 'Valyrio':
        num += ord(i)
    stack.push(num)

''' Stack Commands '''

def DuplicateTop():
    stack.push(stack[0])

def PopTop():
    stack.pop(0)

def ConvertAscii():
    if apply:
        for i in range(len(stack)):
            stack[i] = chr(stack[i])
    else:
        stack[0] = chr(stack[0])

def Reverse():
    data = list(stack)
    stack.clear()
    stack.push(*data)
    return stack

def Length():
    stack.push(len(stack))

def Sort():
    data = stack.copy()
    data.sort()
    stack.clear()
    stack.push(*data)

def Set():
    data = stack.copy()
    data = list(set(data))
    stack.clear()
    stack.push(*data)

def Min():
    stack.push(min(stack))

def Max():
    stack.push(max(stack))

def Clear():
    while stack:
        stack.pop()

def Copy():
    stack.push(*stack.copy())
    
def Credits():
    print('''Credits Not Done''')

def Help():
    print('''Help Not Done''')

class InOut:

    def SingleOut():
        print(str(stack).split()[0])

    def AllOut():
        print(str(stack))

    def AsciiSingleOut():
        print(chr(int(str(stack).split()[0])))
            
    def AsciiAllOut():
        for s in str(stack).split():
            print(chr(int(s)),end='')

    def AsciiSingleUpperOut():
        print(chr(int(str(stack).split()[0])).upper())

    def AsciiAllUpperOut():
        for s in str(stack).split():
            print(chr(int(s)).upper(),end='')

    def AsciiSingleLowerOut():
        print(chr(int(str(stack).split()[0])).lower())

    def AsciiAllLowerOut():
        for s in str(stack).split():
            print(chr(int(s)).lower(),end='')

    def In():
        stack.push(input())

    def InLower():
        stack.push(input().lower())

    def InUpper():
        stack.push(input().upper())

    def InInt():
        stack.push(int(input()))

    def InNoSpace():
        stack.push(''.join(input().split()))

    def Err():
        print('Exited with status 1',file=sys.stderr)

    def RandomErr():
        Errors = ['Syntax Error','Name Error','Trump Error','String Error',
                  'Python Error','Stack Error','Valyrio Error','Quitting.']
        print(random.choice(Errors),file=sys.stderr)
    
    def OutputInput():
        print(input())

