import sys
import spn_approx as approx

"""
main function to get the bias of the linear approximation
"""

if len(sys.argv) == 3:
    s_box_file = sys.argv[1]
    linear_approx_file = sys.argv[2]

    linear_approx = approx.get_bias(linear_approx_file, s_box_file)
else:
    print("Usage: python3 spn_get_bias.py <linear_approx_file> <s_box_file>")
    exit()
