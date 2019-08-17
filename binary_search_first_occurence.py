def first_occurence(array, target):
      left=0
      right=len(array)-1
      while left<right-1:
        mid=(left+right)/2
        if array[mid]<target:
          left=mid+1
        elif array[mid]>target:
          right=mid-1
        else:
          right=mid
      if array[left]==target:
        return left
      if array[right]==target:
        return right
      return 0
