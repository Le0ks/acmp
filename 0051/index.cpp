#include <iostream>
#include <string>

using namespace std;
int main() {
    int n; cin >> n;
    string s; cin >> s;
    int ans = 1;
    int k = s.length();
    if (n % k == 0) {
        for (int i = k; i <= n; i += k) 
            ans *= i;
    } else {
        for (int i = n; i > 0; i -= k)
            ans *= i;
    }
    cout << ans;
    return 0;
}