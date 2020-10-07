{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise\n",
    "\n",
    "1. Create a file with a `if __name__ == '__main__':` clause\n",
    "2. Use the `argparse` library to create an `ArgumentParser`\n",
    "3. Add the *positional* argument `name` that gives you a string\n",
    "4. Save that name into a string"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import argparse\n",
    "\n",
    "arg = 'Torben'\n",
    "\n",
    "def parse_name(name):\n",
    "    parser = argparse.ArgumentParser(description='A program that downloads a URL and stores it locally')\n",
    "    print(parser.parse_args(name))\n",
    "\n",
    "if __name__ == '__main__':    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
