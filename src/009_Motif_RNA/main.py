import re
import sys

if __name__ == "__main__":
    name_file = sys.argv[1]
    string_s = ""
    string_t = ""

    with open(name_file, "r") as ros_subs:
        string_s = ros_subs.readlines()[0].replace("\n", "")
        string_t = ros_subs.readlines()[1].replace("\n", "")

    regExp = f"(?={string_t})"
    indexes = [str(m.start() + 1) for m in re.finditer(regExp, string_s)]
    print(" ".join(indexes))
