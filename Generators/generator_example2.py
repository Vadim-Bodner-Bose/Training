from generator_example1 import countdown
# you can iterate over a generator object with a for in loop
cd = countdown(3)
print(f"iterable created by the countdown generator {cd}")
for x in cd:
    print(x)