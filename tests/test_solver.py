import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.nonogram_solver import calculate_fitness, random_initial_state

def test_fitness_int():
    rows = cols = 5
    row = [[1], [1], [1], [1], [1]]
    col = [[1], [1], [1], [1], [1]]
    state = random_initial_state(rows, cols)
    score = calculate_fitness(state, row, col)
    assert isinstance(score, int)

if __name__ == "__main__":
    test_fitness_int()
    print("✓ fitness returns int")