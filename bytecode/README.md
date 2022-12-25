# Python vs Java bytecode

If Python and Java are both interpreted compiled to bytecode languages why it's Java so much faster that Python?

## Research

[Compilation to Bytecode, Java vs Python. What is the reason for the difference in time taken?](https://stackoverflow.com/questions/63401983/compilation-to-bytecode-java-vs-python-what-is-the-reason-for-the-difference-i)

[Is Java faster than CPython mostly because of JIT? If so, why doesn't CPython have JIT?](https://www.quora.com/unanswered/Is-Java-faster-than-CPython-mostly-because-of-JIT-If-so-why-doesn-t-CPython-have-JIT)

[https://www.quora.com/If-Python-and-Java-both-compile-to-bytecode-why-is-Java-so-much-faster-Whats-the-JIT-doing-with-bytecode-that-CPython-isnt?share=1](https://www.quora.com/If-Python-and-Java-both-compile-to-bytecode-why-is-Java-so-much-faster-Whats-the-JIT-doing-with-bytecode-that-CPython-isnt?share=1)

## Conclusion

Java and Python both are interpreted because both are compiled to bytecode and run in a VM. The difference is that Java being a staticly typed language its compiler can do a lot of optimization knowing the types of all the objects / imports / packages and therefore not checking them at runtime.

Another difference is that probably Java in most of their JREs has already implemented a JIT compiler. And Python by default runs purely interpreted, you have to use Pypy or similar to run with just in time compiled

