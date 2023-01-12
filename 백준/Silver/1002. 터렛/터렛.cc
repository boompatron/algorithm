#include <iostream>
#include <cmath>
using namespace std;
int calcu() 
{
	double x1, x2, y1, y2, r1, r2;
	cin >> x1;cin >> y1;cin >> r1;
	cin >> x2;cin >> y2;cin >> r2;
	double sum, sub, l;
	sum = abs(r1 + r2);
	sub = abs(r1 - r2);
	l = sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
	if (x1 == x2 && y1 == y2 && r1 == r2)
		return -1;
	else 
	{
		if (sum == l || sub == l)
			return 1;
		else if (sum > l && sub < l)
			return 2;
		else
			return 0;
	}
}
int main()
{
	int count;
	cin >> count;
	int *arr = new int[count];
	for(int i = 0; i < count; i++)
		arr[i] = calcu();
	for (int i = 0; i < count; i++)
		cout << arr[i] << endl;
	delete []arr;
	return 0;
}