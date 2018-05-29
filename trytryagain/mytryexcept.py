#!/usr/bin/env python3
# mytryexcept.py
# Micah Raabe

# Lab 40 - Try and Except 02

print('  1 - StopIteration')
print('  2 - ArithmeticError')
print('  3 - AssertionError')
print('  4 - AttributeError')
print('  5 - EOFError')
print('  6 - ImportError')
print('  7 - KeyboardInterrupt')
print('  8 - LookupError')
print('  9 - IndexError')
print(' 10 - KeyError')
print(' 11 - SyntaxError')
print(' 12 - IndentationError')
print(' 13 - SystemError')

userinput = input('Enter a number: ')

try: # code we want to try to run goes under the try
    print("This is what we try to do, but we can raise an error...")
    if int(userinput) == 1:
        raise StopIteration
    if int(userinput) == 2:
        raise ArithmeticError
    if int(userinput) == 3:
        raise AssertionError
    if int(userinput) == 4:
        raise AttributeError
    if int(userinput) == 5:
        raise EOFError
    if int(userinput) == 6:
        raise ImportError
    if int(userinput) == 7:
        raise KeyboardInterrupt
    if int(userinput) == 8:
        raise LookupError
    if int(userinput) == 9:
        raise IndexError
    if int(userinput) == 10:
        raise KeyError
    if int(userinput) == 11:
        raise SyntaxError
    if int(userinput) == 12:
        raise IndentationError
    if int(userinput) == 13:
        raise SystemError
except StopIteration:  # Only catches div by zero errors
    print("This code raised an Stop Iteration Error")
except ArithmeticError:
    print("This code raised an Arithmetic Error")
except AssertionError:
    print("This code raised an Assertion Error")
except AttributeError:
    print("This code raised an Attribute Error")
except EOFError:
    print("This code raised an EOF Error")
except ImportError:
    print("This code raised an Import Error")
except KeyboardInterrupt:
    print("This code raised an Keyboard Interrupt Error")
except LookupError:
    print("This code raised an Lookup Error")
except IndexError:
    print("This code raised an Index Error")
except KeyError:
    print("This code raised an Key Error")
except SyntaxError:
    print("This code raised an Syntax Error")
except IndentationError:
    print("This code raised an Indentation Error")
except SystemError:
    print("This code raised an System Error")
except:
    print("We're sorry, something unexpected happened. See your IT department.")
