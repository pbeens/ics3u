import sys

print("8:", sys.getsizeof(8), "bytes")
print("8 with 21 zeros:", sys.getsizeof(8 * 10**21), "bytes")
print("3.2:", sys.getsizeof(3.2), "bytes")
print("'8':", sys.getsizeof("8"), "bytes")
print("'LAB-PC-14':", sys.getsizeof("LAB-PC-14"), "bytes")
