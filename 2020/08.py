from aocd import data, submit

program = data.splitlines()


def execute(acc=0, pc=0):
    run = set()
    while True:
        if pc in run:
            return False, acc
        elif pc == len(program):
            return True, acc

        operation, arg = program[pc].split(" ")
        arg = int(arg)
        run.add(pc)

        if operation == "nop":
            pc += 1
        elif operation == "jmp":
            pc += arg
        elif operation == "acc":
            acc += arg
            pc += 1


def find(acc=0, pc=0):
    run = set()
    while True:
        operation, arg = program[pc].split(" ")
        arg = int(arg)
        run.add(pc)

        if operation == "nop":
            attempt = execute(acc, pc + arg)
            if attempt[0]:
                return attempt[1]
            pc += 1
        elif operation == "jmp":
            attempt = execute(acc, pc + 1)
            if attempt[0]:
                return attempt[1]
            pc += arg
        elif operation == "acc":
            acc += arg
            pc += 1


submit(execute()[1], part='a')
submit(find(), part='b')
