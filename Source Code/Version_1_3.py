import sys              #For stdout, -in and -err
import string as chars  #Change to chars so that var name string can be used
import math             #For global constants
import stack            #For stack mode

Globals = {'pi':math.pi,'e':math.e,'h':"Hello, World!"} #Define global variables
looped = 0                                              #Define the number of iters in a for loop
__version__ = '1.3'                                     #Version: 1.3

''' Define types '''

''' Define types that cannot be called'''

class _Qurdon: #Define the class containing the list methods

    def __init__(self):
        self.list = list()

    def mazmori(self,x): #append
        self.list += [x]

    def doru(self):
        self.list = []

    def arlise(self,t): #extend
        for i in t:
            self.list.append(i)

    def dinag(self,i,x): #insert
        l = []
        for j in range(len(self.list)):
            if j == i:
                l.append(x)
            l.append(self.list[j])
        self.list = l

    def bemag(self,joiner): #join
        joiner = str(joiner)
        string = ''
        for i in self.list:
            string += str(i) + joiner
        if joiner: return string[:-len(joiner)]
        else: return string

    def guro(self,i=None): #pop
        if i is None:
            s = self.list[-1]
            self.list = self.list[:-1]
            return s
        args = []
        for a in range(len(self.list)):
            if a != i:
                args.append(self.list[a])
            else:
                popped = self.list[i]
        self.list = args
        return popped

    def nadi(self,x): #remove
        args = []
        for arg in self.list:
            if arg == x:
                continue
            else:
                args.append(arg)
        self.list = args

    def qog(self,reverse=False): #sort
        self.list = sorted(self.list,reverse=reverse)

class _Udra: #Define the class containing the string methods

    def __init__(self):
        self.str = ''

    def ilagsebe(self): #capitalize
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        try:
            final = upper[lower.index(self.str[0])]
        except:
            final = self.str[0]
        for c in self.str[1:]:
            try:
                final += lower[upper.index(c)]
            except:
                final += c
        return final

    def unag(self,counting,start=0,end=None): #count
        if end == None: end = len(self.str)
        string = self.str[start:end]
        number = 0
        for char in string:
            if char == counting:
                number += 1
        return number

    def morileda(self,suffix,start=0,end=None): #endswith
        if end == None: end = len(self.str)
        string = self.str[start:end]
        for i in range(len(suffix)):
            if string[-(i+1)] != suffix[-(i+1)]:
                return False
        return True

    def jurnag(self,x,start=0,end=None): #find
        if end == None: end = len(self.str)
        for i in range(start,end):
            if self.str[i] == x:
                return i+1
        raise AttributeError('No such value in string')

    def iamere(self): #isalnum
        values = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        for char in self.str:
            if char not in values:
                return False
        return True

    def ia(self): #isalpha
        values = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for char in self.str:
            if char not in values:
                return False
        return True

    def mere(self): #isdigit
        values = '1234567890'
        for char in self.str:
            if char not in values:
                return False
        return True

    def sagilag(self): #islower
        values = 'abcdefghijklmnopqrstuvwxyz'
        for char in self.str:
            if char not in values and char in string.ascii_letters:
                return False
        return True

    def sagbe(self): #isupper
        values = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for char in self.str:
            if char not in values and char in string.ascii_letters:
                return False
        return True

    def ilag(self): #lower
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        String = ''
        for char in self.str:
            try:
                String += lower[upper.index(char)]
            except:
                String += char
        return String

    def arlin(self,old,new): #replace
        s = self.str
        Lnew = []
        final = []
        while s:
            Lnew.append(s[:len(old)])
            s = s[len(old):]
        for char in Lnew:
            if char == old:
                final.append(new)
            else:
                final.append(char)
        return ''.join(final)

    def pryjag(self,char=' '): #split
        string = self.str
        List = []
        temp = ''
        for c in string:
            if c in char:
                if temp:
                    List.append(temp)
                temp = ''
            else:
                temp += c
        if temp:
            List.append(temp)
        split = qurdon()
        for i in List:
            split.mazmori(i)
        return split

    def rhaenleda(self,prefix,start=0,end=None): #startswith
        if end == None: end = len(self.str)
        String = self.str[start:end]
        for i in range(len(prefix)):
            if String[i] != prefix[i]:
                return False
        return True

    def nadin(self,char=' \t\n'): #strip
        String = ''
        for ch in self.str:
            if ch not in char:
                String += ch
        return String
            
    def arlibe(self): #swapcase
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        String = ''
        for char in self.str:
            if char in upper:
                String += lower[upper.index(char)]
            elif char in lower:
                String += upper[lower.index(char)]
            else:
                String += char
        return String

    def eli(self): #title
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        x = self.str.split(' ')
        final = []
        for i in x:
            temp = ''
            if i[0] not in upper:
                if i[0] in lower:
                    temp = upper[lower.index(i[0])]
            else:
                temp = i[0]
            for char in i[1:]:
                if char in upper:
                    if char not in lower:
                        char = lower[upper.index(char)]
                temp += char
            final.append(temp)
        return ' '.join(final)

    def be(self): #upper
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        String = ''
        for char in self.str:
            try:
                String += upper[lower.index(char)]
            except:
                String += char
        return String

