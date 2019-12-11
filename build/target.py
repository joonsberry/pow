# Project: PoW Target Generation Module
# Author: Jonathan Kenney

# imports
from sys import argv

# main program
def main():

  # get difficulty from CLI input
  d = int(argv[1])

  # init vars
  target_string = ''
  i = 0

  # create target value and then convert to bytes
  while i < 256:

    target_string += '0' if i < d else '1'
    i += 1

  target_int = int(target_string, 2)
  target_bytes = target_int.to_bytes((target_int.bit_length() + 7) // 8, 'big')
  
  # convert to hex to write out value
  target_hex = target_bytes.hex()

  # write out target to terminal and save
  print('Target: %s' % target_hex)
  with open('./data/target.txt', 'w') as f:
    f.write(target_hex)
    f.close()

# main boilerplate
if __name__ == '__main__':
  main()