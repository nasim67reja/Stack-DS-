

// //////////////////////////////////// Implementing Stack using javascript array ///////////////////////////////////////

class Stack {

    constructor() {
        this.arr = [];
        this.top = -1;
    }

    // methods
    push(val) {
        this.top++;
        this.arr[this.top] = val;
    }

    pop() {
        if (this.empty()) return "stack is empty";
        this.top--;
    }

    peek() {
        if (this.empty()) return "stack is empty";
        return this.arr[this.top];
    }
    empty() {
        if (this.top < 0) return true;
        return false;
    }
}

const test = new Stack()
test.push(2);
test.push(1);
test.pop();

console.log(test.peek());

test.pop();


console.log(test.empty());

console.log(test.pop());


