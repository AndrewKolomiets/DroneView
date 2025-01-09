import argparse
 
# Define a custom argument type for a list of strings
#def list_of_strings2(arg):
#    return arg
#    return arg.split(',')
 
# Create an ArgumentParser object
parser = argparse.ArgumentParser()
 
# Add an argument for the list of strings
parser.add_argument('--str-list2', type=str)
 
# Parse the command-line arguments
args = parser.parse_args()
 
# Use the list of strings in your script
print(args.str_list2)