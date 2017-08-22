from main import CustomSeries, CustomDataFrame
import numpy as np
import pandas as pd
from skimage.io import imread


s1 = CustomSeries([pd.Series([1, 2, 3], index=['a', 'b', 'c']),
                   pd.Series([4, 5, 6], index=['d', 'e', 'g'])])
s2 = CustomSeries([1, 2, 3])
s3 = CustomSeries([{"k1": "v1"}, {"k2": 'v2'}])
s4 = CustomSeries([imread('/Users/iwitaly/Downloads/1.jpg')])


df = CustomDataFrame({
    'first': s1,
    'second': s2,
    'third': s3,
    'fourth': s4
})

# df = CustomDataFrame([
#        s1, s2, s3, s4
# ])
# s = df['third']