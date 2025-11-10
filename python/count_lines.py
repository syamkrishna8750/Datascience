filename =  input("Enter a file name: ")
with open(filename) as f:
    line_count = sum(1 for line in f)
print("number of lines:",line_count)