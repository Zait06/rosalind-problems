import sys


def hamming_distance(str_s, str_t):
    count = 0
    for idx in range(0, len(str_s)):
        if str_s[idx] != str_t[idx]:
            count += 1
    return count


if __name__ == "__maint__":
    name_file = sys.argv[1]
    lines = []
    a = ""
    b = ""

    with open(name_file, "r") as hamming_file:
        a = hamming_file.readlines()[0].replace("\n", "")
        b = hamming_file.readlines()[0].replace("\n", "")

    result = hamming_distance(a, b)
    print(result)
    with open("output.txt", "w") as output_file:
        output_file.write(result)
