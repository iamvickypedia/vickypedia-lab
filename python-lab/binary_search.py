import math, sys
itr = 0
def get_midpos(arr,mid):
    arstr = str(arr)
    ind = arstr.replace(",","|",mid-1).find(",")
    if ind > 1:
        ind += 1
    # print(arstr,arstr.count(","),mid,ind)
    return ind

def bin_search(arr,start,end,key):
    global itr
    while start <= end:
        itr += 1
        mid = int(start + (end-start)/2)
        # print(f"iteration:{itr} searchKey:{key} startIndex:{start} endIndex:{end} middleElement:{arr[mid]} subLength:{len(arr[start:end])}")
        print(f"iteration:{itr} searchKey:{key} startIndex:{start} endIndex:{end} middleElement:{arr[mid]}")

        # mid_pos / get_midpos() is just for visual purposes, mid_pos isn't part of Binary Search
        mid_pos = get_midpos(list(arr[start:end+1]),mid-start)

        # print(list(arr[start:end+1]),"startValue:",arr[start],"midValue:",arr[mid])
        print(list(arr[start:end+1]))
        if arr[mid] == key:
            print(" "*mid_pos,u"\u2191") # top
            found = u'\u2713'
            print(f"Found",key,"at location",mid,found)
            return mid
        elif arr[mid] > key:
            print(" "*mid_pos,u"\u2190") # left
            end = mid-1
        else:
            print(" "*mid_pos,u"\u2192") # right
            start = mid+1
    # cross = u'\u274C'
    cross = u'\u2717'
    return f"{key} not found from the given elements {cross}"
    
if __name__ == "__main__":
    try:
        inp = input("Enter the Sorted array elements or enter a range in the format Start-End eg 0-10\n")
        # inp = "1-180"
        # inp = "1 23 25 45 48 56 78 98"
        if "-" in inp:
            start,end,*_ = list(map(int,inp.split("-")))
            arr = range(start,end+1)
        else:
            arr = list(map(int,inp.strip().split()))
            checkArr = sorted(arr)
            if arr != checkArr:
                print("Please enter sorted Elements")
                sys.exit()
        key = int(input("Enter Search Key\n"))
        # key = 100
        start = 0
        end = len(arr) - 1
    except Exception as ex:
        print(ex)
    else:
        # print(arr)
        # arr = [1,23,25,45,48,56,78,98]
        # arr = range(0,50)
        # start, end = 0, len(arr)-1
        # key = 1
        print(bin_search(arr,start,end,key))