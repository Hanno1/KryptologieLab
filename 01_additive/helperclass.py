ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Quelle: https://de.wikipedia.org/wiki/Buchstabenhäufigkeit
TRUE_VALUES = [0.0652, 0.0189, 0.0306, 0.0508, 0.1740, 0.0166, 0.0301, 0.0476, 0.0755, 0.0027, 0.0121, 0.0344, 0.0253, 0.0978, 0.0251, 0.0067, 0.0002, 0.0700, 0.0727, 0.0615, 0.0435, 0.0067, 0.0189, 0.0003, 0.0004, 0.0113]

def read_file(input_file):
    """
    read a file line by line and return the content as a string
    """
    content = ""
    with open(input_file) as file:
        for line in file:
            content += line
    return content

def write_file(string, output_file):
    """
    write a string to a file
    """
    file = open(output_file, "w")
    file.write(string)
    file.close
    return 1

def get_text_length(content):
    """
    get length of a string
    """
    length = 0
    for char in content:
        length += 1 if char in ALPHABET else 0
    return length