''' Int types '''

class Int: #Class for integers, contains no methods
    
    def __init__(self,x):
        self.x = int(x)
        
    def __add__(self,y): #Math operands automatically change the value e.g x := 5 ; x + 6 ; x = 11
        self.x += y
        
    def __sub__(self,y):
        self.x -= y
        
    def __mul__(self,y):
        self.x *= y
        
    def __truediv__(self,y): #Valyrio doesn't handle floats
        self.x //= y
        
    def __mod__(self,y):
        self.x %= y
        
    def __repr__(self):
        return str(self.x)
    
    def __iter__(self): #Ints are iterable, returning the range 1,x+1
        for i in range(self.x):
            yield i+1
            
    def __abs__(self):
        return self.x if self.x >= 0 else -self.x
    
    def __len__(self): #Ints have a length, equivilent to the number of digits in the number 
        length = 0
        for i in str(self.x):
            length += 1
        return length
        
class Hex(Int):
    
    def __init__(self,x,main=hex):
        x = int(x)
        self.main = main
        self.x = self.main(x)[2:]
        self.normal = x
        
    def __add__(self,y):
        self.normal += y
        self.x = self.main(self.normal)[2:]
        
    def __sub__(self,y):
        self.normal -= y
        self.x = self.main(self.normal)[2:]
        
    def __mul__(self,y):
        self.normal *= y
        self.x = self.main(self.normal)[2:]
        
    def __truediv__(self,y):
        self.normal //= y
        self.x = self.main(self.normal)[2:]
        
    def __mod__(self,y):
        self.normal %= y
        self.x = self.main(self.normal)[2:]

class Bool(Int):
    
    def __init__(self,x):
        self.x = 1 if x else 0

class Oct(Hex):
    
    def __init__(self,x):
        super().__init__(x,main=oct)

''' Iterables '''

''' Inherit builtin functions from a separate file '''

class List(_Qurdon):
    
    def __init__(self,*args):
        self.list = [arg for arg in args]
        
    def __mul__(self,x):
        data = self.list.copy()
        temp = self.list.copy()
        for i in range(x):
            data.append(temp)
        return data
            
    def __repr__(self):
        return str(self.list).replace('[','|').replace(']','|')
    
    def __len__(self):
        length = 0
        for i in self.list:
            length += 1
        return length
    
    def __getitem__(self,y):
        return self.list[y]
        
    def __contains__(self,y):
        for l in self.list:
            if l == y:
                return 1
        return 0
    
    def __iter__(self):
        for i in self.list:
            yield i

class Str(_Udra):
    
    def __init__(self,string=''):
        self.str = "{}".format(string)
        
    def __mul__(self,y):
        return self.str * y
            
    def __add__(self,x):
        return self.str + x
        
    def __getitem__(self,x):
        return self.str[x]

    def __repr__(self):
        return '"'+str(self.str)+'"'

    def __contains__(self,y):
        return int(all([1 for i in self.str if i==val])) if bool([1 for i in self.str if i==val]) else 0 # Stupid version so I don't forget it

    def __iter__(self):
        for i in self.str:
            yield i

    def arli(self,*args):
        string = ""
        for a in range(len(args)):
            string = self.str.replace('`{}`'.format(a),args[a])
        return string

''' Define bultin functions '''

def Max(iterable):
    return max(iterable)

def Min(iterable):
    return min(iterable)

def Len(obj):
    return obj.__len__()

def Exec(string):
    Main(string).run()

def Input(prompt=''):
    stdin = ''
    ln = input(prompt)
    while ln:
        stdin += ln
        ln = input()
    return eval(stdin)

def Range(start=0,end=0,step=1):
    return List(*list(range(start,end,step)))

def Quit(code=None):
    quit(code)

