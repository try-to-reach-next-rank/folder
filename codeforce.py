import os,sys,math,bisect
from io import BytesIO, IOBase
from collections import Counter, deque
from itertools import permutations

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower())
MOD = int(1e9+7)

#region FastIO

BUFSIZE = 8192
  
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
  
  
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
  
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

#our code goes here
"""def readfile():
	infile = open('input.txt','r')
	outfile = open('output.txt','w')
	input = infile.readline
	print = outfile.write
readfile()"""
	
def solve():
	s = sorted(input())
	s = ''.join(s)
	l = list(set(permutations(s, len(s))))
	print(len(l))
	for i in range(len(l)):
		l[i] = ''.join(l[i])
	l.sort()
	for i in l:
		print(i)
	
if __name__ == "__main__":
	#for _ in range(int(input())):
	solve()