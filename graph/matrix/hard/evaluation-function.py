"""
Evaluation function : 

The evaluation function is unique for every type of game.
"""
import math

def minimax(currDepth, nodeIndex, maxTurn, scores, targetDepth):
    # base case
    if (currDepth == targetDepth):
        return scores[nodeIndex]
    
    if maxTurn:
        return max(minimax(currDepth+1,nodeIndex*2,False,scores,targetDepth),minimax(currDepth+1,nodeIndex*2+1,False,scores,targetDepth))
    else:
        return min(minimax(currDepth+1,nodeIndex*2,True,scores,targetDepth),minimax(currDepth+1,nodeIndex*2+1,True,scores,targetDepth))



