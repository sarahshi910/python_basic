def last_occurence(array, target):
      left=0
      right=len(array)-1
      while left<right-1:
        mid=(left+right)/2
        if array[mid]<target:
          left=mid+1
        elif array[mid]>target:
          right=mid-1
        else:
          left=mid
      if array[right]==target:
        return right
      if array[left]==target:
        return left
      return 0
#test case
#print first_occurence([1,2,2,2,4,5,8,13,13],13),last_occurence([1,2,2,2,4,5,8,13,13],13)
