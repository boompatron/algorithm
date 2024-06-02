#include <iostream>
#include <vector>
#include <queue>

using namespace std;
using edge = pair<int, int>; // weight, enode
using pq = priority_queue<edge, vector<edge>, greater<edge>>;

vector<vector<edge> > matrix;

int dijkstra(vector<int> dist, pq myPQ, vector<bool> _visited, int _target) {
	while (!myPQ.empty()) {
		edge top = myPQ.top();
		myPQ.pop();

		int snode = top.second;
		int sdistance = top.first;

		if (snode == _target) {
			return dist[_target];
		}

		if (_visited[snode]) continue;
		_visited[snode] = true;

		for (edge i : matrix[snode]) {
			int enode = i.second;
			int weight = i.first;

			if (!_visited[enode] && dist[enode] > sdistance + weight) {
				dist[enode] = sdistance + weight;
				myPQ.push({ dist[enode], enode });
			}
		}
	}
	return -1;
}

int main(void) {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int N, E;
	cin >> N >> E;

	matrix.resize(N + 1);

	for (int i = 0; i < E; i++) {
		int a, b, c;
		cin >> a >> b >> c;

		matrix[a].push_back({ c, b });
		matrix[b].push_back({ c, a });
	}

	int targ1, targ2;
	cin >> targ1 >> targ2;

	vector<int> distance(N + 1, 100000000);
	distance[1] = 0;

	pq myQ;
	myQ.push({ 0, 1 });

	vector<bool> visited(N + 1, false);

	int dv1 = dijkstra(distance, myQ, visited, targ1);
	int dv2 = dijkstra(distance, myQ, visited, targ2);

	fill(distance.begin(), distance.end(), 100000000);
	distance[targ1] = 0;

	myQ = {};
	myQ.push({ 0, targ1 });

	int dv12 = dijkstra(distance, myQ, visited, targ2);
	int dv1N = dijkstra(distance, myQ, visited, N);

	fill(distance.begin(), distance.end(), 100000000);
	distance[targ2] = 0;

	myQ = {};
	myQ.push({ 0, targ2 });

	int dv21 = dijkstra(distance, myQ, visited, targ1);
	int dv2N = dijkstra(distance, myQ, visited, N);

	int answer = 1000000000;
	if (dv1 != -1 && dv12 != -1 && dv2N != -1) {
		answer = min(answer, dv1 + dv12 + dv2N);
	}
	if (dv2 != -1 && dv21 != -1 && dv1N != -1) {
		answer = min(answer, dv2 + dv21 + dv1N);
	}

	if (answer == 1000000000) {
		cout << -1;
	}
	else {
		cout << answer;
	}

	return 0;
}