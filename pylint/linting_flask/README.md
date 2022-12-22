# Linting Flask with Pylint

This is a test to examine what does Pylint consider for best practices.

It has been done picking a file from the [Flask Framework](https://github.com/pallets/flask/blob/main/src/flask/views.py) and modifying until it becomes perfect for the linter.

```bash
# We run the linter excluding warning codes related to the import dependencies
pylint perfect.py --disable=E1101,W0404,E0401
```

## Results
The score was nearly perfect
### `original.py`
```
$ pylint original.py --disable=E1101,W0404,E0401

************* Module linting_flask.original
original.py:76:0: C0330: Wrong hanging indentation before block (add 4 spaces).
        cls, name: str, *class_args: t.Any, **class_kwargs: t.Any
        ^   | (bad-continuation)
original.py:1:0: C0114: Missing module docstring (missing-module-docstring)
original.py:8:0: C0103: Constant name "http_method_funcs" doesn't conform to UPPER_CASE naming style (invalid-name)
original.py:161:4: W0221: Parameters differ from overridden 'dispatch_request' method (arguments-differ)

------------------------------------------------------------------
Your code has been rated at 9.22/10 (previous run: 9.22/10, +0.00)
```
### `perfect.py`
```
$ pylint perfect.py --disable=E1101,W0404,E0401 

************* Module linting_flask.perfect
perfect.py:162:4: W0221: Parameters differ from overridden 'dispatch_request' method (arguments-differ)

------------------------------------------------------------------
Your code has been rated at 9.80/10 (previous run: 9.80/10, +0.00)
```

The changes made to the file to acomplish this score were the following:
```diff
--- original.py	2022-12-22 21:33:35.280647235 +0100
+++ perfect.py	2022-12-22 21:33:04.800154461 +0100
@@ -1,3 +1,4 @@
+""""Module docstring"""
 import typing as t

 from . import typing as ft
@@ -5,7 +6,7 @@
 from .globals import request


-http_method_funcs = frozenset(
+HTTP_METHOD_FUNCS = frozenset(
     ["get", "post", "head", "options", "delete", "put", "trace", "patch"]
 )

@@ -73,7 +74,7 @@

     @classmethod
     def as_view(
-        cls, name: str, *class_args: t.Any, **class_kwargs: t.Any
+            cls, name: str, *class_args: t.Any, **class_kwargs: t.Any
     ) -> ft.RouteCallable:
         """Convert the class into a view function that can be registered
         for a route.
@@ -151,7 +152,7 @@
                 if getattr(base, "methods", None):
                     methods.update(base.methods)  # type: ignore[attr-defined]

-            for key in http_method_funcs:
+            for key in HTTP_METHOD_FUNCS:
                 if hasattr(cls, key):
                     methods.add(key.upper())
```
