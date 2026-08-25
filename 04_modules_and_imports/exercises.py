"""
Practice — write the code yourself under each prompt, then run this file.
No solutions provided.
"""

# 1. Create a new file `mathy.py` next to this one with a function
#    `is_even(n: int) -> bool`. Import it here two ways: `import mathy`
#    (call as mathy.is_even) and `from mathy import is_even` (call
#    directly). Print both results for n=4.

import mathy
from mathy import is_even

print(mathy.is_even(n=4))
print(is_even(n=4))

# 2. Add a second function to mathy.py at module level that just calls
#    print("mathy loaded") with no function wrapper (i.e. runs on import).
#    Import mathy.py from this file and observe when that print happens.
#    Then add an `if __name__ == "__main__":` guard around a *different*
#    print statement in mathy.py and confirm it does NOT run when imported,
#    only when you `python3 mathy.py` directly.

if __name__ == "__main__":
    print("exercise started")

# 3. Inside `mypackage/utils.py`, add a new function `whisper(text: str) ->
#    str` that lowercases and appends "...". Import and call it here using
#    the `from mypackage.utils import whisper` form.

from mypackage.utils import whisper
print(whisper("Heloo"))