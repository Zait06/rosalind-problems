import sys
import copy

DNA_char = {"A": 0, "T": 0, "C": 0, "G": 0}
DNA_replace = {"A": "T", "T": "A", "C": "G", "G": "C"}


def gc_content(gc_dict):
    num = gc_dict["G"] + gc_dict["C"]
    den = gc_dict["G"] + gc_dict["C"] + gc_dict["T"] + gc_dict["A"]
    return num / den * 100


def count_string(dna):
    gc_dict = copy.copy(DNA_char)
    for c in dna:
        if c == "\n":
            continue
        gc_dict[c] += 1
    return gc_dict


def dna_reverse(dna):
    reverse_dna = ""
    for c in dna:
        reverse_dna += DNA_replace[c]
    return reverse_dna[::-1]


if __name__ == "__main__":
    name_file = sys.argv[1]
    dna_str = ""
    name = ""
    all_gc_content = dict()
    with open(name_file, "r") as gc_file:
        for index, line in enumerate(gc_file.readlines()):
            if line.startswith(">"):
                if len(name) > 0:
                    gc_dict = count_string(dna_str)
                    all_gc_content[name[1:-1]] = gc_content(gc_dict)
                    dna_str = ""
                    name = line
                else:
                    name = line
            else:
                dna_str += line

        gc_dict = count_string(dna_str)
        all_gc_content[name[1:-1]] = gc_content(gc_dict)

        max_val = 0
        key_max = ""
        for key in all_gc_content.keys():
            value = all_gc_content[key]
            print(key, value)
            if max_val < value:
                key_max = key
                max_val = value
        result = f"{key_max}\n{max_val}"
        print(result)
        with open("output.txt", "w") as output_file:
            output_file.write(result)
