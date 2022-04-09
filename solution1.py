# Write code for algorithm 1 below

def recursive(n):
    if n == 0:
        return
    else:
        print(n)
        recursive(n - 1)

n = 6
recursive(n)

