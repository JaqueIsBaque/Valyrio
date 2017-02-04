import sys
import interpreter_v1

'''
Usage

$ Valyrio 1 <file name>     Version 1
'''

def parse_cmd_line():
    args = sys.argv[1:]

    try:
        args[1]
    except:
        return 'E'

    mode = args[0]

    if mode == '1':
        interpreter = interpreter_v1
    else:
        return 'E'

    try:
        code = open(args[1]).read()
    except:
        return 'E'

    return code

if __name__ == '__main__':
    args = parse_cmd_line()
        
    if args == 'E':
        pass
    else:
        interpreter.Main(args).run()
