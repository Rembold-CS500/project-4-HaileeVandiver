######################################################################
# Names of any others you worked with:
# AI transcript if used:
# Any extensions done:
######################################################################

def read_print(filename):
    """Reads the given print and returns a dictionary with all info."""
    fingerprint_data = {}
    with open(filename) as fh:
        name = fh.readline().strip()
        width = fh.readline().strip()
        height = fh.readline().strip()
        
        fingerprint_data['name'] = name
        fingerprint_data['width'] = width
        fingerprint_data['height'] = height

        fingerprint = [] 

        for line in fh: 
            fingerprint.append(line.strip().split())
    fingerprint_data['fingerprint'] = fingerprint

    print(fingerprint_data)
    return fingerprint_data

def simple_check(fingerprint_data, another_fingerprint_data): 
    return fingerprint_data['fingerprint'] == another_fingerprint_data['fingerprint']

def variant_check(fingerprint, another_fingerprint):
    #compute the percentage of the matching pixels by dividing that count by the total number of compared pixels and multiplying by 100.
    #compare every character of the two fingerprint arrays 
    matching_pixels = 0
    total_compared_pixels = (len(fingerprint))
    for i in range(len(fingerprint[i])): 
        for j in range(len(fingerprint[i])):
            if fingerprint[i][j] == another_fingerprint[i][j]:
                matching_pixels += matching_pixels
    
    if (matching_pixels / total_compared_pixels) * 100 >= 95: 
        print("These fingerprints are a match")
        return True
    else: 
        print("These fingerprints are not a match")
        return False



if __name__ == '__main__':
    # Just to get you started
    data = read_print("./prints/User1_Original.txt")
    print(data)

    # Add anything else you need for testing down here as you go!
