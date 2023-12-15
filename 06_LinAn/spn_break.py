import sys
from spn_main import SubstitutionPermutationNetwork as SPN

if len(sys.argv) == 3:
    clear_text_files = sys.argv[1]
    encrypted_text_files = sys.argv[2]

    with open(clear_text_files) as f:
        clear_text = f.read()
    with open(encrypted_text_files) as f:
        encrypted_text = f.read()
    
    network = SPN('0000')
    key = network.get_part_keys(clear_text, encrypted_text)

    print(f'part-key: *{key[0]}*{key[1]}')
else:
    print('Usage: `python3 spn_break.py <clear_text_files> <encrypted_text_files>`')