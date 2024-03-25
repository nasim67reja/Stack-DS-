#include <iostream>
#include <vector>
using namespace std;

class Queue
{
public:
    vector<int> v;

    Queue()
    {
        this->v = {};
    };

    void push(int val)
    {
        this->v.push_back(val);
    };
    void pop()
    {
        if (!this->v.empty())
            this->v.erase(this->v.begin());
        else
            cout << "Queue is empty" << endl;
    };
    int front()
    {
        return this->v[0];
    }
};

int main()
{
    Queue q;
    q.push(1);
    q.push(2);
    q.push(3);
    q.pop();
    cout << q.front() << endl;
    return 1;
}