from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:

    def __init__(self):
        self.stack = list()
        self.max_stack = list()
        self.max_val = None

    def empty(self):
        return len(self.stack) == 0

    def max(self):
        return self.max_val

    def pop(self):
        if len(self.stack) == 0:
            return None
        popped = self.stack.pop()
        if popped == self.max_stack[-1]:
            self.max_stack.pop()
            if self.max_stack:
                self.max_val = self.max_stack[-1]
            else:
                self.max_val = None
        return popped

    def push(self, x):
        self.stack.append(x)
        if self.max_val is None or self.max_val <= x:
            self.max_val = x
            self.max_stack.append(x)
        return


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("stack_with_max.py",
                                       'stack_with_max.tsv', stack_tester))
