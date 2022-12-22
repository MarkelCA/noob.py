# Descriptors

## What are they
Descriptors are Python objects that implement a method of the descriptor protocol, which gives you the ability to create objects that have special behavior when they’re accessed **as attributes of other objects.**

```python
__get__(self, obj, type=None) -> object
__set__(self, obj, value) -> None
__delete__(self, obj) -> None
__set_name__(self, owner, name)
````
