"""
Practice — write the code yourself under each prompt, then run this file.
No solutions provided.
"""

from pathlib import Path

# 1. Write a function `write_lines(path: Path, lines: list[str]) -> None`
#    that writes each string in `lines` to a file, one per line, using
#    `with open(...)`. Call it with a scratch file and 3 made-up lines,
#    then read the file back and print its contents to confirm.


# 2. Write a function `count_words(path: Path) -> int` that opens a text
#    file and returns the total word count across all lines (iterate
#    line-by-line, split each line on whitespace). Test it against the
#    file you created in #1.


# 3. Create a dict representing a small "config" (a few string/int/bool
#    keys), write it to a `.json` file with `json.dump`, then read it back
#    with `json.load` into a new variable and assert (with a plain `assert`
#    statement, or just print + eyeball it) that it equals the original
#    dict. Clean up the scratch file afterward with `Path.unlink()`.
