#include <bits/stdc++.h>
#include <cstdlib>
using namespace std;
using ll = int64_t;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  ll N, K, Q;
  cin >> N >> K >> Q;
  vector<ll> xors(N);
  // vector<ll> xorsplus762(N);
  // vector<ll> xorsneg(N);
  ll curr = 0;
  // ll currplus762 = 0;
  // ll currneg = 0;
  for (ll i = 0; i < N; i++) {
    ll x;
    cin >> x;
    curr ^= x;
    // currplus762 ^= (x + 1);
    // currneg ^= (x*3);
    xors[i] = curr;
    // xorsplus762[i] = currplus762;
    // xorsneg[i] = currneg;
  }
  // for (auto x : xors) {
  //     cerr << x << " ";
  // }
  // cerr << "\n";

  auto xorsfixed = [](const vector<ll> &xors, ll i) {
    if (i < 0)
      return (ll)0;
    if (i >= xors.size())
      return xors[xors.size() - 1];
    return xors[i];
  };

  for (ll i = 0; i < Q; i++) {
    ll l, r;
    cin >> l >> r;
    ll m = l - 2, n = r - 1;
    // cerr << m << ": " << xorsfixed(m) << "\n";
    // cerr << n << ": " << xorsfixed(n) << "\n";
    ll res = (xorsfixed(xors, m) ^ xorsfixed(xors, n));
    // ll res = 0;
    cout << res << "\n";
  }
}