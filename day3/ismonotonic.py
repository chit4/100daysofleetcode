#https://leetcode.com/problems/monotonic-array/submissions/


class Solution:
    def isMonotonic(self, A):
        return (all(A[i] <= A[i+1] for i in range(len(A) -1 )) or
                all(A[i] >= A[i+1] for i in range(len(A) -1 )))