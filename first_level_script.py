import sys
import os
from first_dir.first_script import print_blah

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print_blah()

print(sys.path)
print(BASE_DIR)