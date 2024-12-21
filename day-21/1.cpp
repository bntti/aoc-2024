#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pi = pair<int, int>;

string ppi(pi x) {
  return "{" + to_string(x.first) + ", " + to_string(x.second) + "}";
}

vector<tuple<int, int, char>> dirs = {
    {1, 0, '>'}, {0, 1, 'v'}, {-1, 0, '<'}, {0, -1, '^'}};
vector<char> pos_final = {'7', '8', '9', '4', '5', '6',
                          '1', '2', '3', ' ', '0', 'A'};
vector<char> pos_mid = {' ', '^', 'A', '<', 'v', '>'};

char c_at(pi pos, bool finall) {
  if (finall) {
    if (pos.first < 0 || pos.first >= 3) return ' ';
    if (pos.second < 0 || pos.second >= 4) return ' ';
    return pos_final[pos.first + pos.second * 3];
  }
  if (pos.first < 0 || pos.first >= 3) return ' ';
  if (pos.second < 0 || pos.second >= 2) return ' ';
  return pos_mid[pos.first + pos.second * 3];
}

int solve(string &code) {
  map<char, pair<int, int>> m;
  for (auto dir : dirs) m[get<2>(dir)] = {get<0>(dir), get<1>(dir)};

  set<tuple<int, pi, pi, pi>> visited;
  queue<tuple<int, pi, pi, pi, string>> q;
  q.push({0, {2, 3}, {2, 0}, {2, 0}, ""});

  // v<A<AA>>^AvAA<^A>Av<<A>>^AvA^Av<<A>>^AAv<A>A^A<A>Av<<A>A>^AAAvA<^A>AA
  // <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
  string dbgs = "v<A<AA>>^AvAA<^A>";
  //             <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A

  while (!q.empty()) {
    auto p = q.front();
    q.pop();

    // We -> p3 -> p2 -> p1 -> code
    int i = get<0>(p);
    auto p1 = get<1>(p);
    auto p2 = get<2>(p);
    auto p3 = get<3>(p);
    string s = get<4>(p);

    // bool dbg = s == dbgs;
    // if (dbg) cout << i << " " << s << " " << q.size() << endl;
    // cout << ppi(p1) << " " << ppi(p2) << " " << ppi(p2) << endl;

    if (visited.count({i, p1, p2, p3})) continue;
    visited.insert({i, p1, p2, p3});

    if (i == code.size()) {
      cout << s.size() << " " << s << endl;
      // exit(0);
      return s.size();
    }

    // We move p3
    for (auto dir : dirs) {
      int new_x = p3.first + get<0>(dir);
      int new_y = p3.second + get<1>(dir);
      // if (dbg)
      //   cout << get<2>(dir) << " -> " << new_x << ", " << new_y << ' '
      //        << c_at({new_x, new_y}, false) << endl;
      if (c_at({new_x, new_y}, false) == ' ') continue;
      q.push({i, p1, p2, {new_x, new_y}, s + get<2>(dir)});
    }

    char c3 = c_at(p3, false);
    if (c3 != 'A') {
      // We press A -> p3 pushes (non-A)
      // if (dbg) cout << "A {we, p3} =" << c3 << endl;
      int new_x = p2.first + get<0>(m[c3]);
      int new_y = p2.second + get<1>(m[c3]);
      if (c_at({new_x, new_y}, false) == ' ') continue;
      q.push({i, p1, {new_x, new_y}, p3, s + 'A'});
      continue;
    }

    char c2 = c_at(p2, false);
    if (c2 != 'A') {
      // We and p3 press A -> p2 pushes (non-A)
      // if (dbg) cout << "A {we, p3, p2} =" << c2 << endl;
      int new_x = p1.first + get<0>(m[c2]);
      int new_y = p1.second + get<1>(m[c2]);
      if (c_at({new_x, new_y}, true) == ' ') continue;
      q.push({i, {new_x, new_y}, p2, p3, s + 'A'});
      continue;
    }

    // We, p3, and p2 press A -> p1 pushes
    char c1 = c_at(p1, true);
    // if (dbg)
    //   cout << "A {we, p3, p2, p1} =" << c1 << " == " << code[i] << " " <<
    //   code
    //        << endl;
    if (c1 == code[i]) q.push({i + 1, p1, p2, p3, s + 'A'});
  }
  assert(false);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int n = 5;
  vector<string> v(n);
  for (int i = 0; i < n; ++i) cin >> v[i];

  int res = 0;
  for (int i = 0; i < n; ++i) {
    string s = v[i];
    s.pop_back();
    int x = stoi(s);
    res += solve(v[i]) * x;
  }
  cout << res << endl;
}
