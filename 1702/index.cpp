#include <iostream>

using namespace std;

int main() {
    int n; cin >> n;
    int p[n];
    for (int i = 0; i < n; i++) cin >> p[i];
    for (int i = 0; i < n; i++) {
        int m = p[0];
        int m_index = 0;
        for (int j = 0; j < n - i; j++) {
            if (m < p[j]) {
                m = p[j];
                m_index = j;
            }
        }
        cout << m_index << " ";
        swap(p[n - i - 1], p[m_index]);
    }
    return 0;
}