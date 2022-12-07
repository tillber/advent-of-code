import re

message = open("message.txt", "r").read()


def main():
    regex = "((\w)"

    start_len = 4  # 14 for part 2
    for i in range(1, start_len):
        inner = ""
        for j in range(2, i + 2):
            inner += f"(?!\{j})"
        regex += f"({inner}\w)"

    regex += ")"

    match = re.search(regex,  message)
    # add length of start-of-message;
    # in order to get position of first message marker
    start_index = message.find(match.group(0)) + start_len

    print(start_index)


if __name__ == "__main__":
    main()
