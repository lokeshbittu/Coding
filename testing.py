
from Crypto.Util import number
import os

primenum = number.getPrime(8, os.urandom)

print(primenum)