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
from err import Feat, Req

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
import app

class SmallestExample(Spec):
    # Import specs under the `modules` method
    def modules(self):
        return [app]

if __name__ == "__main__":
    # Generate the XML spec inside the 'spec-build' directory
    SmallestExample().write_xml("build-spec")
```

Here, we inherit from `libspec.Spec` and implement the `modules` method to return a list of our spec modules (in this case, just `app`). Then, calling `.write_xml("build-spec")` walks the object model, compiles our docstrings and inheritance trees, and renders the final language-agnostic XML specifications into the `build-spec/` directory.

## Building the Spec

To actually generate your parsed object model, execute the main spec file as a Python module from your project root. Be sure you've set PYTHONPATH and aren't using relative imports:

```bash
export PYTHONPATH=.
```

```bash
python -m spec.main_spec
```

Or, in a `uv` environment:

```bash
uv run libspec build spec/main_spec.py
```

This runs your `SmallestExample` code, constructs your specification artifact, and neatly outputs it all into the `build-spec/` folder.

## Reviewing Specs (Spec Diffs)

Libspec provides a built-in tool that can be invoked as a Python module to evaluate your generated specifications. Once your specs are built into a directory, you can review them and view diffs using:

```bash
python -m libspec.spec_diff build-spec
```

This command compares existing specs, providing an efficient way to track additions, removals, and changes over the course of your iterative software specification.

## The Libspec Workflow

Once started, the generic workflow using libspec is approximately:

1. **Build** the new spec artifact.
2. **Diff** the new spec with the old spec using the binary to get the isolated changes.
3. **Pass** the resulting changes to a coding agent to quickly generate the implementation.
4. **`git commit`** the changes alongside the new spec. This approach encodes a record of development that supplements your standard Git commit messages.

## Using Libspec with MCP

Libspec provides a Model Context Protocol (MCP) server that exposes its functionality to compatible AI coding agents. This allows your agent to programmatically build, diff, and query your project's specifications.

To use the `libspec-mcp` server, you'll need to configure your editor or AI agent to run it. Here is the standard JSON configuration snippet:

```json
{
    "mcpServers": {
        "libspec": {
            "command": "uv",
            "args": [
                "run",
                "libspec-mcp"
            ]
        }
    }
}
```

### Editor-Specific Configuration

The process for adding a custom MCP server varies depending on your tool. Below are links to the official documentation for adding custom MCP servers for popular editors and AI agents:

*   **Cursor:** [Adding Custom MCP Servers in Cursor](https://docs.cursor.com/context/model-context-protocol)
*   **Claude Code:** [Claude Code MCP Configuration](https://modelcontextprotocol.io/quickstart/user)
*   **Windsurf:** [Windsurf MCP Documentation](https://docs.codeium.com/windsurf/mcp)
*   **GitHub Copilot:** [VS Code MCP Configuration](https://code.visualstudio.com/docs/editor/ai-chat#_model-context-protocol)
*   **Gemini:** [Google Gemini MCP Integration](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/model-context-protocol)
*   **Aider:** [Aider MCP Documentation](https://aider.chat/docs/mcp.html)
