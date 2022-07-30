#include <iostream>
#include <cmath>

using namespace std;

int gcd(int x, int y) {
	while (y %= x) swap(x, y);
	return x;
}

int main() {
	int x, y, f = 0, F = 1; cin >> x >> y;
	x = max(x, y); y = min(x, y);
	for (int i = 2; i <= x; i++) {
		swap(f, F);
		F += f;
		if (i == y) y = F;
		if (i == x) x = F;
	}
	cout << x << y;
	return 0;
}