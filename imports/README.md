# Imports

This section is meant to compare the trade-offs of the two different import styles 
The two posibilities are `import X` vs `from X import Y` statements.

# Conclusion


The individual import could be slower but in most cases would be unnoticable. Both imports have to parse the entire module. The difference is that when you use a full import using the imported member means performing 2 lookups, one for the module and another one for the member variable / function. Using the from statemet does not require the module lookup because the function gets copied locally in the current module. This could affect performance specially when you use an imported members so repeatedly (for example millions of times)

### Full module import 

| Pros  | Cons |
| ------------- | ------------- |
| More expressive because because of the explicit namespace  | Slower on performance for some cases |

### Individual imports

| Pros  | Cons |
| ------------- | ------------- |
| Faster performance on some cases  | Overrides same named variables without warning |
