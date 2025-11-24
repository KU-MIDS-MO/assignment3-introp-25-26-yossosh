import numpy as np

def clean_and_scale_scores(scores, min_score, max_score):
    ### Replace with your own code (begin) ###
    scores = np.array(scores, dtype=float)
    
    scores[scores < min_score] = min_score
    scores[scores > max_score] = max_score
    
    scaled_scores = (scores - min_score) / (max_score - min_score)
    return scaled_scores
    
    ### Replace with your own code (end)   ###
clean_and_scale_scores([8,9,2,10,5,6,9,9,11,2,3,12], 4, 10)
