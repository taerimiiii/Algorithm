#include <stdio.h>

int is_prime(int n);

int main()
{
	int arr[10][10];
	int i, j;

	for (i = 0; i < 9; i++) {
		for (j = 0; j < 9; j++)
			scanf("%d", &arr[i][j]);
	}

	int max_val = arr[0][0], row = 0, col = 0;
	for (i = 0; i < 9; i++) {
		for (j = 0; j < 9; j++) {
			if (max_val < arr[i][j]) {
				max_val = arr[i][j];
				row = i;
				col = j;
			}
		}
	}

	printf("%d\n%d %d", max_val, row + 1, col + 1);

	return 0;
}