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

        for line in filename:
            cleaned_line = line.rstrip()  # Keep trailing spaces but remove newlines
        # If the line is empty, create a row of spaces with the correct width
        if not cleaned_line:
            cleaned_line = ' ' * width
        fingerprint.append(cleaned_line)

        if not fingerprint:  # Check if the fingerprint list is empty
            print(f"Warning: No fingerprint data found in {filename}")
        else:
            fingerprint_data['fingerprint'] = fingerprint

    print(fingerprint_data)
    return fingerprint_data


def simple_check(fingerprint_data1, fingerprint_data2):
    """
    Compares the fingerprint portions of two fingerprint dictionaries.
    Returns True if the fingerprints are the same, otherwise False.
    """
    return fingerprint_data1['fingerprint'] == fingerprint_data2['fingerprint']

def variant_check(fingerprint_data1, fingerprint_data2):
    """
    Compares the fingerprint portions of two fingerprint dictionaries
    and calculates the percentage of matching pixels.
    Returns True if the matching percentage is 95% or higher, otherwise False.
    """
    fingerprint1 = fingerprint_data1['fingerprint']
    fingerprint2 = fingerprint_data2['fingerprint']

    matching_pixels = 0
    total_pixels = 0

    for i in range(len(fingerprint1)):
        for j in range(len(fingerprint1[i])):
            total_pixels += 1
            if fingerprint1[i][j] == fingerprint2[i][j]:
                matching_pixels += 1

    match_percentage = (matching_pixels / total_pixels) * 100
    print(f"Matching percentage: {match_percentage:.2f}%")

    return match_percentage >= 95

def shifted_check(fingerprint_data1, fingerprint_data2):
    """
    Compares the fingerprint portions of two fingerprint dictionaries
    with possible shifts and computes the best matching percentage.
    Returns True if the best matching percentage is 95% or higher, otherwise False.
    """
    fingerprint1 = fingerprint_data1['fingerprint']
    fingerprint2 = fingerprint_data2['fingerprint']
    height = len(fingerprint1)
    width = len(fingerprint1[0])
    max_shift = 5
    best_match_percentage = 0

    for vertical_shift in range(-max_shift, max_shift + 1):
        for horizontal_shift in range(-max_shift, max_shift + 1):
            matching_pixels = 0
            total_pixels = 0

            for i in range(max(0, -vertical_shift), min(height, height - vertical_shift)):
                for j in range(max(0, -horizontal_shift), min(width, width - horizontal_shift)):
                    if fingerprint1[i][j] == fingerprint2[i + vertical_shift][j + horizontal_shift]:
                        matching_pixels += 1
                    total_pixels += 1

            if total_pixels > 0:
                match_percentage = (matching_pixels / total_pixels) * 100
                best_match_percentage = max(best_match_percentage, match_percentage)

    print(f"Best matching percentage: {best_match_percentage:.2f}%")

    return best_match_percentage >= 95


if __name__ == '__main__':
    # Read in two fingerprint files
    data1 = read_print("./prints/User1_Original.txt")
    data2 = read_print("./prints/User1_Variant1.txt")
    user_1_shifted_1 = read_print("./prints/User1_ShiftedVariant1.txt")  
    user_1_shifted_2 = read_print("./prints/User1_ShiftedVariant2.txt")

    print(shifted_check(data1, user_1_shifted_2))  # Test with a shifted variant

