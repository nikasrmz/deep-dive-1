### Section 3: Variables & memory
* In Python, every variable is a memory pointer
* String interning & integer caching
* Garbage collection & Reference counting


### Section 4: Numeric types  
* Built-in round() implements bankers rounding, not the classical half-up rounding
* Floats are not reliable, since some rational numbers in base 10 might not be rational in base 2, thus, is truncated to be stored.
* Decimals are more precise than floats, but lot heavier to store/process.
* Theres `divmod(quotient, divisor) -> dividend, remainder` function, replacing `a, b = n // m,  n % m`
* Code: `if (lst is not None) and (len(lst) > 0):` is exactly the same as: `if lst:` 
* Boolean operators return values that you pass, not just booleans
  * `X or Y`   --  returns `X` if `X` is `true`, else `Y`
  * `X and Y`  --  returns `X` if `X` is `false`, else `Y`


### Section 5: Functional parameters
* Unpacking
    * `*` for every iterable, such as `list`
    * `**` for every mapping, such as `dict`
* Parameter passing: `*args`, `**kwargs`, `*`, `/`
* Default parameter values are evaluated once at function definition time, so mutable defaults are shared across calls. 


### Section 6: First-class functions
* Lambda functions
* Function introspection
  * Introspection in Python means the ability of a program to examine itself at runtime — specifically, to inspect the type, structure, and attributes of objects.
* `inspect` library
  * `ismethod(callable)`
  * `isfunction(callable)`
  * `isroutine(callable)`
  * `getsource(callable)`
  * `getmodule(callable)`
  * ... and many more.
* Function vs method - A method is a function that is bound to an instance of a class.
* Implementing `__call__` method makes instance of an object callable
* `map()`, `filter()`, `reduce()`, `zip()`
* Idea of partial functions, `partial` from `functools`
* `operator` module, encapsulating many useful and mostly simple functions, so you don't have to write them yourself usign lambda.
  * `itemgetter()` and `attrgetter()` 


