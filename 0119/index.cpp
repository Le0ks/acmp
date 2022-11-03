#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n; cin >> n;
    vector <vector<int>> p(n, vector <int> (3));
    for (int i = 0; i < n; i++) cin >> p[i][0] >> p[i][1] >> p[i][2];
    for (int i = 0; i < n; i++) {
        int m = p[0][0] * 3600 + p[0][1] * 60 + p[0][2];
        int m_index = 0;
        for (int j = 0; j < n - i; j++) {
            int s = p[j][0] * 3600 + p[j][1] * 60 + p[j][2];
            if (s > m) {
                m = s;
                m_index = j;
            }
        }
        swap(p[n - i - 1], p[m_index]);
    }
    for (int i = 0; i < n; i++) cout << p[i][0] << " " << p[i][1] << " " << p[i][2] << "\n";
    return 0;
}