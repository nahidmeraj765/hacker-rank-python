def count_substring(supStr, subStr):
    count = 0
    start = 0
    
    while True:
        start = supStr.find(subStr, start) # starting from 0th index
        # find() - get the first index position of a substring 
        
        if start == -1:
            break
        
        count += 1
        start += 1

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)