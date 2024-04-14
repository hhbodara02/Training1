#include "mergesort.h"
#include "check.h"
#include "read.h"

#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int world_rank = 0;
int world_size = 0;

int main(int argc, char** argv)
{
    unsigned N = atoi(argv[1]);
    double* input = (double*)malloc(N * sizeof(double));

    MPI_INIT(&argc, &argv[0]);
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    read_input("./unsorted.txt", &input[0], N);

    // Implementation

    if (check("./sorted.txt", &sorted[0], N))
        puts("Mergsort ran successfully!");
    else
        puts("Mergsort failed!");

    MPI_Barrier(MPI_COMM_WORLD);
    MPI_Finalize();
}
