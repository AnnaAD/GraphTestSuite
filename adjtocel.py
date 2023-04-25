import sys

with open(sys.argv[2], 'w') as the_file:  
    with open(sys.argv[1], 'r') as my_file:
        for line in my_file:
            items = line.strip().split(" ")
            for i in items[2:]:
                the_file.write(items[0] + " " + i + "\n")
