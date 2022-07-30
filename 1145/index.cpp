#include <iostream>
#include <cmath>

using namespace std;

int main() {
	long double n = -1, sum = 0, t = 0, x;
	do {
		n++;
		cin >> x;
		sum += x;
		t += x * x;
	} while (x);
	double s = sum / n;
	cout << sqrt((t - 2 * s * sum + s * s * n) / (n - 1));
	return 0;
}