## Exercise

#Implement a small download program, using `https://hackernews.com` as a test URL:

#1. Create a cli program to take 2 arguments: url (required) and destination_file (optional)
#2. Create a description of what the program does
#3. Implement the download part
#  * If no destination file was specified, save the file in `default_file.dat`
#4. Improve the code: if no destination file was specified, use the last subset of the URL as the name for the file
#5. Improve the code: if no destination file was specified, use the MIME-type of the HTTP header to guess the file extension

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Small download program')
    parser.add_argument('URL', help='The URL to process')
    parser.add_argument('--destination_file', default='default_file.dat', help='The name of the destination file')    

    print('URL:' + parser.parse_args().URL)
    print('Destination_file:' + parser.parse_args().destination_file)


