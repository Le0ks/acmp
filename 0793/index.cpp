#include <iostream>

using namespace std;

bool is_prime(int n) {
    if (n == 1) return false;
    for (int i = 2; i * i <= n; i++)
        if (n % i == 0)
            return false;
    return true;
}

int sum_num(int n) {
    int ans = 0;
    while (n) {
        ans += n % 10;
        n /= 10;
    }
    return ans;
}

int sum_prime_num(int n) {
    int d = 2;
    int ans = 0;
    while (d * d <= n) {
        if (n % d == 0) {
            ans += sum_num(d);
            n /= d;
        } else d++;
    }
    if (n > 1) ans += sum_num(n);
    return ans;
}

int main() {
    int n;
    while (cin >> n) {
        if (is_prime(n)) cout << 0;
        else if (sum_num(n) == sum_prime_num(n)) cout << 1;
        else cout << 0;
    }
    return 0;
}