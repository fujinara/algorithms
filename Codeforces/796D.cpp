#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k, d;
    cin >> n >> k >> d;
    vector<char> visited(n + 1);
    vector<pair<int, int>> adj[n + 1];
    queue<int> q;
    for (int i = 0; i < k; i++) {
        int p;
        cin >> p;
        q.push(p);
        visited[p] = true;
    }
    for (int i = 1; i < n; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back({v, i});
        adj[v].push_back({u, i});
    }

    set<int> needed;
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        for (auto u : adj[v]) {
            if (!visited[u.first]) {
                visited[u.first] = true;
                q.push(u.first);
                needed.insert(u.second);
            }
        }
    }

    cout << n - 1 - (int)needed.size() << "\n";
    for (int i = 1; i < n; i++) {
        if (needed.find(i) == needed.end()) {
            cout << i << " ";
        }
    }
}