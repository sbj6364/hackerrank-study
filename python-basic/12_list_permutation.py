if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    list1 = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if(i+j+k == n):
                    pass
                else:
                    list_tmp = [i, j, k]
                    list1.append(list_tmp)
    print(list1)
                    

