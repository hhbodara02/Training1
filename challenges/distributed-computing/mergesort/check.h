#ifndef CHECK_H
#define CHECK_H

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

bool check(char* filename, double* data, unsigned size)
{
    double* compare = (double*)malloc(size * sizeof(double));
    FILE* file = fopen(filename, "r");

    if (file == NULL) {
        printf("Error!");
        exit(1);
    }

    for (int i = 0; i < size; ++i)
        fscanf(file, "%lf", compare + i);

    for (int i = 0; i < size; ++i)
        if (data[i] != compare[i])
            return false;

    fclose(file);
    return true;
}

#endif // CHECK_H
