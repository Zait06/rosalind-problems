import sys

RNA_CONDON_TABLE = {
    "UUU": "F",
    "CUU": "L",
    "AUU": "I",
    "GUU": "V",
    "UUC": "F",
    "CUC": "L",
    "AUC": "I",
    "GUC": "V",
    "UUA": "L",
    "CUA": "L",
    "AUA": "I",
    "GUA": "V",
    "UUG": "L",
    "CUG": "L",
    "AUG": "M",
    "GUG": "V",
    "UCU": "S",
    "CCU": "P",
    "ACU": "T",
    "GCU": "A",
    "UCC": "S",
    "CCC": "P",
    "ACC": "T",
    "GCC": "A",
    "UCA": "S",
    "CCA": "P",
    "ACA": "T",
    "GCA": "A",
    "UCG": "S",
    "CCG": "P",
    "ACG": "T",
    "GCG": "A",
    "UAU": "Y",
    "CAU": "H",
    "AAU": "N",
    "GAU": "D",
    "UAC": "Y",
    "CAC": "H",
    "AAC": "N",
    "GAC": "D",
    "UAA": None,
    "CAA": "Q",
    "AAA": "K",
    "GAA": "E",
    "UAG": None,
    "CAG": "Q",
    "AAG": "K",
    "GAG": "E",
    "UGU": "C",
    "CGU": "R",
    "AGU": "S",
    "GGU": "G",
    "UGC": "C",
    "CGC": "R",
    "AGC": "S",
    "GGC": "G",
    "UGA": None,
    "CGA": "R",
    "AGA": "R",
    "GGA": "G",
    "UGG": "W",
    "CGG": "R",
    "AGG": "R",
    "GGG": "G",
}


def split_string_into_n_characters(input_string, n):
    return [input_string[i : i + n] for i in range(0, len(input_string), n)]


if __name__ == "__main__":
    n = 3
    sp = []

    name_file = sys.argv[1]
    line = ""
    with open(name_file, "r") as ros_prot:
        line = ros_prot.readline().replace("\n", "")

    result = split_string_into_n_characters(line, n)

    for r in result:
        r_char = RNA_CONDON_TABLE[r]
        if r_char is None:
            continue
        sp.append(r_char)

    result = "".join(sp)
    print(result)
    with open("output.txt", "w") as output_file:
        output_file.write(result)