def Sorted(iterable):
    return sorted(iterable)

def Print(value,delim='\n',display=sys.stdout):
    if value in Globals:
        value = Globals[value]
    print(value,end=delim,file=display)

''' Define single char operands '''

def Greater(x,y):
    if x in Globals.keys():
        x = Globals[x]
    if y in Globals.keys():
        y = Globals[y]
    return int(x.__gt__(y))

def Less(x,y):
    if x in Globals.keys():
        x = Globals[x]
    if y in Globals.keys():
        y = Globals[y]
    return int(x.__lt__(y))

def Exponent(x,y):
    if x in Globals.keys():
        x = Globals[x]
    if y in Globals.keys():
        y = Globals[y]
    return x ** y

def Add(x,y):
    if x in Globals.keys():
        x = Globals[x]
    if y in Globals.keys():
        y = Globals[y]
    return x + y

def Minus(x,y):
    if x in Globals.keys():
        x = Globals[x]
    if y in Globals.keys():
        y = Globals[y]
    return x - y

def Times(x,y):
    if x in Globals.keys():
        x = Globals[x]
    if y in Globals.keys():
        y = Globals[y]
    return x * y

def Divide(x,y):
    if x in Globals.keys():
        x = Globals[x]
    if y in Globals.keys():
        y = Globals[y]
    return x // y

def Modulo(x,y):
    if x in Globals.keys():
        x = Globals[x]
    if y in Globals.keys():
        y = Globals[y]
    return x % y

def Equals(x,y):
    if x in Globals.keys():
        x = Globals[x]
    if y in Globals.keys():
        y = Globals[y]
    return int(x == y)

def Not(x):
    if x in Globals.keys():
        x = Globals[x]
    if y in Globals.keys():
        y = Globals[y]
    return not bool(x)

def Negative(x):
    return -x

def In(val,iterable):
    return iterable.__contains__(val)

def GetIndex(obj,index):
    return obj.__getitem__(index)

def SwapVar(x,y):
    Globals[x] , Globals[y] = Globals[y] , Globals[x]

''' Define keywords '''

def Import(module):
    return __import__(str(module))

def Or(*bools):
    for b in bools:
        if b:
            return True
    return False

def If(boolean,func,args=None,Else=None,eargs=None):
    if boolean:
        if args is None:
            try:
                func()
            except:
                pass
        else:
            try:
                func(*args)
            except TypeError:
                func(args)
            except:
                pass
    else:
        if Else is None:
            pass
        else:
            if args is None:
                try:
                    Else()
                except:
                    pass
            else:
                try:
                    Else(*eargs)
                except TypeError:
                    Else(eargs)
                except:
                    pass
                

def And(*bools):
    for b in bools:
        if not b:
            return False
    return True

def Delete(var):
    Globals.pop(var)

def For(iters,func,args=None):
    if iters in Globals:
        iters = Globals[iters]
    global looped
    if iters == looped:
        looped = 0
        return
    if args is None:
        try:
            func()
        except:
            pass
    else:
        try:
            func(*args)
        except TypeError:
            func(args)
        except:
            pass
    looped += 1
    For(iters,func,args)

TYPES = {
    
    'ampa':(Int,1),
    'byre':(Hex,1),
    'doru':(Bool,1),
    'jenqa':(Oct,1),
    'qurdon':(List,-1),
    'udra':(Str,1),

}

BUILTINS = {
    
    'be':(Max,1),
    'ilag':(Min,1),
    'bosa':(Len,1),
    'dako':(Exec,1),
    'epag':(Input,1),
    'jior':(GetIndex,2),
    'mazigon':(Range,3),
    'henu':(Quit,0),                      
    'qogare':(Sorted,1),
    'sagon':(SwapVar,2),
    'urnep':(Print,3),

}
    
OPERANDS = {
    
    '>':(Greater,2),
    '<':(Less,2),
    '^':(Exponent,2),
    '+':(Add,-1),
    '-':(Minus,-1),
    '*':(Times,-1),
    '/':(Divide,2),
    '%':(Modulo,2),
    '=':(Equals,2),
    '~':(Negative,1),

    ':':('=',2),

}
    
KEYWORDS = {

    'daor':(Not,1),
    'dereb':(Import,1),
    'ia':(Or,-1),
    'isse':(In,2),
    'lo':(If,3),
    'nadi':(Delete,-1),
    'se':(And,-1),
    'syt':(For,3),

}

