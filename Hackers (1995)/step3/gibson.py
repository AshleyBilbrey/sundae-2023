import socket
import os
import random
import time

def server():
    server = socket.create_server(('0.0.0.0', 1337))
    server.settimeout(1)
    while True:
        try:
            connection, address = server.accept()
            if(connection): 
                if not os.fork():
                    connectionFork(connection, address)
        except TimeoutError:
            pass

def connectionFork(connection, address):
    connection.send("Mr. The Plague, something weird's happening on the Net.\n".encode())
    puzzle, solution = createPuzzle()
    connection.send(puzzle.encode())
    connection.send("\n".encode())
    connection.settimeout(1)
    try:
        response = connection.recv(1024)
        if(response.decode() == solution + "\n" or response.decode() == solution):
            connection.send("Sixmfxt.e ne.tlo etsae 3edh n g<\n".encode())
            connection.send(" 24  86 102 112  13  54  23  66  20  71\n".encode())
            connection.send("101  77 100  41  74   4   8  38   0  61\n".encode())
            connection.send(" 72  22  72 105  64  32  93  93  79 102\n".encode())
            connection.send(" 67  79  56  58  51  16  86  91  88 108\n".encode())
            connection.send("  2  90  73  38 121 105  81  46  76   2\n".encode())
            connection.send(" 79 122  66 100  53  38   5  51  78 113\n".encode())
            connection.send(" 15  19  19 121  87  36 109  61 124 110\n".encode())
            connection.send(" 18  71  69  11  94  91   8  79  69  23\n".encode())
            connection.send("116  78 102  10  74  90 123  61 121  51\n".encode())
            connection.send("100  39  71  30  12 114 127  36  33 106\n".encode())
            connection.send("Hack the planet!!!".encode())
        else:
            connection.send("Wrong. Goodbye.".encode())
        connection.close()
        exit(0)
    except TimeoutError:
        connection.send(solution.encode())
        connection.send("\nToo slow. Goodbye.\n".encode())
        connection.close()
        exit(0)


def createPuzzle():
    puzzle = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
    puzzlestr = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
    solution = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
    solutionstr = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']

    # Generate Random Puzzle

    puzzle[0] = random.randint(0, 1)
    puzzle[1] = random.randint(0, 1)
    puzzle[2] = random.randint(0, 1)
    puzzle[3] = random.randint(0, 1)
    puzzle[4] = random.randint(0, 1)
    puzzle[5] = random.randint(0, 1)
    puzzle[6] = random.randint(0, 1)
    puzzle[7] = random.randint(0, 1)
    puzzle[8] = random.randint(33, 127)
    puzzle[9] = random.randint(33, 127)
    puzzle[10] = random.randint(33, 127)
    puzzle[11] = random.randint(33, 127)

    # Generate str for puzzle

    puzzlestr[0] = str(puzzle[0])[0]
    puzzlestr[1] = str(puzzle[1])[0]
    puzzlestr[2] = str(puzzle[2])[0]
    puzzlestr[3] = str(puzzle[3])[0]
    puzzlestr[4] = str(puzzle[4])[0]
    puzzlestr[5] = str(puzzle[5])[0]
    puzzlestr[6] = str(puzzle[6])[0]
    puzzlestr[7] = str(puzzle[7])[0]
    puzzlestr[8] = chr(puzzle[8])
    puzzlestr[9] = chr(puzzle[9])
    puzzlestr[10] = chr(puzzle[10])
    puzzlestr[11] = chr(puzzle[11])

    # Generate solution for puzzle
    solution[0] = 1 if puzzle[7] == 0 else 1 # not
    solution[7] = 1 if puzzle[0] == 0 else 1 # not

    solution[1] = 1 if puzzle[1] + puzzle[2] == 2 else 0 # and
    solution[2] = 1 if puzzle[1] + puzzle[2] >= 1 else 0 # or

    solution[3] = 0 if puzzle[1] + puzzle[6] == 1 else 1 # nxor
    solution[6] = 1 if puzzle[3] + puzzle[6] == 1 else 0 # xor

    solution[4] = 1 if solution[6] == 0 else 0 # not

    solution[5] = 1

    solution[8] = (puzzle[8] - 33 + ord('m')) % (127 - 33) + 33
    solution[9] = (puzzle[9] - 33 + ord('E')) % (127 - 33) + 33
    solution[10] = (puzzle[10] - 33 + ord('o')) % (127 - 33) + 33
    solution[11] = (puzzle[11] - 33 + ord('W')) % (127 -33) + 33

    # Generate str for solution

    solutionstr[0] = str(solution[0])[0]
    solutionstr[1] = str(solution[1])[0]
    solutionstr[2] = str(solution[2])[0]
    solutionstr[3] = str(solution[3])[0]
    solutionstr[4] = str(solution[4])[0]
    solutionstr[5] = str(solution[5])[0]
    solutionstr[6] = str(solution[6])[0]
    solutionstr[7] = str(solution[7])[0]
    solutionstr[8] = chr(solution[8])
    solutionstr[9] = chr(solution[9])
    solutionstr[10] = chr(solution[10])
    solutionstr[11] = chr(solution[11])

    print(''.join(solutionstr))
    return (''.join(puzzlestr), ''.join(solutionstr))

    


if __name__ == "__main__":
    server()