var isValid = function (s) {
    let stack = []

    const obj = {
        ')': '(',
        '}': '{',
        ']': '[',
    }

    for (let i = 0; i < s.length; i++) {

        if (!Object.keys(obj).includes(s[i])) stack.push(s[i])

        else {
            if (stack.length > 0 && stack[stack.length - 1] === obj[s[i]]) stack.pop()
            else return false
        }
    };

    return stack.length === 0
}

let ans = isValid("()[]{}")
console.log(ans)