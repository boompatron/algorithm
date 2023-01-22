#include <iostream>
using namespace std;
int main(void)
{
    int month, day;
    cin >> month; cin >> day;
    for (int i = month; i > 0; i--) {
        if (i == 2 || i == 4 || i == 6 || i == 8 || i == 9 || i == 11)
            day += 31;
        else if (i == 5 || i == 7 || i == 10 || i == 12)
            day += 30;
        else if (i == 3) 
            day += 28;
        else  //i == 1
            day += 0;
    }
    day--;
    int DoW = day % 7;
    switch (day % 7) {
    case 1:
        cout << "TUE" << endl;
        break;
    case 2:
        cout << "WED" << endl;
        break;
    case 3:
        cout << "THU" << endl;
        break;
    case 4:
        cout << "FRI" << endl;
        break;
    case 5:
        cout << "SAT" << endl;
        break;
    case 6:
        cout << "SUN" << endl;
        break;
    default:
        cout << "MON" << endl;
    }
    return 0;
}