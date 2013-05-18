# Simple Exercises in Python
These exercises were designed to be run in Python 3+, but should be compatible with 2.7+

# Possible improvements that could be made:
- A more efficient algorithm for searching out neighboring bombs. Execution time for large data sets is currently unacceptable.
- Replace recursion in clearing-the-way.py with an iterative algorithm. Python is not optimized for tail recursion. Iteration is considered a more "pythonic" way of doing things.

# How to make sure they're working:
Running `minesweeper.py` and `clearing-the-way.py` will load the `stdin#.txt` files that are already in the directory with them. The `#` is hard-coded in the script. If you want to add more tests, just jump to the bottom of each script and add the number of the test to the line `for i in (#,)`.

Each script will write out a file called `newout#.txt` that can be compared for accuracy with `stdout#.txt`