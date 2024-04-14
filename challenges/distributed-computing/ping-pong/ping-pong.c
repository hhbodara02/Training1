// Original Author: Wes Kendall
// Copyright 2011 www.mpitutorial.com
// This code is provided freely with the tutorials on mpitutorial.com. Feel
// free to modify it for your own use. Any distribution of the code must
// either provide a link to www.mpitutorial.com or keep this header intact.
//
// Ping pong example with MPI_Send and MPI_Recv. Two processes ping pong a
// number back and forth, incrementing it until it reaches a given value.
//
// Adapted by: Tyler Swann, Osman Haji
// for Monash DeepNeuron HPC Training 2023

#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

int world_rank = 0;
int world_size = 0;

int main(int argc, char** argv)
{
    // Initialize the MPI environment

    // Find out our rank and environemnt size

    // Check we are using 2 nodes

    // Main Implementation

    // Finalize MPI environment
}