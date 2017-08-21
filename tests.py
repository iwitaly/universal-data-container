from main import Series, DataFrame
import numpy as np
import pandas as pd


print(
    Series(
        [pd.Series([1, 2, 3])]
    )
)


print(DataFrame([
    Series([1, 2, 3]),
    Series([4, 5, 6]),
    Series(['a', 'b', 'c'])
]))