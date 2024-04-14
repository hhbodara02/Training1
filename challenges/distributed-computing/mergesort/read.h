#ifndef READ_H
#define READ_H

#include <stdio.h>
#include <stdlib.h>

void read_input(char* filename, double* data, unsigned size)
{
    FILE* file = fopen(filename, "r");

    if (file == NULL) {
        printf("Error!");
        exit(1);
    }

    for (int i = 0; i < size; ++i)
        fscanf(file, "%lf", data + i);

    fclose(file);
}

#endif // READ_H
