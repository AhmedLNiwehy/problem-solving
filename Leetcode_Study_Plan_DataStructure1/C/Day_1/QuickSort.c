#include <stdio.h>
#include <stdlib.h>

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high)
{
    int pivot = arr[high];
    int greater = low - 1;

    for(int j=low; j<high; j++)
    {
        if(arr[j] <= pivot)
        {
            greater++;
            swap(&arr[greater], &arr[j]);
        }
    }
    swap(&arr[greater+1], &arr[high]);
    return(greater+1);
}

void quickSort(int arr[], int low, int high)
{
    if(low < high)
    {
        int part_point = partition(arr, low, high);
        quickSort(arr, low, part_point - 1);
        quickSort(arr, part_point + 1, high);
    }
}

int main()
{
    int arr[] = {1, 3, 0, 5, 8, 9, 2};
    int low = 0;
    int high = (sizeof(arr) / sizeof(arr[0])) - 1;

    printf("Before sorting: ");
    for(int i=0; i<=high; i++)
    {
        printf("%d  ",arr[i]);
    }

    quickSort(arr, low, high);

    printf("\nAfter sorting: ");
    for(int i=0; i<=high; i++)
    {
        printf("%d  ",arr[i]);
    }
    return 0;
}