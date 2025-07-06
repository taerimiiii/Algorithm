#include <stdio.h>

int main()
{
	int n, m, i, x, y;
	int input_arr[100001] = { 0, };
	int sum_arr[100001] = { 0, };

	scanf("%d %d", &n, &m);
	for (i = 0; i < n; i++) {
		scanf("%d", &input_arr[i]);

		if (i == 0)
			sum_arr[i] = input_arr[i];
		
		else {
			sum_arr[i] = sum_arr[i - 1] + input_arr[i];
		}
	}

	for (i = 0; i < m; i++) {
		scanf("%d %d", &x, &y);

		if (x == 1) {
			printf("%d\n", sum_arr[y - 1]);
		}
		else if (x == y) {
			printf("%d\n", input_arr[x - 1]);
		}
		else {
			printf("%d\n", sum_arr[y - 1] - sum_arr[x - 2]);
		}
	}

	return 0;
}
