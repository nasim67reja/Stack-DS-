#include <stdio.h>

#include <iostream>
#include <stack>
using namespace std;

bool isValid(string s)
{
    stack<char> st;
    for (int i = 0; i < s.size(); i++)
    {
        char ch = s[i];

        // if opening bracket, push stack

        if (ch == '(' || ch == '{' || ch == '[')
            st.push(ch);

        // if close bracket, stack top check and pop
        else
        {
            // for closing bracket
            if (!st.empty())
            {

                char top = st.top();
                cout << top << endl;
                if ((ch == ')' && top == '(') ||
                    (ch == '}' && top == '{') ||
                    (ch == ']' && top == '['))
                {
                    st.pop();
                }
                else
                    return false;
            }
            else
                return false;
        }
    }
    if (st.empty())
        return true;
    else
        return false;
}

int main()
{
    bool ans = isValid("()[]{}");
    cout << ans;

    return 1;
}