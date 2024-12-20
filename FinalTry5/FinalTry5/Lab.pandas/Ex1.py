import numpy as np

Percentile = [
 (10, 14629), 
 (20 , 25600),
 (30, 37002),
 (40, 50000),
 (50,63179 ),
 (60, 79542),
 (70, 100162),
 (80, 130000),
 (90, 184292)
 ]

percentile_array = np.array(Percentile)

# To print or use the array
print(f"The percentile_array is {percentile_array.ndim} dimensional and has {percentile_array.size} elements.")
