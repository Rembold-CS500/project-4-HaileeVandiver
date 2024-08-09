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
        width = int(fh.readline().strip())
        height = int(fh.readline().strip())
        
        fingerprint_data['name'] = name
        fingerprint_data['width'] = width
        fingerprint_data['height'] = height

        fingerprint = [] 

        for line in fh:
            cleaned_line = line.strip()
            if cleaned_line:  # Only add the line if it's not empty
                fingerprint.append(cleaned_line.split())

        if not fingerprint:  # Check if the fingerprint list is empty
            print(f"Warning: No fingerprint data found in {filename}")
        else:
            fingerprint_data['fingerprint'] = fingerprint

    print(fingerprint_data)
    return fingerprint_data


def simple_check(fingerprint_data, another_fingerprint_data): 
    return fingerprint_data['fingerprint'] == another_fingerprint_data['fingerprint']
def variant_check(fingerprint_data, another_fingerprint_data):
    fingerprint = fingerprint_data['fingerprint']
    another_fingerprint = another_fingerprint_data['fingerprint']
    
    height = fingerprint_data['height']
    width = fingerprint_data['width']

    # Ensure both fingerprints have the same dimensions
    if height != another_fingerprint_data['height'] or width != another_fingerprint_data['width']:
        print("Fingerprints have different dimensions and cannot be compared.")
        return False

    matching_pixels = 0
    total_compared_pixels = 0
    
    for i in range(height):
        for j in range(width):
            total_compared_pixels += 1
            if fingerprint[i][j] == another_fingerprint[i][j]:
                matching_pixels += 1
    
    match_percentage = (matching_pixels / total_compared_pixels) * 100
    print(f"Matching percentage: {match_percentage:.2f}%")
    
    if match_percentage >= 95: 
        return True
    else: 
        return False

if __name__ == '__main__':
    # Example usage
    data = read_print("./prints/User1_Original.txt")
    data2 = read_print("./prints/User1_Variant1.txt")
    is_match = variant_check(data, data2)
    print("Match:" if is_match else "No Match")

