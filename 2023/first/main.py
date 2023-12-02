calibration = open("calibration.txt", "r").read()
calibration_lines = calibration.split("\n")

sum = 0

for line in calibration_lines:
    last = ""
    first = ""

    for c in line:
        if c.isnumeric():
            if not first:
                first = c
            else:
                last = c

    if first and last:
        sum += int(first + last)
    else:
        sum += int(first + first)

print(sum)
