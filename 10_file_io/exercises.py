"""
Practice — write the code yourself under each prompt, then run this file.
No solutions provided.
"""

from pathlib import Path
import json

# 1. Write a function `write_lines(path: Path, lines: list[str]) -> None`
#    that writes each string in `lines` to a file, one per line, using
#    `with open(...)`. Call it with a scratch file and 3 made-up lines,
#    then read the file back and print its contents to confirm.

def write_lines(path: Path, lines: list[str]) -> None:
    with open(path, 'w') as f:
        for line in lines:
            f.write(line + '\n')
        
data_path = Path(__file__).parent / 'scratch.txt'

write_lines(
    data_path, 
    ['first line', 'second line', 'third line']
)

with open(data_path) as f:
    print(f.read())
    
# 2. Write a function `count_words(path: Path) -> int` that opens a text
#    file and returns the total word count across all lines (iterate
#    line-by-line, split each line on whitespace). Test it against the
#    file you created in #1.
def count_words(path: Path) -> int:
    count = 0
    with open(path, encoding='utf-8') as f:
        for line in f:
            words = line.split()
            count += len(words)
    
    return count

print(count_words(data_path))

# 3. Create a dict representing a small "config" (a few string/int/bool
#    keys), write it to a `.json` file with `json.dump`, then read it back
#    with `json.load` into a new variable and assert (with a plain `assert`
#    statement, or just print + eyeball it) that it equals the original
#    dict. Clean up the scratch file afterward with `Path.unlink()`.

json_path = Path(__file__).parent / 'config.json'
config = {
    "enable_payments": True, 
    "amount": 100, 
    "title": "Payment for subscription"
}

with open(json_path, 'w') as f:
    json.dump(config, f, indent=2)
    
    
with open(json_path) as f:
    config_data = json.load(f)

assert config_data == config
json_path.unlink()