#include <bits/stdc++.h>
using namespace std;
int v, e;
int parent[500001];
int get_parent(int p[], int x){
    if (p[x] != x) {
        p[x] = get_parent(p, p[x]);
    }
    return p[x];
}
void union_parent(int p[], int a, int b){
    a = get_parent(p, a);
    b = get_parent(p, b);
    if (a > b)
        p[a] = b;
    else if (a < b)
        p[b] = a;
    else
        return;
}
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int a, b;
    cin >> v >> e;
    for (int i = 0; i < v; i++){
        parent[i] = i;
    }
    for (int i = 0; i < e; i++){
        cin >> a >> b;
        if (get_parent(parent, a) != get_parent(parent, b))
            union_parent(parent, a, b);
        else {
            cout << i + 1 << endl;
            return 0;
        }
    }
    cout << "0" << endl;
    return 0;
}