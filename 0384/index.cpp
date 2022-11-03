#include <iostream>

using namespace std;

int gcd(int a, int b) {
	if (b == 0) return a;
	return gcd(b, a % b);
}

int main() {
	int i, j; cin >> i >> j;
	long long f_prev = 0, f_now = 1;
	for (int x = 2; x <= gcd(i, j); x++) {
		long long f = (f_now + f_prev) % 1000000000;
		f_prev = f_now;
		f_now = f;
	}
	cout << f_now;
	return 0;
}