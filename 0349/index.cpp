#include <iostream>
#include <vector>

using namespace std;

int main() {
    int m, n; cin >> m >> n;
    vector <bool> p(n, true);
    bool flag = true;
    for (int i = 1; i < n; i++) {
        if (p[i]) {
            if (i + 1 >= m) {
                cout << i + 1 << "\n";
                flag = false;
            }
            for (int j = 2 * i + 1; j < n; j += i + 1) {
                p[j] = false;
            }
        }
    }
    if (flag) cout << "Absent";
    return 0;
}