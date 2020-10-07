## Exercise

#1. Create a file with a `if __name__ == '__main__':` clause
#2. Use the `argparse` library to create an `ArgumentParser`
#3. Add the positional argument `name` that gives you a string
#4. Save that name into a string
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parses name to string')
    parser.add_argument('name', help='The name to parse')

    print(str(parser.parse_args()))




