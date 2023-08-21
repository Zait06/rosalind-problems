import sys
import numpy as np

RNA_count = {
    'A': [],
    'C': [],
    'G': [],
    'T': []
}

def count_char_dna(dna_string):
    pass

if __name__ == '__main__':
    file_name = sys.argv[1]
    data_matrix = []
    dna_string = ''
    with open(file_name, 'r') as file_data:
        for line in file_data.readlines():
            print(line)
            if line.startswith('>'):
                if len(dna_string) == 0:
                    continue
                data_matrix.append(list(dna_string))
                dna_string = ''
            else:
                dna_string += line.replace('\n', '')
    
    size = len(data_matrix[0])
    data_matrix = np.array(data_matrix)
    print(data_matrix, "\n")
    for idx in range(0, size):
        vector = data_matrix[:, idx]
        for key in RNA_count.keys():
            RNA_count[key].append(vector.tolist().count(key))

    print(RNA_count)
