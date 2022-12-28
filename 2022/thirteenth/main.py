import json

packets = open("packets.txt", "r").read()


def compare_packets(left, right):
    for i in range(0, max(len(left), len(right))):
        if i == len(left) and i <= len(right):
            return True  # left out of items
        elif i == len(right) and i <= len(left):
            return False  # right out of items

        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] < right[i]:
                return True
            elif left[i] > right[i]:
                return False
            else:
                continue

        # convert number to list for comparison
        if isinstance(left[i], int) and isinstance(right[i], list):
            left[i] = [left[i]]
        elif isinstance(left[i], list) and isinstance(right[i], int):
            right[i] = [right[i]]

        if isinstance(left[i], list) and isinstance(right[i], list):
            comparison = compare_packets(left[i], right[i])

            if not comparison == -1:
                return comparison

    return -1  # unable to validate packets


def main():
    indices = []
    pairs = packets.split("\n\n")

    for i, pair in enumerate(pairs):
        first, second = pair.split("\n")

        left = json.loads(first)
        right = json.loads(second)

        if compare_packets(left, right):
            indices.append(i + 1)  # first index is 1

    print(f"Sum of indices with correct packet order: {sum(indices)}")


if __name__ == "__main__":
    main()
