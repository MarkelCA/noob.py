def get_g():
    return (n for n in range(10))

g = get_g()

print('First run of g:')
for n in g:
    print(n, end=' ')

print('\nSecond run of g:')

for n in g:
    print(n, end=' ')

print('\nNew generator:')

for n in get_g():
    print(n, end=' ')
