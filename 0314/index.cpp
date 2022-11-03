#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n; cin >> n;
    string k; cin >> k;
    vector <string> p(n);
    for (int i = 0; i < n; i++) {
        p[i] = to_string(i + 1);
    }
    int ans =0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (p[j] > p[j + 1])
                swap(p[j], p[j + 1]);
            if (p[j] == k)
                ans = j + 1;
            if (p[j + 1] == k)
                ans = j + 2;
        }
    }
    cout << ans;
    return 0;
}