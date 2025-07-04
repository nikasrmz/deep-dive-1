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
* `from functools import wraps` - is used in custom decorators to decorate the inner function, ensuring that the original function's metadata (like its name and docstring) is preserved.
* **Memoization** - a technique used to cache the results of expensive function calls and return the cached result when the same inputs occur again, thereby reducing computation time on subsequent calls.  
* **Decorator factories** are either functions or callable classes used to implement parameterized decorators.
  * In the function-based approach, the outer function takes the decorator parameters and returns the actual decorator, which in turn returns the wrapper function.
  * n the class-based approach, the class takes the parameters in `__init__`, and implements `__call__` to behave like the decorator — returning the wrapper when applied to a function.
* **Monkey-patching** - dynamic modification or extension of classes or modules at runtime — for example, adding, overriding, or altering functions or attributes. It is often used to change the behavior of third-party libraries without modifying their source code. While monkey-patching can be done using decorators, it's not limited to them.
* **Decorator dispatching** refers to dynamically selecting which implementation to use based on the type or value of the argument(s) at runtime, often using a dispatch table or the functools.singledispatch mechanism.


### Section 8: Tuples as Data Structures and Named Tuples
* Using `_` as a placeholder when unpacking is just a convention. For python, it's just another variable. For example: `*_, c = (1, 2, 3)` => `_ = [1, 2]`, `c = 3`
* `from collections import namedtuple` is a class factory function in Python that returns a new class type, which is a subclass of `tuple`. This class allows you to create tuple-like objects where fields can be accessed using named attributes, making the code more readable and self-documenting.
    ```
    Point2D = namedtuple('Point2D', ['x', 'y'])
    point = Point2D(x=1, y=2)
    ```
* `_replace` - a method on namedtuple instances that returns a **new instance** with specified fields replaced by new values. Since namedtuples **are immutable**, `_replace()` provides a safe way to create modified copies.
* `namedtuple` is a more memory-efficient and faster alternative to `dataclass` when you only need immutable, lightweight data containers.


### Section 9: Modules, Packages and Namespaces
* **Imported modules are objects** (specifically instances of the built-in type module), and when you import a module, you're **binding a variable to that module object**.