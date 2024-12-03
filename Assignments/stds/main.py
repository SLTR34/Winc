# Do not modify these lines
__winc_id__ = "8c2e6882503c4baa9ce2e050497c3f2f"
__human_name__ = "stds"

# Add your code after this line

import sys
import io

def main():
    # TODO: read text from stdin
    input_string = sys.stdin.read()
    
    # TODO: Filter character given as an argument from the text
    variables = input_string.split()
    result = input_string.replace(variables[0], "")

    # TODO: Print the result to stdout
    sys.stdout.write(result)

    # TODO: Print the total number of removed characters to stderr
    number_of_removed_characters = len(input_string) - len(result)  
    sys.stderr.write(str(number_of_removed_characters))


if __name__ == "__main__":
    main()
