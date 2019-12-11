# Project: PoW Solution Generation Module
# Author: Jonathan Kenney

# imports
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

# main program
def main():
  
  # init vars
  target = 0
  message = b''
  s = '0'.encode('utf-8') # start solution counter at '0'

  # fetch target from file and convert to integer
  with open('./data/target.txt', 'r') as f:
    target = int(f.read(), 16)
    f.close()

  # fetch message from file and encode
  with open('./data/input.txt', 'r') as f:
    message = f.read().encode('utf-8')
    f.close()

  # check the base hash value
  digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
  digest.update(message + s)

  # check if this digest has solved the puzzle
  solved = int(digest.finalize().hex(), 16) < target

  # loop and increment solution by 1 until puzzle is solved
  tries = 1
  while solved == False:

    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    tries += 1
    s = str(int(s.decode('utf-8')) + 1).encode('utf-8')
    digest.update(message + s)

    solved = int(digest.finalize().hex(), 16) < target

  # decode the solution
  s = s.decode()

  # print out the solution and number of tries, then write solution to file
  print('Solution: %s' % s)
  print('Num tries: %d' % tries)
  with open('./data/solution.txt', 'w') as f:
    f.write(s)
    f.close()

# main boilerplate
if __name__ == '__main__':
  main()