### Section 3: Variables & memory
* In Python, every variable is a memory pointer
* String interning & integer caching
* Garbage collection & Reference counting


### Section 4: Numeric types  
* Built-in round() implements banker's rounding, not the classical half-up rounding
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


### Section 7: Scopes, Closures & Decorators
* If Python can not find variable in current **scope**, it will look for it in an enclosing scope's namespace, going one step up in hierarchy.
* At compile time, python pre-determines that specific variables (for example function local variables), will be part of local namespaces, but namespaces and scopes are created at runtime, sometimes leads to confusing errors. For example when you're using outer variable of name `a`, but have it later defined in local scope.
* `global` keyword  
* In Python, code blocks do **not** have separate scopes/namespaces. So for example variables created within `if` statement, exist in scope that said `if` belongs to.
* **Closures** are basically functions, which carry reference to **heap-allocated cells**, allowing those variables to persist across calls or closures.
* **Cells** in python are intermediary objects (middlemen). When returning a closure from a function, the *free variable*, the variable that is defined in outer scope being used in the inner scope (thus creating the closure), are pointing to same cell in memory, which is pointing to value in memory address.
* **Cells** are created if these 2 conditions are met:
  * A variable is assigned in a non-global scope
  * That same variable is referenced in a nested function
* **Decorators** are higher-order functions that take another function as input, and return a new function (often a closure) that wraps the original function, adding extra behavior before or after its execution.