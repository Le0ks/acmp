#include <iostream>

using namespace std;

int main() {
    int n; cin >> n;
    int p[n]; int ans = 0;
    for (int i = 0; i < n; i++) cin >> p[i];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - 1; j++)
            if (p[j] > p[j + 1]) {
                swap(p[j], p[j + 1]);
                ans++;
            }
    }
    cout << ans << "\n";
    for (int i = 0; i < n; i++) cout << p[i] << " ";
    return 0;
}