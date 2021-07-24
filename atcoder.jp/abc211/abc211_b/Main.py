s = []
for _ in range(4):
    s.append(input())
if 'H' in s:
    if '2B' in s:
        if '3B' in s:
            if 'HR' in s:
                print('Yes')
            else:
                print('No')
        else:
            print('No')        
    else:
        print('No')      
else:
    print('No')