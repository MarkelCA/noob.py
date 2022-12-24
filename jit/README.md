# JIT

These are a set of tests with just in time compilation to measure the python performance on repetitive calculations

Credits to: [Just In Time (JIT) Compilers - Computerphile](https://www.youtube.com/watch?v=d7KHAVaX_Rs)

## Code
```python
def f(x, y):
    return x + y

a = 0
for _ in range(10000000):
    a += f(2,3)
```

## Tests
### Python interpreter
```bash
time python3 waste.py
```
Output:
```
________________________________________________________
Executed in    1,17 secs   fish           external
   usr time  1168,18 millis  559,00 micros  1167,62 millis
   sys time    4,19 millis  192,00 micros    4,00 millis
```
### PyPy (jit interpreter on)
```
time pypy  waste.py
```
Output:
```
________________________________________________________
Executed in   61,26 millis    fish           external
   usr time   21,89 millis  628,00 micros   21,26 millis
   sys time   21,26 millis    0,00 micros   21,26 millis
```
### PyPy (jit interpreter off)
```
time pypy --jit off waste.py
```
Output:
```
________________________________________________________
Executed in    2,40 secs   fish           external
   usr time    2,37 secs  728,00 micros    2,37 secs
   sys time    0,02 secs    0,00 micros    0,02 secs
```
