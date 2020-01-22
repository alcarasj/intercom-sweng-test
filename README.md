# intercom-sweng-test
A take-home test for a software engineer position at Intercom Dublin.

## Installation
Requires Python >=3.5, `pip3` and `virtualenv` to be installed on your machine.
1. Install `virtualenv` globally using `pip3` with `pip3 install virtualenv`.
2. Create a `virtualenv` named `".venv"` with `virtualenv .venv`.
3. Activate the `virtualenv` with `. .venv/bin/activate`.
4. Install dependencies with `pip3 install -r requirements.txt`.

## Usage
- To run the solution: `make run` 
- To run tests: `make test`

## Tests
Running `make test` tests the solution and dumps coverage files in the directory at `htmlcov`. Within this folder, open `index.html` in browser for coverage percentages, and `main_py.html` for line-by-line coverage.
