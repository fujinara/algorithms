#include <bits/stdc++.h>
using namespace std;

vector<int> adj[1000500];
vector<char> used(1000500);
int cat[1000500], n, m;
int ans = 0;

void dfs(int v, int cnt=0) {
    cnt = cat[v] == 1 ? cnt + 1 : 0;
    if (cnt > m) {
        return;
    }
    used[v] = true;
    if ((int)adj[v].size() == 1 && v != 1) {
        ans++;
    }
    for (auto i : adj[v]) {
        if (!used[i]) {
            dfs(i, cnt);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;
    for (int i = 1; i <= n; i++) {
        cin >> cat[i];
    }
    for (int i = 1; i < n; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(1);
    cout << ans << "\n";
}