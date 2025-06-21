class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        result = []

        while i < len(intervals):
            if intervals[i][1] < newInterval[0]:
                result.append(intervals[i])
                i += 1
            
            else:
                break        

        while i < len(intervals):
            if intervals[i][0] <= newInterval[1]:
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
                i += 1

            else:
                break

        result.append(newInterval)

        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result


        

            
        
        