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