STACKCOMMANDS = {

    # Keywords

    '!':stack.Not, 
    '=':stack.Is,
    '≠':stack.NotEqual,

    # Math Operands
    
    '-':stack.Minus,
    '+':stack.Add,
    '/':stack.Divide,
    '*':stack.Times,
    
    '%':stack.Modulo,
    '^':stack.Exponent,
    '±':stack.PlusMinus,
    '√':stack.Sqrt,
    'a':stack.Abs,
    
    '<':stack.Less,
    '>':stack.Greater,
    '≤':stack.LessEqual,
    '≥':stack.GreaterEqual,
    
    'µ':stack.ConvertMillion,
    '‰':stack.DivThousand,
    '~':stack.Negative,
    'S':stack.SumRange,
    'l':stack.Log,
    't':stack.LogTen,

    '∑':stack.Sum,
    'R':stack.Range,
    'x':stack.Product,
    'p':stack.IsPrime,
    'f':stack.Factorial,
    'P':stack.PrimeRange,

    # Base Convertions

    'u':stack.Unary,
    'b':stack.Binary,
    't':stack.Tenary,
    'å':stack.Oct,
    'h':stack.Hex,
    'B':stack.Base,

    # Number Commands
    
    'π':stack.PushPi,
    'r':stack.Random,
    '∞':stack.Infinite,
    'e':stack.PushE,
    'F':stack.FizzBuzz,
    
    'X':stack.Push10,
    'L':stack.Push50,
    'C':stack.Push100,
    'D':stack.Push500,
    'T':stack.PushThou,
    'Ω':stack.PushMill,

    # String Commands
    
    '´':stack.HelloWorld,
    'ß':stack.ScoreLang,

    # Stack Commands
    
    '∆':stack.ApplyAll,
    '»':stack.DuplicateTop,
    '«':stack.PopTop,
    '…':stack.ConvertAscii,
    'Z':stack.Reverse,
    '–':stack.Length,
    's':stack.Sort,
    'J':stack.Set,
    'm':stack.Min,
    'M':stack.Max,
    'c':stack.Clear,
    'y':stack.Copy,

    # Others
    
    '©':stack.Credits,
    'q':quit,
    'Q':quit,
    'v':stack.Help,
    'V':stack.Help,

    # In and Output and Error
    
    'o':stack.InOut.SingleOut,
    'O':stack.InOut.AllOut,
    'ø':stack.InOut.AsciiSingleOut,
    'Ø':stack.InOut.AsciiAllOut,
    'Ó':stack.InOut.AsciiSingleUpperOut,
    'Ô':stack.InOut.AsciiAllUpperOut,
    'Ò':stack.InOut.AsciiSingleLowerOut,
    '':stack.InOut.AsciiAllLowerOut,
    
    'I':stack.InOut.In,
    'Í':stack.InOut.InLower,
    'Î':stack.InOut.InUpper,
    'Ï':stack.InOut.InInt,
    'i':stack.InOut.InNoSpace,

    'w':stack.InOut.Err,
    'W':stack.InOut.RandomErr,

    'Æ':stack.InOut.OutputInput,
}

tags = ['d',    # debug mode
        'e',    # execute code
        'f',    # full mode
        's',    # stack mode
        ]

def Main(text):
        
    tag = text.split('∫')[0].strip()
    text = text.split('∫')[1].strip()

    if tag == 's':
        return MainStack(text)
    
    return MainText(text,tag)
        

