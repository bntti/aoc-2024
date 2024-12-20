#include <bits/stdc++.h>
using namespace std;
using ll = long long;

constexpr int N = 200;
bool grid[N][N];
bool visited[N][N][2];
int cost[N][N][2];
pair<int, int> sstart;
pair<int, int> eend;
int w, h;

vector<pair<int, int>> dirs = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}, {0, 0}};

// I originally misunderstood the problem such that you could walk through 2
// walls instead of one...
int solve(pair<int, int> cs, pair<int, int> ce) {
  for (int i = 0; i < h; ++i) {
    for (int j = 0; j < w; ++j) {
      for (int k = 0; k < 2; ++k) {
        visited[i][j][k] = 0;
        cost[i][j][k] = 0;
      }
    }
  }

  queue<pair<pair<int, int>, pair<int, int>>> q;
  q.push({sstart, {0, 0}});

  while (!q.empty()) {
    auto p = q.front();
    q.pop();

    int x = p.first.first;
    int y = p.first.second;
    int c = p.second.first;
    int ch = p.second.second;
    if (visited[y][x][ch]) continue;
    visited[y][x][ch] = 1;
    cost[y][x][ch] = c;

    for (auto dir : dirs) {
      int new_x = x + dir.first;
      int new_y = y + dir.second;
      if (new_x < 0 || new_x >= w) continue;
      if (new_y < 0 || new_y >= h) continue;
      if (grid[new_y][new_x]) continue;

      int new_ch = ch;
      if (x == cs.first && y == cs.second && new_x == ce.first &&
          new_y == ce.second)
        new_ch = 1;

      q.push({{new_x, new_y}, {c + 1, new_ch}});
    }
  }
  return cost[eend.second][eend.first][1];
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  cin >> w >> h;

  for (int y = 0; y < h; ++y) {
    string s;
    cin >> s;
    for (int x = 0; x < w; ++x) {
      char c = s[x];
      if (c == '#') grid[y][x] = 1;

      if (c == 'S') sstart = {x, y};
      if (c == 'E') eend = {x, y};
    }
  }

  int base_cost = solve(sstart, sstart) - 1;

  vector<int> total(10000, 0);
  for (int x = 0; x < w; ++x) {
    for (int y = 0; y < h; ++y) {
      if (!grid[y][x]) continue;

      grid[y][x] = 0;

      int cst = solve({x, y}, {x, y}) - 1;
      if (cst > 0 && cst < base_cost) {
        int res = base_cost - cst;
        total[res] += 1;
      }

      grid[y][x] = 1;
    }
  }
  int res = 0;
  for (int i = 0; i < 10000; ++i) {
    if (i >= 100) res += total[i];
    // if (total[i] > 0) cout << i << " " << total[i] << endl;
  }
  cout << res << endl;
}
