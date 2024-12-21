#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pi = pair<int, int>;

string ppi(pi x) {
  return "{" + to_string(x.first) + ", " + to_string(x.second) + "}";
}

// End of tepmlate

string mid_trans_pos(pi a, pi b) {
  string res = "";

  while (a.second < b.second) {
    res += 'v';
    ++a.second;
  }

  while (a.first < b.first) {
    res += '>';
    ++a.first;
  }

  while (a.first > b.first) {
    res += '<';
    --a.first;
  }

  while (a.second > b.second) {
    res += '^';
    --a.second;
  }

  return res;
}

map<char, pi> c_to_mid = {
    {'^', {1, 0}}, {'A', {2, 0}}, {'<', {0, 1}}, {'v', {1, 1}}, {'>', {2, 1}}};
string mid_trans(char ac, char bc) {
  pi a = c_to_mid[ac];
  pi b = c_to_mid[bc];
  return mid_trans_pos(a, b);
}

map<string, int> transition_id;
vector<string> all_transitions;
void init_trans_id() {
  int i = 0;
  transition_id["A"] = i++;
  all_transitions.push_back("A");

  for (int x1 = 0; x1 <= 2; ++x1) {
    for (int y1 = 0; y1 <= 1; ++y1) {
      for (int x2 = 0; x2 <= 2; ++x2) {
        for (int y2 = 0; y2 <= 1; ++y2) {
          if (x1 == x2 && y1 == y2) continue;
          string trans = mid_trans_pos({x1, y1}, {x2, y2});

          if (transition_id[trans + "A"] == 0) {
            all_transitions.push_back(trans + "A");
            transition_id[trans + "A"] = i++;
          }
        }
      }
    }
  }
}

constexpr int T = 30;   // Number of transitions
constexpr int NT = 25;  // Number of middle robots
ll num_trans[T][NT][T]; // Transition after x+1 middle robots, how many of each
                        // transition at the end for the human
ll cost[T];             // Cost of transition
map<string, vector<string>> next_transitions;

void init_num_trans() {
  for (string start_trans : all_transitions) {

    // Init num_trans layer 0
    int id = transition_id[start_trans];
    num_trans[id][0][id] = 1;

    // Init next_transitions
    next_transitions[start_trans] = {};
    char p = 'A';
    for (char c : start_trans) {
      string trans = mid_trans(p, c) + "A";
      next_transitions[start_trans].push_back(trans);
      p = c;
    }
  }

  for (string start_trans : all_transitions) {
    int start_id = transition_id[start_trans];

    for (int t = 1; t < NT; ++t) {
      for (string trans : all_transitions) {
        int trans_id = transition_id[trans];

        for (string next_trans : next_transitions[trans]) {
          int next_id = transition_id[next_trans];
          num_trans[start_id][t][next_id] +=
              num_trans[start_id][t - 1][trans_id];
        }
      }
    }
    ll sum = 0;
    for (string trans : all_transitions) {
      int trans_id = transition_id[trans];
      sum += num_trans[start_id][NT - 1][trans_id] * trans.length();
    }
    cost[start_id] = sum;
  }
}

vector<tuple<int, int, char>> dirs = {
    {1, 0, '>'}, {0, 1, 'v'}, {-1, 0, '<'}, {0, -1, '^'}};
vector<char> pos_final = {'7', '8', '9', '4', '5', '6',
                          '1', '2', '3', ' ', '0', 'A'};

char c_at(pi pos) {
  if (pos.first < 0 || pos.first >= 3) return ' ';
  if (pos.second < 0 || pos.second >= 4) return ' ';
  return pos_final[pos.first + pos.second * 3];
}

ll solve(string &code) {
  set<tuple<int, pi, char>> visited;
  priority_queue<pair<ll, tuple<int, pi, char>>> q;
  q.push({0, {0, {2, 3}, 'A'}});

  while (!q.empty()) {
    auto p = q.top();
    q.pop();

    ll costt = -p.first;
    int i = get<0>(p.second);
    auto pos = get<1>(p.second);
    char prev = get<2>(p.second);

    if (visited.count({i, pos, prev})) continue;
    visited.insert({i, pos, prev});

    if (i == (int)code.size()) return costt;

    // Move
    for (auto dir : dirs) {
      int new_x = pos.first + get<0>(dir);
      int new_y = pos.second + get<1>(dir);
      if (c_at({new_x, new_y}) == ' ') continue;
      string trans = mid_trans(prev, get<2>(dir)) + "A";
      ll c2 = cost[transition_id[trans]];
      q.push({-(costt + c2), {i, {new_x, new_y}, get<2>(dir)}});
    }

    // Press A
    if (c_at(pos) == code[i]) {
      string trans = mid_trans(prev, 'A') + "A";
      ll c2 = cost[transition_id[trans]];
      q.push({-(costt + c2), {i + 1, pos, 'A'}});
    }
  }
  assert(false);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int n = 5;
  vector<string> v(n);
  for (int i = 0; i < n; ++i) cin >> v[i];

  init_trans_id();
  init_num_trans();

  ll res = 0;
  for (int i = 0; i < n; ++i) {
    string s = v[i];
    s.pop_back();
    ll x = stoi(s);
    res += solve(v[i]) * x;
  }
  cout << res << endl;
}
