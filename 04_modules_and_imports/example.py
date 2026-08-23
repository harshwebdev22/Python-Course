"""Run me from this folder: python3 example.py"""

import math  # whole module
from math import sqrt, pi  # named imports
from math import sqrt as square_root  # alias

print(math.floor(3.7))
print(sqrt(16), pi)
print(square_root(25))

# Local module (helpers.py, sitting right next to this file)
import helpers
from helpers import format_name

print(helpers.GREETING_PREFIX)
print(format_name("  harsh WEBSITE dev  "))

# A local package (mypackage/, with __init__.py)
from mypackage import utils
from mypackage.utils import shout

print(utils.shout("hi"))
print(shout("bye"))

# __name__ trick — this only prints when the file is run directly,
# not if something else `import example`s it.
if __name__ == "__main__":
    print(f"__name__ is {__name__!r} — this file was run directly")
