import sys
import Version_1_3

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
        interpreter = Version_1_3
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
