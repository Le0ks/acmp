#include <iostream>

using namespace std;

int main() {
	int k, n; cin >> k >> n;
	int a[n + 1]; a[0] = 1;
	for (int i = 1; i <= n; i++) {
		int sum_ = 0;
		for (int j = 1; j <= min(k, i); j++) {
			sum_ += a[i - j];
		}
		a[i] = sum_;
	}
	cout << a[n];
	return 0;
}