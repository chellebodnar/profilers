Profiling code is cool.  One way to do this is to count how many times particular lines of code or functions are run, in order to identify spots where optimizations can be made.

C++profiler.py reads in C++ code and insert statements following each opening curly brace, so it tracks how many times each function or loop is run.  It assumes all classes are defined prior to main() and that the last statement in main() is "return endOfMain;".  This just made the syntax a bit easier.

Run your code in the usual way.  At the end, you'll get a printout of how many times lines after opening curly braces were run.

pythonProfiler.py does a similar thing, but with Python code.  Instead of looking for opening curly braces, it looks for colons at the end of a line.
