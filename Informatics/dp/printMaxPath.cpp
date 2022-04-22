// https://informatics.msk.ru/mod/statements/view.php?id=656&chapterid=2966#1

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> a(n + 1, vector<int> (m + 1, 0));
    vector<vector<int>> dp(n + 1, vector<int> (m + 1, 0));

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            cin >> a[i][j];
        }
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            dp[i][j] = a[i][j] + max(dp[i - 1][j], dp[i][j - 1]);
        }
    }

    cout << dp[n][m] << "\n";

    stack<char> path;
    int x = n, y = m;
    while (x > 0 && y > 0) {
        if (dp[x - 1][y] + a[x][y] == dp[x][y]) {
            path.push('D');
            x--;
        }
        else {
            path.push('R');
            y--;
        }
    }
    
    path.pop();
    while (!path.empty()) {
        cout << path.top() << ' ';
        path.pop();
    }
}