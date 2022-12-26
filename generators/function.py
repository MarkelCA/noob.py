def get_g():
    for n in range(10):
        yield n * 2

print('First run of g:')
g = get_g()
for n in g:
    print(n, end=' ')

print('\nSecond run of g:')
for n in g:
    print(n, end=' ')

