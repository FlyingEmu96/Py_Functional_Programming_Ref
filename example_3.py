def get_median_font_size(font_sizes):
    if len(font_sizes) == 0:
        return None
    return sorted(font_sizes)[(len(font_sizes) - 1) // 2]

# This function calculates the median font size from a list of font sizes. 
# Step 1: If the input list is empty, it returns None (since no median exists).  
# Step 2: Otherwise, it sorts the list in ascending order.  
# Step 3: It then finds the middle index using integer division 
#         `(len(font_sizes) - 1) // 2`, which works for both odd and even lengths 
#         by picking the lower middle in the even case.  
# Step 4: Finally, it returns the element at that middle index.  
#
# Teaching points:
# 1. Handling edge cases – empty input should be considered.  
# 2. Sorting – ensures values are in order before selecting a median.  
# 3. Integer division `//` – guarantees an integer index, not a float.  
# 4. Simplicity – this is a compact way to get a median, though it 
#    doesn’t compute the exact mean of two middle values in the even case.  
