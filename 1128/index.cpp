#include <iostream>
#include <cmath>

using namespace std;

int main() {
	double x, y; cin >> x >> y;
	int day = 1;
	while (abs(x - y) > 0.01 && x < y) {
		x = x + x * 0.15;
		day++;
	}
	cout << day;
	return 0;
}