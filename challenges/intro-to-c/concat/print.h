#ifndef PRINT_H
#define PRINT_H

#include <stdio.h>

void print(int arr[], unsigned int sz)
{
    printf("{ ");
    for (unsigned int i = 0; i < sz - 1; ++i)
        printf("%d, ", arr[i]);

    printf("%d }\n", arr[sz - 1]);
}

#endif /// PRINT_H
