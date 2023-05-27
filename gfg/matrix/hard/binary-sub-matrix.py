"""
Maximum size rectangle binary sub-matrix with all 1s.

Algorithm:

1. Run a loop to traverse through the rows.
2. Now if the current row is not the first row then update the row
   as follows, if matrix[i][j] is not zero then matrix[i][j]=matrix[i-1][j]+matrix[i][j].

3. Find the maximum rectangular area under the histogram, consider the ith row as
   heights of bars of a histogram.

4. Do the previous two steps for all rows and print the maximum area of all the rows.

"""
class Solution:
    def maxHist(self,row):
        # create an empty stack. The stack holds indexes of hist array / 
        # The bars stored in stack are always in increasing order of their heights.
        result=[]
        # top of stack
        top_val=0
        # initialize max area in current
        max_area=0
        # row or histogram
        area=0
        i=0
        while (i<len(row)):
            
