# 05 — Virtual Environments & pip

This topic has no example.py — it's tooling/workflow, not language syntax.
Do the commands below yourself in a terminal.

## The problem this solves

Node scopes dependencies per-project automatically (`node_modules/`).
Composer does too (`vendor/`). Python does **not** — by default, `pip
install` puts packages in one global location shared by every Python
project on your machine. Two projects needing different versions of the same
package will conflict. A **virtual environment (venv)** is Python's
equivalent of a local `node_modules`/`vendor` — an isolated, per-project
install location.

You create one per project. This is not optional/advanced — it's the
baseline expected workflow for any real Python project.

## Creating and using a venv

```bash
python3 -m venv .venv        # creates a .venv/ folder in the current project — like node_modules, but you name it
source .venv/bin/activate    # macOS/Linux — activates it for the current shell
# .venv\Scripts\activate     # Windows equivalent
```

Once activated, your shell prompt changes (usually shows `(.venv)`), and
`python`/`pip` inside that shell now point at the venv's isolated copies —
completely separate from your system Python and from other projects' venvs.

```bash
deactivate                   # leaves the venv, back to system Python
```

`.venv/` should **always** go in `.gitignore` — never commit it, same as
`node_modules/`.

## pip — Python's npm/composer

With the venv activated:

```bash
pip install requests               # install a package into the active venv
pip install requests==2.31.0       # pin a version
pip uninstall requests
pip list                           # what's installed in this venv
```

## Recording dependencies for others (or your future self)

The classic approach — a plain text `requirements.txt`, closest analog to
`package.json`'s dependency list (but no built-in lockfile-with-tree
semantics like `package-lock.json`):

```bash
pip freeze > requirements.txt      # dump exact installed versions
pip install -r requirements.txt    # install everything listed, e.g. on a fresh clone
```

`requirements.txt` typically looks like:
```
requests==2.31.0
click==8.1.7
```

## Where this fits today

Modern projects increasingly use `pyproject.toml` (the `package.json`
equivalent for metadata + dependencies) plus a faster all-in-one tool like
`uv` or `poetry` that manages the venv *and* dependencies together instead
of doing `venv` + `pip` as two separate manual steps. Those are worth
knowing exist, but `python3 -m venv` + `pip` is the foundational workflow
every Python developer needs first — it's what those tools wrap under the
hood, and it's what you'll find in most existing codebases and tutorials.

## Quick checklist for a new project

```bash
mkdir myproject && cd myproject
python3 -m venv .venv
source .venv/bin/activate
pip install requests
pip freeze > requirements.txt
echo ".venv/" >> .gitignore
```
