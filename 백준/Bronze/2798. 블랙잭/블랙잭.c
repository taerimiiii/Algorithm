#include <stdio.h>

int main()
{
	int n, m, i, j, k, sum = 0, near_val = 0;
	int arr[100];

	scanf("%d %d", &n, &m);
	for (i = 0; i < n; i++)
		scanf("%d", &arr[i]);

	for (i = 0; i < n - 2; i++) {
		for (j = i + 1; j < n - 1; j++) {
			for (k = j + 1; k < n; k++) {
				sum += arr[i] + arr[j] + arr[k];

				if (m - sum >= 0) {
					if (sum > near_val) {
						near_val = sum;
					}
				}

				sum = 0;
			}
		}
	}

	printf("%d", near_val);

	return 0;
}