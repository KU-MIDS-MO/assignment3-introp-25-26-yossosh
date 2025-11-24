import numpy as np

def count_values_in_bins(data, bin_edges):
    ### Replace with your own code (begin) ###
    data = np.array(data)
    bin_edges = np.array(bin_edges)
    
    B = len(bin_edges) - 1
    counts = np.zeros(B, dtype=int)
    
    for x in data:
        if x < bin_edges[0] or x > bin_edges[-1]:
            continue
    
        for i in range(B):
            left = bin_edges[i]
            right = bin_edges[i + 1]
        
            if i < B - 1:
                if left <= x < right:
                    counts[i] += 1
                    break
            else:
                if left <= x <= right:
                    counts[i] += 1
                    break
            
    return counts
    ### Replace with your own code (end)   ###
