#include <bits/stdc++.h>
using namespace std;
using ll = long long;

constexpr int N = 200;
bool grid[N][N];
int cost[N][N];
bool visited[N][N];
int w, h;

vector<pair<int, int>> dirs = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

bool solve() {
  for (int i = 0; i <= h; ++i) {
    for (int j = 0; j <= w; ++j) visited[i][j] = 0;
  }

  priority_queue<pair<int, pair<int, int>>> q;
  q.push({0, {0, 0}});
  while (!q.empty()) {
    auto p = q.top();
    q.pop();

    int c = -p.first;
    int x = p.second.first;
    int y = p.second.second;
    if (x == w && y == h) return true;

    if (visited[y][x]) continue;
    visited[y][x] = 1;

    for (auto dir : dirs) {
      int new_x = x + dir.first;
      int new_y = y + dir.second;
      if (new_x < 0 || new_x > w) continue;
      if (new_y < 0 || new_y > h) continue;
      if (grid[new_y][new_x]) continue;
      q.push({-(c + 1), {new_x, new_y}});
    }
  }
  return false;
};

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> w >> h >> n;

  vector<pair<int, int>> v;
  for (int i = 0; i < n; ++i) {
    int a, b;
    cin >> a >> b;
    v.push_back({a, b});
  }

  for (int i = 0; i < n; ++i) {
    grid[v[i].first][v[i].second] = true;
    if (!solve()) {
      cout << v[i].first << "," << v[i].second << endl;
      break;
    }
  }
}
