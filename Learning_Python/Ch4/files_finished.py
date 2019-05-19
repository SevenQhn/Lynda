#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open the file back up and read the contents
  f = open("textfile.txt","r")

  fl = f.readlines()
  for x in fl:
      print (x)

if __name__ == "__main__":
  main()
