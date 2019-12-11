# Project: PoW Solution Verification Module
# Author: Jonathan Kenney

# imports
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

# main program
def main():
  
  # init vars
  target = 0
  message = b''
  s = b''

  # fetch target from file and convert to integer
  with open('./data/target.txt', 'r') as f:
    target = int(f.read(), 16)
    f.close()

  # fetch message from file and encode
  with open('./data/input.txt', 'r') as f:
    message = f.read().encode('utf-8')
    f.close()

  # fetch solution from file and encode
  with open('./data/solution.txt', 'r') as f:
    s = f.read().encode('utf-8')
    f.close()

  # run the solution through the hash
  digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
  digest.update(message + s)
  proof = digest.finalize().hex()

  # verify the solution is correct
  verified = int(proof, 16) < target

  # if solution is correct, print 1, otherwise print 0
  if verified:
    print(1)
  else:
    print(0)

# main boilerplate
if __name__ == '__main__':
  main()