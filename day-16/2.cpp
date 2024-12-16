#include <bits/stdc++.h>
using namespace std;
using ll = long long;

constexpr int N = 200;
char grid[N][N];
bool visited[N][N][4];
bool visited2[N][N][4];
bool best[N][N];
int cost[N][N][4];

vector<pair<int, int>> dirs = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int w, h;
  cin >> w >> h;

  for (int y = 0; y < h; ++y) {
    for (int x = 0; x < w; ++x) cin >> grid[y][x];
  }

  priority_queue<pair<int, pair<pair<int, int>, int>>> q;
  q.push({0, {{1, h - 2}, 0}});
  while (!q.empty()) {
    auto p = q.top();
    q.pop();

    int c = -p.first;
    int x = p.second.first.first;
    int y = p.second.first.second;
    int d = p.second.second;

    if (visited[y][x][d]) continue;
    visited[y][x][d] = 1;
    cost[y][x][d] = c;

    q.push({-(c + 1000), {{x, y}, (d + 1) % 4}});
    q.push({-(c + 1000), {{x, y}, (d - 1 + 4) % 4}});

    auto dir = dirs[d];
    int new_x = x + dir.first;
    int new_y = y + dir.second;
    if (grid[new_y][new_x] != '#') q.push({-(c + 1), {{new_x, new_y}, d}});
  }

  int min_cost = 1e9;
  int min_cost_d = -1;
  for (int d = 0; d < 4; ++d) {
    if (cost[1][w - 2][d] < min_cost) {
      min_cost = cost[1][w - 2][d];
      min_cost_d = d;
    }
  }

  queue<tuple<int, pair<int, int>, int>> qq;
  qq.push({min_cost, {w - 2, 1}, min_cost_d});

  int res = 0;
  while (!qq.empty()) {
    auto p = qq.front();
    qq.pop();

    int c = get<0>(p);
    int x = get<1>(p).first;
    int y = get<1>(p).second;
    int d = get<2>(p);

    if (visited2[y][x][d]) continue;
    visited2[y][x][d] = 1;
    if (!best[y][x]) res += 1;
    best[y][x] = 1;

    if (cost[y][x][(d + 1) % 4] == c - 1000)
      qq.push({c - 1000, {x, y}, (d + 1) % 4});
    if (cost[y][x][(d - 1 + 4) % 4] == c - 1000)
      qq.push({c - 1000, {x, y}, (d - 1 + 4) % 4});

    auto dir = dirs[d];
    int new_x = x - dir.first;
    int new_y = y - dir.second;

    if (cost[new_y][new_x][d] == c - 1) qq.push({c - 1, {new_x, new_y}, d});
  }

  cout << res << endl;
}
