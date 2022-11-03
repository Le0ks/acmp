#include <iostream>

using namespace std;

bool is_prime(int n) {
    for (int i = 2; i * i <= n; i++)
        if (n % i == 0)
            return false;
    return true;
}

int next_prime(int n) {
    while (true) {
        if (is_prime(++n)) return n;
    }
}

int main() {
    int n; cin >> n;
    while (n > 1) {
        int prime = next_prime(n);
        int l = prime - n;
        int cnt = 0;
        for (int i = l; i <= (n + l) / 2; i++)
            cout << i << " " << n - cnt++ << "\n";
        n = l - 1;
    }
    return 0;
}