#!/bin/bash

#SBATCH --job-name=
#SBATCH --time=0:05:00
#SBATCH --mem=1GB
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --partition=
#SBATCH --output=slurm-%x.out
#SBATCH --error=slurm-%x.err

. ~/vf38_scratch/spack/share/spack/setup-env.sh
spack load mpich

# Job commands here
