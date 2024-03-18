#include <stdio.h>

#include <iostream>
// #include <stack>
using namespace std;

///////////////////////////////////  Createing Stack using array /////////////////////////////

class Stack
{
public:
    int *arr;
    int size;
    int top;
    Stack(int size)
    {
        this->size = size;
        arr = new int[size];
        top = -1;
    }

    // methods

    void push(int element)
    {
        if (size - top > 1)
        {
            top++;
            arr[top] = element;
        }
        else
            cout << "Stack Overflow" << endl;
    }

    void pop()
    {
        if (top >= 0)
        {
            top--;
        }
        else
            cout << "Stack Underflow" << endl;
    }

    int peek()
    {
        if (top >= 0 && top < size)
            return arr[top];
        else
        {
            cout << "Stack is Empty" << endl;
            return -1;
        }
    }

    bool isEmpty()
    {
        if (top == -1)
            return true;
        else
            return false;
    }
};

int main()
{

    Stack st(5);
    st.push(1);
    st.push(2);
    st.push(3);

    while (!st.isEmpty())
    {
        cout << st.peek() << " ";
        st.pop();
    }

    // stack<int> stack;

    // stack.push(1);
    // stack.push(2);
    // stack.push(3);

    // while (!stack.empty())
    // {
    //     cout << stack.top() << " ";
    //     stack.pop();
    // }

    return 1;
}