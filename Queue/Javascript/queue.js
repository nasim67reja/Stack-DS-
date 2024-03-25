class Queue {
    constructor() {
        this.queue = []
    }
    push(data) {
        this.queue.push(data)
    }
    printQu() {
        return this.queue;
    }
    pop() {
        this.queue.shift()
    }
    front() {
        return this.queue[0]
    }
    back() {
        return this.queue[this.queue.length - 1]
    }
    size() {
        return this.queue.length
    }
    empty() {
        return this.queue.length === 0
    }
}

const q = new Queue()
q.push('a')
q.push('b')
q.push('c')

q.pop()
console.log(q.back())
console.log(q.size())
console.log(q.empty())

