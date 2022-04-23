import numpy

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180,
           168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

greater_than_188 = []
less_than_188 = []
for h in heights:
    if h > 188:
        greater_than_188.append(h)
    else:
        less_than_188.append(h)

print('\t These are greater than 188 \n')
print(greater_than_188)

print('\n \t these are less than 188')
print(less_than_188)

print(type(numpy))
