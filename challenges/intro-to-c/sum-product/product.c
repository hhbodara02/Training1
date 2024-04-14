#include "print.h"
#include <stdio.h>

/// `product()` implementation

int main()
{
    int a[] = {1, 2, 3, 4, 5};
    int b[] = {35, -91, 4, 46, 15, 27};

    printf("a = ");
    print(a, 5);
    printf("b = ");
    print(b, 4);

    /// Output implementation

    return 0;
}
