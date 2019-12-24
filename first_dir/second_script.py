import sys
import os
import first_script

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


first_script.print_blah()

print(sys.path)
print(BASE_DIR)
