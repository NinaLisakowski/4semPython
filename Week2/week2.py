import argparse

#1. Create a python file with 3 functions:
#A. def print_file_content(file) that can print content of a csv file to the console
def print_file_content(file):
    """Print a csv files content to the console"""
    with open(file) as file_object:
        reader = csv.reader(file_object)
        for line in reader:
            print(str(line))
    

#B. def write_list_to_file(output_file, lst) that can take a list of tuple and write each element to a new line in file
#a. rewrite the function so that it gets an arbitrary number of strings instead of a list
def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as file_object:
        for element in lst:
            file_object.write(element + '\n')


        
#C.def read_csv(input_file) that take a csv file and read each row into a list
def read_csv(input_file):
    return_lst = []
    with open(input_file) as file_object:
        content = file_object.readlines()
        for line in content:
            return_lst.append(line)
        print(return_lst)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Week 2 Solution Handin - A program to read from an input file, and write it to an output file or the console')
    parser.add_argument('input_file', help='the chosen input files name')
    parser.add_argument('--file', help='the output files name')
    
    if parser.parse_args().file is None:
        print('INPUT:' + parser.parse_args().input_file)
    else:
        lines = read_csv(parser.parse_args().input_file)
        write_list_to_file(parser.parse_args().input_file, lines)
        print(lines)
    
    