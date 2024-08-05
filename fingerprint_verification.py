######################################################################
# Names of any others you worked with:
# AI transcript if used:
# Any extensions done:
######################################################################

def read_print(filename):
    """Reads the given print and returns a dictionary with all info."""
    # Your turn!
    fingerprint_data = {}
    with open(data) as fh:
        for line in fh: 
            #grab first line as name, second line as width, third line height, line 9 on as fingerprint
            name, username = line.strip()
            fingerprint_data[name] = username
            width, fingerprint_width = line[1].strip()
            fingerprint_data[width] = fingerprint_width
            height, fingerprint_height = line[2].strip()
            fingerprint_data[height] = fingerprint_height
    print(fingerprint_data)
    return fingerprint_data




if __name__ == '__main__':
    # Just to get you started
    data = read_print("./prints/User1_Original.txt")
    print(data)

    # Add anything else you need for testing down here as you go!
