#include <iostream>

using namespace std;

int main() {
    int n; cin >> n;
    int c[n];
    for (int i = 0; i < n; i++) cin >> c[i];
    int ans = 0, max_ = 0;
    for (int i = n - 1; i >= 0; i--) { // важная идея, что можно пройти массив с конца
        max_ = max(c[i], max_);
        ans += max_;
    }
    cout << ans;
    return 0;
}