'''
Using doctest
We just learned about doctest, which, if you're writing full docstrings with examples, is a simple way to minimally test your functions. In this exercise, you'll get some hands-on practice testing and debugging with doctest.

The following have all be pre-loaded in your environment: doctest, Counter, and text_analyzer.

Note that your docstring submission must match the solution exactly. If you find yourself getting it wrong several times, it may be a good idea to refresh the sample code and start over.

Instructions
100 XP
Complete the input code of the example in the docstring for sum_counters.
Complete the docstring example by filling in the expected output.
Run the testmod function from doctest to test your function's example code.
'''
SOLUTION

def sum_counters(counters):
    """Aggregate collections.Counter objects by summing counts

    :param counters: list/tuple of counters to sum
    :return: aggregated counters with counts summed

    >>> d1 = text_analyzer.Document('1 2 fizz 4 buzz fizz 7 8')
    >>> d2 = text_analyzer.Document('fizz buzz 11 fizz 13 14')
    >>> sum_counters([d1.word_counts, d2.word_counts])
    Counter({'fizz': 4, 'buzz': 2})
    """
    return sum(counters, Counter())

doctest.testmod()