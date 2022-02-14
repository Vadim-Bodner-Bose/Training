from generator_example1 import countdown

# you can use it for functions that take iterables as input
cd = countdown(3)
sum_cd = sum(cd)
print(f" sum of the generated iterable is: {sum_cd}")

cd = countdown(3)
sorted_cd = sorted(cd)
print(f" the sorted iterable from generator is: {sorted_cd}")