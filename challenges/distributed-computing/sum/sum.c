#include "read.h"

#include <mpi.h>
#include <stdio.h>

int world_size = 0;
int world_rank = 0;

MPI_Status status;

int main(int argc, char* argv[])
{
    unsigned N = atoi(argv[1]);
    double* input = (double*)malloc(N * sizeof(double));

    MPI_Init(&argc, &argv);

    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    read_input("./input.txt", &input[0], N);

    // Implementation

    MPI_Finalize();

    return 0;
}