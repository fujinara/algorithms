#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 5;
vector<int> g[N];
vector<int> color(N);
vector<int> parent(N);
int cycle_start, cycle_end;
int n, m;


bool dfs(int v) {
    color[v] = 1;
    for(auto u : g[v]){
        if (color[u] == 0) {
            parent[u] = v;
            if (dfs(u)) {
                return true;
            }
        }
        else if (color[u] == 1) {
            cycle_end = v;
            cycle_start = u;
            return true;
        }
    }
    color[v] = 2;
    return false;
}

void solve() {
    cycle_start = -1;
    
    for (int v = 1; v <= n; v++) {
        if (color[v] == 0 && dfs(v)) {
            break;
        }
    }
    
    if (cycle_start == -1) {
        cout << "NO" << "\n";
    }
    else {
        cout << "YES" << "\n";
        vector<int> cycle;
        for (int v = cycle_end; v != cycle_start; v = parent[v]) {
            cycle.push_back(v);
        }
        cycle.push_back(cycle_start);
        reverse(cycle.begin(), cycle.end());
        for (auto v : cycle) {
            cout << v << " ";
        }
        cout << "\n";
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;
    for(int i = 0; i < m; i++){
       int u, v;
       cin >> u >> v;
       g[u].push_back(v);
    }

    solve();
}