# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `src/pydbmtools/main.py:21` - `dump` opens files only with `dbm.gnu.open`, so it fails with `dbm.gnu.error` on ndbm and dumb-dbm files - the very formats `pyproject.toml:19-21` advertises (`ndbm`, `shelve`). Use `dbm.open(filename, "r")` (it detects the backend via `dbm.whichdb`) and iterate `db.keys()` instead of the gdbm-only `firstkey`/`nextkey`.

## Medium

- `src/pydbmtools/main.py:16-20` - `max_free_args=2` with no `min_free_args`: running `pydbmtools dump` with no file crashes with `IndexError` at `get_free_args()[0]`, and a second argument is accepted but ignored. Set `min_free_args=1, max_free_args=1`.
- `src/pydbmtools/configs.py:7-12` - `ConfigPrint.full` ("full dumps or just id?") is never wired in: `dump` registers `configs=[]` (`main.py:15`) and always prints key, length and type. Either pass `configs=[ConfigPrint]` and print the value when `full` is set, or delete `configs.py` (and its entry in `sphinx/pydbmtools.rst:7-13`).
- `tests/unit_tests/test_basic.py:20-28` - the only tests are import checks; `dump` is never exercised. Add a test that writes a small dbm file to `tmp_path` and checks the `dump` output.

## Low

- `doc/TODO.txt:1` - "implement the basic dump functionality" is stale: `dump` exists (`main.py:19`). Replace with the real remaining work (value printing, non-gdbm support) or delete the file.
- `pyproject.toml:86` - `mypy_path = "src:python:scripts"` names `python/` and `scripts/`, which do not exist here (the same line is in 82 fleet pyproject files, so fix it at the source that seeds them); set `"src"`.
- `src/pydbmtools/__init__.py:5` - `LOGGER_NAME` duplicates `static.py:5` (generated from config) and nothing reads either; drop the hand-written copy.
