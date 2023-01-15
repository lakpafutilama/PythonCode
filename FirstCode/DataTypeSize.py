import sys
import math
print(f"""
Size of integer = {sys.getsizeof(1)}
Size of floating-point number = {sys.getsizeof(1.1)}
Size of complex = {sys.getsizeof(math.sqrt(1))}
Size of list = {sys.getsizeof([1])}
Size of set = {sys.getsizeof({1})}
Size of String = {sys.getsizeof("1")}
""")