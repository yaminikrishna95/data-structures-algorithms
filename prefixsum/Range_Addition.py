from typing import List


class Solution:

    def Range_Addition(self, arr,length):
       diff =  [0] * (length+1)
       print(diff)
       for start, stop, inc in arr:
           diff[start] += inc
           diff[stop +1 ] -= inc
       running=0
       final_result=[]
       for i in range(length):
               running += diff[i]
               final_result.append(running)
       return final_result







if __name__ == "__main__":
    arr = [[1,3,2],[2,4,3],[0,2,-2]]
    length=5
    sol = Solution()
    print(sol.Range_Addition(arr,length))