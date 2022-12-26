# Generators

Generators are a object type useful for iterations. The difference with lists is that they **generate** the next item on demand, rather than storing the entire list on memory.

They are useful as a performance optimization if you just want to iterate your list once but they're not compatible with lists methods.

```python
def gen():
    return (something for something in get_some_stuff())

print gen()[:2]     # generators don't support indexing or slicing
print [5,6] + gen() # generators can't be added to lists
```

There are two ways of creating generators. One way it's with generator expressions and the other one are generator functions using the `yield` command
