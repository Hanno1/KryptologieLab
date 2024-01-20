import helperclass as hc

# permutation used in the linear approximation
PERMUTATION = [1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]

def check_linear_approx(linear_approx):
    """
    check the linear approximation
    -> activity of the s-boxes have to be correct
    """
    for i in range(2):
        current_data = linear_approx[i]
        activity = get_next_active_s_boxes(current_data)
        if activity == -1:
            return -1
        # print(i, activity)
        if check_activity(activity, linear_approx[i + 1]) == -1:
            return -1
    return 1

def get_next_active_s_boxes(inputs):
    """
    function to check if the linear analysis is right
    it will return the next active s-boxes [0, 1, 0, 0] means only the second s-box is active
    """
    active_s_boxes = [0 for _ in range(4)]
    for i in range(4):
        input = inputs[i][0]
        output = inputs[i][1]
        if (input == 0 and output != 0) or (input != 0 and output == 0):
            return -1
        if output == 0:
            continue
        # output is a number -> convert to binary
        output = hc.int_to_bit_4(output)
        for j in range(4):
            val = output[j]
            if val == '1':
                after_perm = PERMUTATION[i*4+j] // 4
                active_s_boxes[after_perm] = 1
    return active_s_boxes

def check_activity(current, next_line):
    """
    check if a line is correct 
    -> if there is a output without a input or vice versa it throws an error
    -> if there is no input, but a previous active s-box, it throws an error and so on
    """
    # current is the activity of the s-boxes in the current line
    # next_line is the activity of the s-boxes in the next line
    for i in range(4):
        if current[i] == 1:
            # nextline has to have a input
            if next_line[i][0] == 0 or next_line[i][1] == 0:
                return -1
        else:
            # nextline has to have no input since the input is inactive
            if next_line[i][0] != 0 or next_line[i][1] != 0:
                return -1
    return 1

def get_linear_approx(linear_approx_file):
    """
    returns the linear approximation from a file in matrix form -> matrix entries are in integer format
    """
    data = []
    with open(linear_approx_file) as f:
        for line in f:
            line = line.replace("\n", "").split(' ')
            new_line = []
            for el in line:
                tmp = []
                for entry in el:
                    # convert hex to int
                    tmp.append(int(entry, 16))
                new_line.append(tmp)
            data.append(new_line)
    # data is in form [[[0, 0], [1, 2], [0, 0], [3, 14]], ...] -> first s-box in first line input is in the first first element on the left
    # first s-box in first line output is in the first first element on the right
    # and so one for all s-box activity in the linear approximation
    return data

def get_s_box(s_box_file):
    """
    reads the s box from the file and saves it in a list of integers
    """
    s_box = []
    with open(s_box_file) as f:
        for line in f:
            line = line.replace("\n", "").split(' ')
            for entry in line:
                for el in entry:
                    # convert hex to int
                    s_box.append(int(el, 16))
    return s_box

def count_zeros(approx, s_box):
    """
    gets the approximation of a s box -> input , output in a list like [11, 4]
    goes through every combination of possible inputs and computes how often U_a id equal to U_b
    this approach to the algorithm is directly taken from the main lecture slides -> page 139 / 140 -> computation of l(a,b)
    """
    # approx has form [11, 4] with 11 being the input bits and 4 the output bits
    # a
    active_input_bits = hc.int_to_bit_4(approx[0])
    # b
    active_output_bits = hc.int_to_bit_4(approx[1])

    zeros_counter = 0
    # every possible input i
    for i in range(16):
        # convert i to bit representation (4 bits)
        bit_repr = hc.int_to_bit_4(i)
        # apply s_box
        after_s_box = s_box[i]
        bit_repr_after = hc.int_to_bit_4(after_s_box)

        # for every active bit in the input, calculate the activity output -> U_a
        bit_list = []
        for b in range(len(active_input_bits)):
            if active_input_bits[b] == '1':
                bit_list.append(bit_repr[b])
        # active bits in the output -> U_b
        for b in range(len(active_output_bits)):
            if active_output_bits[b] == '1':
                bit_list.append(bit_repr_after[b])
        # count ones -> since we want to know if U_a xor U_b is zero -> if ones are even -> we have U_a xor U_b = zero
        if bit_list.count('1') % 2 == 0:
            zeros_counter += 1
    return zeros_counter

def get_bias(linear_approx_file, s_box_file):
    """
    complete function to get the bias of the linear approximation

    this approach is directly taken from the main lecture slides
    """
    # check if approximation is right
    linear_approx = get_linear_approx(linear_approx_file)
    check = check_linear_approx(linear_approx)
    if check == -1:
        print("Approximation is not right!")
        exit(-1)

    # get the s box
    s_box = get_s_box(s_box_file)
    different_s_boxes = {}
    length = 0
    for line in linear_approx:
        for start, end in line:
            # current s box is not active
            if start == 0 or end == 0:
                continue
            length += 1
            if (start, end) in different_s_boxes:
                different_s_boxes[(start, end)] += 1
            else:
                different_s_boxes[(start, end)] = 1

    # calculate the bias as given in the main lecture slides page 148-150
    bias = 2**(length - 1)
    for key in different_s_boxes:
        zeros = (count_zeros(key, s_box) - 8) / 16
        bias *= (zeros**different_s_boxes[key])
    print(abs(bias))
    