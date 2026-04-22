# Small Libspec Example

Welcome to the smallest possible example of using **[libspec](https://github.com/drhodes/libspec)**! 

Libspec is a way to iteratively specify a piece of software. Although the libspec itself is written in Python, the specs it generates are completely language-agnostic. Libspec defines an object model for spec generation, aiming to reduce boilerplate with inheritance.

## The Object Model and Inheritance

Libspec reduces the repetition common in specification writing by leveraging standard object-oriented programming concepts like inheritance.

To see this in action, take a look at the specifications located in the `spec/` directory.

### Focusing on `spec/app.py` and `spec/err.py`

In our `spec/err.py` file, we use multiple inheritance to create base classes that mix-in boilerplate requirements:

```python
from libspec import Ctx, Feature, Requirement

class Err(Ctx):
    '''It's important that error handling be done excellently.  If a
    function can fail, then it needs to do so in the most elegant way
    possble.  Error reporting, handling, exceptions and all aspects of
    failure must be taken to extreme. It should be possible to
    understand the program by reading the error messages.'''

# Mixin `Err` with `Feature` and `Requirement`
class Feat(Err, Feature): pass
class Req(Err, Requirement): pass
```

By having our specific features naturally inherit from these custom base classes (`Feat`, `Req`), every feature automatically incorporates the disciplined error handling guidance defined in `Err`. 

### What is a Feature?

In libspec, a `Feature` (and its counterpart `Requirement`) is a class used to formally declare a specific capability of your software. The class's docstring acts as the human-readable description of that feature. 

When you look at `spec/app.py`, you can see how we implement specific capabilities using the base classes we created:

```python
from .err import Feat, Req

class App(Req):
    '''This program found in project-root/main.py should emit the
    string "Hello, world!" to the terminal.'''

class CmdLine(Feat):
    '''This program does not take any command line arguments.'''
```

## Generating the Spec

Once your features and requirements are defined, you use a main spec script to tie them together and generate your language-agnostic outputs (like XML).

Check out `spec/main_spec.py`:

```python
from libspec import Spec
from . import app

class SmallestExample(Spec):
    # Import specs under the `modules` method
    def modules(self):
        return [app]

if __name__ == "__main__":
    # Generate the XML spec inside the 'spec-build' directory
    SmallestExample().write_xml("build-spec")
```

Here, we inherit from `libspec.Spec` and implement the `modules` method to return a list of our spec modules (in this case, just `app`). Then, calling `.write_xml("build-spec")` walks the object model, compiles our docstrings and inheritance trees, and renders the final language-agnostic XML specifications into the `build-spec/` directory.
