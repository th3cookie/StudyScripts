def maxSequence(arr):
        max_now = 0
        max_end = 0
        for i in range(len(arr)):
            max_now = max(arr[i], max_now + arr[i])
            max_end = max(max_end, max_now)
        return max_end