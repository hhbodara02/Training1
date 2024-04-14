#ifndef MERGESORT_H
#define MERGESORT_H

void merge(double* output, double* input, int left, int middle, int right)
{

    int h = 0;
    int i = 0;
    int j = 0;
    int k = 0;

    h = left;
    i = left;
    j = middle + 1;

    while ((h <= middle) && (j <= right)) {
        if (output[h] <= output[j]) {
            input[i] = output[h];
            h++;
        } else {
            input[i] = output[j];
            j++;
        }

        i++;
    }

    if (middle < h)
        for (k = j; k <= right; k++) {
            input[i] = output[k];
            i++;
        }
    else
        for (k = h; k <= middle; k++) {
            input[i] = output[k];
            i++;
        }

    for (k = left; k <= right; k++)
        output[k] = input[k];
}

void mergesort(double* output, double* input, int left, int right)
{

    int middle = 0;

    if (left < right) {
        middle = (left + right) / 2;

        mergesort(output, input, left, middle);
        mergesort(output, input, (middle + 1), right);
        merge(output, input, left, middle, right);
    }
}

#endif // MERGESORT_H
