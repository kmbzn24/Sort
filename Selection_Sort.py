list = [];
n = int(input());
for i in range(0, n) :
    list += [int(input())];
def selection_sort(array) :
    for i in range(0, len(array)) :
        min = float("inf");
        for j in range(0, len(array) - i) :
            if (array[j] < min) :
                min = array[j];
                loc = j;
        del array[loc];
        array = array + [min];
    for i in range(0, len(array)) :
        print(array[i]);
selection_sort(list);