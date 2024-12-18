#include <bits/stdc++.h>
using namespace std;
using ll = long long;

constexpr int N = 200;
bool grid[N][N];
int cost[N][N];
bool visited[N][N];

vector<pair<int, int>> dirs = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int w, h, n;
  cin >> w >> h >> n;

  n = 1024;
  for (int i = 0; i < n; ++i) {
    int a, b;
    cin >> a >> b;
    grid[a][b] = 1;
  }

  priority_queue<pair<int, pair<int, int>>> q;
  q.push({0, {0, 0}});
  while (!q.empty()) {
    auto p = q.top();
    q.pop();

    int c = -p.first;
    int x = p.second.first;
    int y = p.second.second;

    if (visited[y][x]) continue;
    visited[y][x] = 1;
    cost[y][x] = c;

    for (auto dir : dirs) {
      int new_x = x + dir.first;
      int new_y = y + dir.second;
      if (new_x < 0 || new_x > w) continue;
      if (new_y < 0 || new_y > h) continue;
      // cout << grid[new_y][new_x] << endl;
      if (grid[new_y][new_x]) continue;
      q.push({-(c + 1), {new_x, new_y}});
    }
  }
  cout << cost[h][w] << endl;
}
