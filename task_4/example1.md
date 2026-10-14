# Question 1: Check Whether a Number Is Even or Odd

## 1. Question
Write a C program to input an integer and check whether it is even or odd.

## 2. Solution

```c
#include <stdio.h>

int main()
{
    int n;

    printf("Enter a number: ");
    scanf("%d", &n);

    if (n % 2 == 0)
    {
        printf("The number is even.\n");
    }
    else
    {
        printf("The number is odd.\n");
    }

    return 0;
}
```

## 3. Explanation

1. `#include <stdio.h>` includes the standard input/output library.
2. `int n;` declares an integer variable to store the input.
3. `scanf("%d", &n);` accepts an integer from the user.
4. `n % 2` calculates the remainder when `n` is divided by 2.
5. If the remainder is `0`, the number is even; otherwise, it is odd.
6. `return 0;` indicates that the program has executed successfully.

## 4. Sample Input

```text
Enter a number: 7
```

## 5. Sample Output

```text
The number is odd.
```

## 6. Time and Space Complexity

- **Time Complexity:** O(1), because the program performs a constant number of operations.
- **Space Complexity:** O(1), because it uses a constant amount of memory.
