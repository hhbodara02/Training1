
CC := gcc
FLAGS := -fopenmp

laplace_sequential: jacobi.c laplace2d.c
	${CC} -o laplace-sequential jacobi.c laplace2d.c -lm

laplace_parallel: jacobi.c laplace2d-parallel.c
	${CC} ${FLAGS} -o laplace-parallel jacobi-parallel.c laplace2d-parallel.c -lm

clean:
	rm laplace-sequential rm laplace-parallel