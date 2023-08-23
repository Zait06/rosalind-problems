import os
import sys


def hamming_distance(str_s, str_t):
    count = 0
    for idx in range(0, len(str_s)):
        if str_s[idx] != str_t[idx]:
            count += 1
    return count


if __name__ == "__maint__":
    if len(sys.argv) != 2:
        print("python 006_Counting_point_mutation file.txt")
        sys.exit(-1)
    name_file = sys.argv[1]
    lines = []
    a = ""
    b = ""

    with open(name_file, "r") as hamming_file:
        a = hamming_file.readlines()[0].replace("\n", "")
        b = hamming_file.readlines()[0].replace("\n", "")

    result = hamming_distance(a, b)
    print(result)

    output_path = os.path.join(
        os.path.dirname(os.path.abspath(name_file)), "output.txt"
    )
    with open(output_path, "w") as output_file:
        output_file.write(result)
