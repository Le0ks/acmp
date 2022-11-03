#include <iostream>

using namespace std;

int c_div(int n) {
    int ans = 0;
    int d = 2;
    while (d * d <= n) {
        if (n % d == 0) {
            ans++;
            n /= d;
        } else {
            d++;
        }
    }
    if (n > 1) ans++;
    return ans;
}

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

int main() {
    int n, m; cin >> n >> m;
    int  t = gcd(n, m);
    cout << c_div(m / t) + c_div(n / t);
    return 0;
}