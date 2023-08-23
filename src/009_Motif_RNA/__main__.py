import os
import re
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("python 009_Motif_RNA file.txt")
        sys.exit(-1)

    name_file = sys.argv[1]
    string_s = ""
    string_t = ""

    with open(name_file, "r") as ros_subs:
        string_s = ros_subs.readlines()[0].replace("\n", "")
        string_t = ros_subs.readlines()[1].replace("\n", "")

    regExp = f"(?={string_t})"
    indexes = [str(m.start() + 1) for m in re.finditer(regExp, string_s)]

    result = " ".join(indexes)
    print(result)

    output_path = os.path.join(
        os.path.dirname(os.path.abspath(name_file)), "output.txt"
    )
    with open(output_path, "w") as output_file:
        output_file.write(result)
