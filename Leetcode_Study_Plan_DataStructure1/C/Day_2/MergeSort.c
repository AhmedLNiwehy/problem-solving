#include <stdio.h>
#include <stdlib.h>

void merge(int arr[], int l, int m, int h)
{
    // Create L ← arr[l..m] and M ← arr[m+1..h]
    int s1 = m - l + 1;
    int s2 = h - m;

    int L[s1], M[s2];

    for(int i=0; i<s1; i++)     // L ← arr[l..m]
        L[i] = arr[l+i];

    for(int j=0; j<s2; j++)     // M ← arr[m+1..h]
        M[j] = arr[m+1+j];

    int i=0, j=0, k=l;

    while(i < s1 && j < s2)
    {
        if(L[i] <= M[j])
            arr[k] = L[i++];
        else
            arr[k] = M[j++];
        k++;
    }
    while(i < s1)
        arr[k++] = L[i++];

    while(j < s2)
        arr[k++] = M[j++];
}

void mergeSort(int arr[], int l, int h)
{
    int m;
    if(l < h)
    {
        m = (l + h) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m+1, h);
        merge(arr, l, m, h);
    }
}

void printArray(int arr[], int size)
{
  for (int i = 0; i < size; i++)
    printf("%d ", arr[i]);
  printf("\n");
}

int main()
{
    int arr[6] = {2, 1, 3, 4, 9, 6};
    printArray(arr, 6);
    mergeSort(arr, 0, 5);
    printArray(arr, 6);
    return 0;
}