class MainStack:

    def __init__(self,text):

        if '\n' in text:
            raise SyntaxError('Invalid character: "\n"')

        self.text = text.split('main [')[1][:-1]

    def run(self,default=None):
        
        quine = False
        
        if default is not None:
            stack.stack.push(default)

        self.compiled = self.tokenize()
        
        for char in self.compiled:
            if isinstance(char,int):
                stack.stack.push(char)
            else:
                if len(char) != 1:
                    char = char[1:-1]
                    stack.stack.push(*char)
                elif char == '§':
                    quine = True
                else:
                    STACKCOMMANDS[char]()
        if quine:
            self.quine()

    def tokenize(self):
        
        nums = []
        final = []
        temp = ''
        instring = False
        parsed_strings = []
        parsed = []
        stringnum = 0
        
        for c in list(self.text):
            if c in '1234567890':
                temp += c
            else:
                if temp:
                    nums.append(temp)
                    temp = ''
                else:
                    nums.append(c)
                    
        if temp:
            nums.append(temp)
            
        for i in nums:
            if i and i != ' ':
                final.append(i)
                    
        indexes = list(MainStack.atIndex(''.join(final),'"'))
        commentStart = list(MainStack.atIndex(''.join(final),'‹'))
        commentEnd = list(MainStack.atIndex(''.join(final),'›'))

        if bool(commentStart) ^ bool(commentEnd):
            raise SyntaxError('Comments must be ended')

        if commentStart and commentEnd:

            commentrange = list(range(commentStart[0],commentEnd[0]+1))

            temp = []

            for i in range(len(final)):
                if i not in commentrange:
                    temp.append(final[i])
                    
            final = temp

        for i in range(0,len(indexes),2):
            parsed_strings.append(''.join(final[indexes[i:i+2][0]:indexes[i:i+2][1]+1]))

        for c in final:
            if c == '"':
                instring = not instring
                stringnum += 1
            if not instring:
                parsed.append(c)
            else:
                parsed.append(parsed_strings[stringnum//2])

        parsed = self.removeDuplicates(parsed)
        
        if '"' in parsed:
            parsed.remove('"')

        for i in range(len(parsed)):
            try:
                parsed[i] = int(parsed[i])
            except:
                pass
        
        return parsed
    
    def quine(self):
        print('s ∫ main ['+self.text+']')

    @staticmethod
    def atIndex(text,char):
        start = 0
        while True:
            start = text.find(char,start)
            if start == -1: return
            yield start
            start += 1

    @staticmethod
    def removeDuplicates(text):
        out = []
        for x in text:
            if x not in out:
                out.append(x)
        return out
        
class MainText:

    def __init__(self,text,tag):

        self.COMMENT = '==>'
        self.STRINGON = False
        self.errors = None

        self.text = text
        self.tag = tag

        if 's' in self.tag:
            raise SyntaxError('Wrong Tag')

        if self.tag not in tags:
            raise SyntaxError('No such tag as "{0}"'.format(self.tag))

    def __len__(self):
        return len(self.text)

    def compile(self):

        self.program = ''

        for line in self.text.split('\n'):

            line = self.translateLine(line)

            self.program += line + '\n'

        return 'Program compiled!'

    def run(self):

        if self.tag == 'd':
            raise SyntaxError
        
        self.errors = []
        self.programlines = self.program.split('\n')
        
        if self.programlines:

            if self.programlines[0] != 'main [':
                self.errors.append((0,'Syntax Error','Programs must start with main ['))

            for i in self.programlines:

                try:
                    exec(i)
                except Exception as e:
                    self.errors.append((self.programlines.index(i),e.__class__.__name__[:-5]+' '+e.__class__.__name__[-5:],e))
                finally:
                    pass

        template = '\n\n\nProgram run {0}successfully. {1} error{2} found.{3}'

        self.errors = self.errors[1:-1]

        if self.errors:
            template = template.format('un',len(self.errors),'s' if len(self.errors) != 1 else '',[' Do method.debug() to see any errors',''][self.tag == 'f'])
        else:
            template = template.format('',0,'s','')

        print(template)

        if self.tag == 'f':
            self.debug()

    def translateLine(self,line):
        
        line = line.split(self.COMMENT)[0].strip()

        nostring = string = ''

        for char in line:
            if char == '"':
                self.STRINGON = not self.STRINGON
            if not self.STRINGON:
                nostring += char
            else:
                string += char
                
        nostring = nostring.replace('"',chr(1000))
        string += '"'

        nostring , line = line , nostring
        
        for char in line:
            
            if char in OPERANDS:
                try:
                    line = line.replace(char,OPERANDS[char][0])
                except:
                    line = line.replace(char,OPERANDS[char][0].__name__+'(')
                    line = line.split('(')[0] + '(' + line.split('(')[1].strip().replace(' ',',') + ')'

            if char == '(':

                commands = line.split('(')[:-1]

                for c in range(len(commands)):
                    if commands[c] in BUILTINS:
                        line = line.replace(commands[c],BUILTINS[commands[c]][0].__name__)
                    if commands[c] in KEYWORDS:
                        line = line.replace(commands[c],KEYWORDS[commands[c]][0].__name__)

        line = line.replace(chr(1000),string)

        return line

    def debug(self):
        strerrs = ''
        if self.errors is None:
            print('Code must be run first!')
        if self.errors:
            for ln in self.errors:
                strerrs += 'Line {0} produced {1}: {2}\n'.format(ln[0],ln[1],ln[2])
            print(strerrs)
        else:
            print('No errors found!')
