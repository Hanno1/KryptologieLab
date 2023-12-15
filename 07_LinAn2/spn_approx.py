import helperclass as hc

PERMUTATION = [1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]

def get_next_active_s_boxes(inputs):
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
    for i in range(4):
        if current[i] == 1:
            if next_line[i][0] == 0 or next_line[i][1] == 0:
                return -1
        else:
            if next_line[i][0] != 0 or next_line[i][1] != 0:
                return -1
    return 1

def check_linear_approx(linear_approx):
    for i in range(2):
        current_data = linear_approx[i]
        activity = get_next_active_s_boxes(current_data)
        if activity == -1:
            return -1
        # print(i, activity)
        if check_activity(activity, linear_approx[i + 1]) == -1:
            return -1
    return 1

def get_linear_approx(linear_approx_file):
    data = []
    with open(linear_approx_file) as f:
        for line in f:
            line = line.replace("\n", "").split(' ')
            new_line = []
            for el in line:
                tmp = []
                for entry in el:
                    tmp.append(int(entry, 16))
                new_line.append(tmp)
            data.append(new_line)
    return data

def get_s_box(s_box_file):
    s_box = []
    with open(s_box_file) as f:
        for line in f:
            line = line.replace("\n", "").split(' ')
            for entry in line:
                for el in entry:
                    s_box.append(int(el, 16))
    return s_box

def count_zeros(approx, s_box):
    # approx has form [11, 4] with 11 being the input bits and 4 the output bits
    active_input_bits = hc.int_to_bit_4(approx[0])
    active_output_bits = hc.int_to_bit_4(approx[1])

    zeros_counter = 0
    for i in range(16):
        bit_repr = hc.int_to_bit_4(i)
        after_s_box = s_box[i]
        bit_repr_after = hc.int_to_bit_4(after_s_box)

        bit_list = []
        for b in range(len(active_input_bits)):
            if active_input_bits[b] == '1':
                bit_list.append(bit_repr[b])
        for b in range(len(active_output_bits)):
            if active_output_bits[b] == '1':
                bit_list.append(bit_repr_after[b])
        if bit_list.count('1') % 2 == 0:
            zeros_counter += 1
    return zeros_counter

def get_bias(linear_approx_file, s_box_file):
    linear_approx = get_linear_approx(linear_approx_file)
    check = check_linear_approx(linear_approx)

    if check == -1:
        print("Approximation is not right!")
        exit(-1)
    s_box = get_s_box(s_box_file)
    different_s_boxes = {}
    length = 0
    for line in linear_approx:
        for start, end in line:
            if start == 0 or end == 0:
                continue
            length += 1
            if (start, end) in different_s_boxes:
                different_s_boxes[(start, end)] += 1
            else:
                different_s_boxes[(start, end)] = 1
    bias = 2**(length - 1)
    for key in different_s_boxes:
        zeros = (count_zeros(key, s_box) - 8) / 16
        bias *= (zeros**different_s_boxes[key])
    print(abs(bias))
    