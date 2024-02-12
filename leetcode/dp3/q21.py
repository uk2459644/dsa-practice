nums = [3,2,1,5,6,4]
def merge_sort(nums):
    if len(nums)>1:
        mid=len(nums)//2
        l=nums[:mid]
        r=nums[mid:]
        merge_sort(l)
        merge_sort(r)
        i=0
        h=0
        j=0
        while i<len(l) and j<len(r):
            if l[i]>r[j]:
                nums[h]=l[i]
                i+=1
            else:
                nums[h]=r[j]
                j+=1
            h+=1
        while i<len(l):
            nums[h]=l[i]
            i+=1
            h+=1
        while j<len(r):
            nums[h]=r[j]
            j+=1
            h+=1
                
merge_sort(nums)
print(nums)
