def is_positive(num):
    if int(num) > 0:
        return True
    else:
        return False


def is_palindromic(num):
    if num == num[::-1]:
        return True
    else:
        return False


n = int(input())
arr_pos = []
arr_pal = []

arr = input().split(' ')

for i in range(n):
    arr_pos.append(is_positive(arr[i]))
    arr_pal.append(is_palindromic(arr[i]))

print(all(arr_pos) and any(arr_pal))
