#! /usr/bin/python3


# start collecting measurement data
f = open("justaminute.02.in")

lines = []
for line in f:
    lines.append(line)
f.close()

# measurement data collected
lines.pop(0)


for line in lines:
    measurements = line.split()
    display_minutes = measurements[0]
    actual_seconds = measurements[1]
    actual_minutes = int(actual_seconds) / 60
    sum_actual_minutes = sum_actual_minutes + actual_minutes
    sum_display_minites = sum_display_minites + int(display_minutes)

result = sum_actual_minutes / sum_display_minites

if result <= 1:
    print('measurement error')
else:
    print(result)












