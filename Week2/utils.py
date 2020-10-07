import os

#1. first function takes a path to a folder and writes all filenames in the folder to a specified output file
def first_function(path, output_file):
    lst = os.listdir(path)
    with open(output_file, 'w') as f_object:
        for line in lst:
            f_object.write(line + "\n")

            
#2. second takes a path to a folder and write all filenames recursively (files of all sub folders to)
def second_function(path, output_file):
    directory = os.walk(path)
    with open(output_file, "w") as f_object:
        for root, dirs, files in directory:
            for filename in files:
                print(os.path.join(root, filename))
                f_object.write("%s\n" % os.path.join(root, filename))
    

#3. third takes a list of filenames and print the first line of each
def third_function(lst):
    for file in lst:
        with open(file,'r') as f_object:
            print(file + "'s first line: " + f_object.readlines()[0])
    

#4. fourth takes a list of filenames and print each line that contains an email (just look for @)
def fourth_function(lst):
    for file in lst:
        with open(file,'r') as f_object:
            for line in f_object.readlines():
                if "@" in line:
                    print("File: " + file + "\n" + line)

                    
#5. fifth takes a list of md files and writes all headlines (lines starting with #) to a file Make sure your module can be called both from cli and imported to another module Create a new module that imports utils.py and test each function.                    
def fifth_function(lst, output_file):
    lines_to_output = []
    for file in lst:
        with open(file,'r') as f_object:
            for line in f_object.readlines():
                if line[0] == "#":
                    lines_to_output.append(line);
        with open(output_file, 'w') as f_object:
            for line in lines_to_output:
                f_object.write(line)

