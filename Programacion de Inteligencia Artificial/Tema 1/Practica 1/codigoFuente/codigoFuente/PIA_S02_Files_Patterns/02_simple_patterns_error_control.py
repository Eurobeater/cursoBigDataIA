#!/usr/bin/python3

# Import module sys
import sys


def main():
    # Variable to store how many times the pattern was found
    occurrences = 0

    try:
        # Open the file whose name is specified in the first argument
        with open(sys.argv[1]) as f:
            for line in f:
                # The words of every line are stored as a list
                words = line.split()
                # Check for matches
                for w in words:
                    # The pattern to be found is specified in sys.argv[2]
                    if w == sys.argv[2]:
                        occurrences += 1 

        print("The word", sys.argv[2], "appeared",
              occurrences, "times in the file", sys.argv[1])
        f.close()
    except IndexError:
        print("Error! You need to provide the filepath and the pattern.")
        print("Sinopsis: python3 02_simple_patterns_error_control <file> <pattern>")


if __name__ == "__main__":
    main()
