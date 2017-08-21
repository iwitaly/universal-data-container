from main import Series, DataFrame
import numpy as np
import pandas as pd


print(
    Series(
        [1, 2, 3]
    ).get_type()
)


d = DataFrame({
    'a': Series([1, 2, 3]),
    'b': Series([4, 5, 6]),
    'c': Series(['a', 'b', 'c'])
})

print(
    d.filter_by_type(np.int64)
)

print(
    isinstance(int, np.int64)
)