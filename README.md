# Advent of Code 2020
Puzzles and Solutions for the Advent of Code puzzle, December 1-25, 2020.


## Layout of this Repo

`*.txt` - Problem statement files

`Pipfile` - Python requirements for solutions and testing (pipenv)

`data/*.in` - Input text / data for problem statements

`python/dayNNN.py` - Python solutions for each day's challenge

`python/tests/test_dayNNN.py` - Pytest unit tests for Python solutions


#### NOTE: Other language solutions may be added in the future under appropriate subdirectories.


## Testing

To run the pytest unit tests:
- Clone this repo
- Install Pipenv (https://pipenv.pypa.io/en/latest/install/#installing-pipenv)
- Within the cloned directory, run `pipenv install`
- Run `pipenv run pytest` or `pipenv shell` and then `pytest`

To run the solutions:

Each solution is written as both a module and a script. Simply run each Python file on the command line or via the IDE tool of your choice (i.e. `python python/day001.py`). Note that some solutions may potentially require parameters passed on the command line and will be documented as such.
