#include <bits/stdc++.h>
using namespace std;
using ll = long long;

constexpr int N = 200;
bool grid[N][N];
bool visited[N][N];
int cost[N][N];
bool pvisited[N][N];
pair<int, int> sstart;
pair<int, int> eend;
int w, h;

vector<pair<int, int>> dirs = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

void init() {
  queue<pair<pair<int, int>, int>> q;
  q.push({sstart, 0});

  while (!q.empty()) {
    auto p = q.front();
    q.pop();

    int x = p.first.first;
    int y = p.first.second;
    int c = p.second;
    if (visited[y][x]) continue;
    visited[y][x] = 1;
    cost[y][x] = c;

    for (auto dir : dirs) {
      int new_x = x + dir.first;
      int new_y = y + dir.second;
      if (new_x < 0 || new_x >= w) continue;
      if (new_y < 0 || new_y >= h) continue;

      if (grid[new_y][new_x]) continue;
      q.push({{new_x, new_y}, c + 1});
    }
  }
}

int solve(pair<int, int> s) {
  if (grid[s.second][s.first]) return 0;
  int sc = cost[s.second][s.first];

  int total = 0;
  for (int xd = -20; xd <= 20; ++xd) {
    for (int yd = -20; yd <= 20; ++yd) {

      int x = s.first + xd;
      int y = s.second + yd;
      int c = abs(xd) + abs(yd);
      if (c > 20) continue;
      if (x < 0 || x >= w) continue;
      if (y < 0 || y >= h) continue;
      if (grid[y][x]) continue;

      assert((x == sstart.first && y == sstart.second) || cost[y][x] > 0);
      int res = cost[y][x] - sc - c;
      // if (res >= 74)
      //   cout << "Res: " << res << ", s: {" << s.first << ", " << s.second
      //        << "} ";
      // if (res >= 74)
      //   cout << "e: {" << x << ", " << y << "} c: " << c << " " << cost[y][x]
      //        << " - " << sc << endl;
      if (res >= 100) total += 1;
    }
  }
  return total;
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

  init();

  int res = 0;
  for (int x = 0; x < w; ++x) {
    for (int y = 0; y < h; ++y) {
      res += solve({x, y});
    }
  }
  cout << res << endl;
}
