# virtualenv-wrapper
Before PEP 668 – Marking Python base environments as “externally managed”, we
used to be able to install python packages globally for each user and use them
in any python scripts. This is ugly but extremely convenient to use.

In contrast, using virtualenv is a multi-step process. You have to:
1. Setup virtual environment with `virtualenv .`
2. Activate the virtual environment with `source bin/activate`
3. Install any package you need with `pip install <packages>`
Importantly, step 2 have to be done everytime you need to run your scripts.

Another annoying aspect of virtualenv is that it poop a lot files into the
current directory, making your work directory cluttered.

Both of this make python as almost as annoying to use as conventional compiled
language even though python is technically a scripting language.

This tool is designed to solve both of the above problems by
1. Allowing you to declare your dependencies at the beginning of your python
   scripts.
2. Creating transient virtual environments keyed by the list of dependencies in
   xdg cache directory.

This goal is that you should be able to just write any python script in a
single file and "just run it" as long as you have virtualenv-wrapper installed.

## Installation
Copy [virtualenv-wrapper](virtualenv-wrapper) to somewhere under your PATH.

## Usage
The code in [example.py](example.py) should provide a simple enough example.

## Caveat
Language servers for python will not be able to resolve installed packages
because it is unaware of the transient virtual environment. In fact, since
dependencies are completely specified in code, it is necessary to execute
potentially untrusted code to resolve the virtual environment. This makes
interop with language servers more difficult.
