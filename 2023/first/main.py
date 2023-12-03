calibration = open("calibration.txt", "r").read()
calibration_lines = calibration.split("\n")

digits = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
          'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

sum = 0

for line in calibration_lines:
    print(f"line: {line}")

    last = None
    first = None

    for i, c in enumerate(line):
        if c.isnumeric():
            if not first:
                first = (i, c)
            else:
                last = (i, c)

    if not last:
        last = first

    # found by digits
    print(f"first: {first}, last: {last}")

    for d in digits.keys():
        lfind = line.find(d)
        rfind = line.rfind(d)

        if lfind >= 0 and (not first or lfind < first[0]):  # new 'first' found
            first = (lfind, digits[d])

        if rfind >= 0 and (not last or rfind > last[0]):  # new 'last' found
            last = (rfind, digits[d])

    # found by name (updated)
    print(f"updated first: {first}, last: {last}")

    print(int(first[1] + last[1]))
    sum += int(first[1] + last[1])

print(sum)
