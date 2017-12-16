def merge_sort(a) :
    if (len(a) != 1) :
        half = len(a)//2
        front = merge_sort(a[:half]);
        rear = merge_sort(a[half:]);
        result = merge(front, rear);
        return result;
    return a;
def merge(front, rear) :
    result = list();
    i = 0; j = 0;
    while ((i < len(front)) & (j < len(rear))) :
        if (front[i] <= rear[j]) :
            result.append(front[i]);
            i += 1;
        else :
            result.append(rear[j]);
            j += 1;
    while ((i != len(front)) | (j != len(rear))) :
        if (i == len(front)) :
            result.append(rear[j]);
            j += 1;
        elif (j == len(rear)) :
            result.append(front[i]);
            i += 1;
    return result;

list = []; #리스트 생성
n = int(input()); #1번째 줄에서 리스트의 길이값을 입력받는다.
for i in range(0, n) :
    list += [int(input())]; #2번째 줄부터 n + 1번째 줄까지 값을 받고 리스트로 만든다.

merge_sort(list); #정의된 함수 실행
