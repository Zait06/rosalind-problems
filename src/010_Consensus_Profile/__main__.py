import os
import sys
import numpy as np

RNA_count = {"A": [], "C": [], "G": [], "T": []}


def matrix_str():
    str = ""
    for key in RNA_count.keys():
        str += f"{key}: {' '.join(RNA_count[key])}\n"
    return str


if __name__ == "__main__":
    file_name = sys.argv[1]
    data_matrix = []
    dna_string = ""

    with open(file_name, "r") as file_data:
        for line in file_data.readlines():
            if line.startswith(">"):
                if len(dna_string) == 0:
                    continue
                data_matrix.append(list(dna_string))
                dna_string = ""
            else:
                dna_string += line.replace("\n", "")
        data_matrix.append(list(dna_string))

    size = len(data_matrix[0])
    data_matrix = np.array(data_matrix)
    final_dna = []
    for idx in range(0, size):
        vector = data_matrix[:, idx]
        max_count = 0
        elem_char = ""
        for key in RNA_count.keys():
            data = vector.tolist().count(key)
            RNA_count[key].append(str(data))
            if max_count < data:
                elem_char = key
                max_count = data
        final_dna.append(elem_char)

    print("".join(final_dna))
    print(matrix_str())

    output_path = os.path.join(
        os.path.dirname(os.path.abspath(file_name)), "output.txt"
    )

    with open(output_path, "w") as output_file:
        output_file.write("".join(final_dna) + "\n")
        output_file.write(matrix_str())
