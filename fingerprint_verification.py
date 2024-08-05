######################################################################
# Names of any others you worked with:
# AI transcript if used:
# Any extensions done:
######################################################################

def read_print(filename):
    """Reads the given print and returns a dictionary with all info."""
    # Your turn!
    fingerprint_data = {}
    with open(filename) as fh:
        lines = fh.readlines()
        # Initialize variables for each part of the data
        name = None
        width = None
        height = None
        fingerprint = []

    i = 1

    while i < len(lines): 
        #grab first line as name, second line as width, third line height, line 9 on as fingerprint
        name = lines[i].strip()
        width = lines[i+1].strip()
        height = lines[i+2].strip()
    print(fingerprint_data)
    return fingerprint_data




if __name__ == '__main__':
    # Just to get you started
    data = read_print("./prints/User1_Original.txt")
    print(data)

    # Add anything else you need for testing down here as you go!
