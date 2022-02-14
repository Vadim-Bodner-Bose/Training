# https://github.com/python-engineer/python-engineer-notebooks/blob/master/advanced-python/14-Generators.ipynb
def countdown(num):
    """example of a simple iterator"""
    print('Starting')
    while num > 0:
        yield num
        num -= 1

# this will not print 'Starting'
cd = countdown(3)

# this will print 'Starting' and the first value
print(next(cd))

# will print the next values
print(next(cd))
print(next(cd))

# this will raise a StopIteration
# print(next(cd))