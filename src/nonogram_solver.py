#AI project Code fall'24 BS(DS)-1
#Nonogram Puzzle Solver Using Simulated Annealing

#Mohammad Hasnain (462247)
#Mohammad Umar Raza (461532)
#Mohid Arshad (455977)

import random
import math
import turtle

# Generate a random initial state
def random_initial_state(rows, cols):
    return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

# Calculate fitness: Count rows and columns matching constraints
def calculate_fitness(state, row_constraints, col_constraints):
    def check_line(line, constraints):
        result, count = [], 0
        for cell in line:
            if cell == 1:
                count += 1
            elif count > 0:
                result.append(count)
                count = 0
        if count > 0:
            result.append(count)
        return result == constraints

    row_score = sum(check_line(row, row_constraints[i]) for i, row in enumerate(state))
    col_score = sum(check_line([state[r][c] for r in range(len(state))], col_constraints[c]) for c in range(len(state[0])))
    return row_score + col_score

# Simulated Annealing solver with repeated solving
def simulated_annealing(state, row_constraints, col_constraints, max_iter=10000, temp=100):
    rows, cols = len(row_constraints), len(col_constraints)
    best_state = [row[:] for row in state]
    best_fitness = calculate_fitness(state, row_constraints, col_constraints)

    for _ in range(max_iter):
        temp = max(0.01, temp * 0.995)  # Cooling schedule
        next_state = [row[:] for row in state]

        # Flip a random cell
        row_idx = random.randint(0, rows - 1)
        col_idx = random.randint(0, cols - 1)
        next_state[row_idx][col_idx] ^= 1  # Flip the cell

        current_fitness = calculate_fitness(state, row_constraints, col_constraints)
        next_fitness = calculate_fitness(next_state, row_constraints, col_constraints)

        if next_fitness > best_fitness:
            best_state, best_fitness = next_state, next_fitness

        if next_fitness > current_fitness or random.random() < math.exp((next_fitness - current_fitness) / temp):
            state = next_state

    return best_state

# Solve Nonogram until a perfect solution is found
def solve_nonogram_repeatedly(rows, cols, row_constraints, col_constraints):
    state = random_initial_state(rows, cols)
    max_fitness = rows + cols
    
    while calculate_fitness(state, row_constraints, col_constraints) < max_fitness:
        state = simulated_annealing(state, row_constraints, col_constraints)
    
    return state

# Visualize the solution using Turtle graphics
def visualize_solution(state, row_constraints, col_constraints):
    cell_size = 25
    rows, cols = len(state), len(state[0])
    grid_width = cols * cell_size
    grid_height = rows * cell_size

    # Configure turtle
    turtle.speed(0)
    turtle.bgcolor("bisque")
    turtle.penup()
    turtle.hideturtle()

    # Draw the grid background rectangle
    turtle.color("beige")
    turtle.goto(-grid_width // 2, grid_height // 2 - 20)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(grid_width)
        turtle.right(90)
        turtle.forward(grid_height)
        turtle.right(90)
    turtle.end_fill()

    # Display heading
    turtle.goto(0, grid_height // 2 + 70)
    turtle.color("midnightblue")
    turtle.write("Nonogram Puzzle Solver", align="center", font=("Georgia", 18, "bold"))

    # Display column constraints
    for i, col in enumerate(col_constraints):
        for j, num in enumerate(reversed(col)):
            turtle.goto(i * cell_size - cols * cell_size // 2 + 12,
                        rows * cell_size // 2 + (j + 1) * 15 - 27)
            turtle.write(str(num), align="center", font=("Arial", 12, "normal"))

    # Display row constraints
    for i, row in enumerate(row_constraints):
        for j, num in enumerate(reversed(row)):
            turtle.goto(-cols * cell_size // 2 - (j + 1) * 15,
                        (rows - i) * cell_size - rows * cell_size // 2 - 40)
            turtle.write(str(num), align="center", font=("Arial", 12, "normal"))

    # Draw grid cells
    for y, row in enumerate(state):
        for x, cell in enumerate(row):
            start_x = x * cell_size - cols * cell_size // 2 
            start_y = rows * cell_size // 2 - y * cell_size - 20

            # Draw filled cells
            if cell:
                turtle.fillcolor("maroon")
                turtle.begin_fill()
                turtle.goto(start_x, start_y)
                turtle.pendown()
                for _ in range(4):
                    turtle.forward(cell_size)
                    turtle.right(90)
                turtle.end_fill()
                turtle.penup()
            else:
                # Draw crosses for empty cells
                turtle.color("darkgray")
                turtle.penup()
                turtle.goto(start_x, start_y)
                turtle.pendown()
                turtle.goto(start_x + cell_size, start_y - cell_size)
                turtle.penup()
                turtle.goto(start_x + cell_size, start_y)
                turtle.pendown()
                turtle.goto(start_x, start_y - cell_size)
                turtle.penup()

            # Draw cell borders
            turtle.color("gray")
            turtle.goto(start_x, start_y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(cell_size)
                turtle.right(90)
            turtle.penup()

    turtle.done()

# Validate constraints
def validate_constraints(rows, cols, row_constraints, col_constraints):
    def check_constraints(constraints, max_length):
        for line_constraints in constraints:
            min_length = sum(line_constraints) + len(line_constraints) - 1
            if min_length > max_length:
                return False, f"Constraints {line_constraints} exceed maximum length {max_length}."
        return True, "Constraints are valid."

    row_valid, row_message = check_constraints(row_constraints, cols)
    if not row_valid:
        return False, f"Row constraints invalid: {row_message}"

    col_valid, col_message = check_constraints(col_constraints, rows)
    if not col_valid:
        return False, f"Column constraints invalid: {col_message}"

    total_row_blocks = sum(sum(row) for row in row_constraints)
    total_col_blocks = sum(sum(col) for col in col_constraints)
    if total_row_blocks != total_col_blocks:
        return False, (f"Row and column constraints mismatch: "
            f"Total row blocks = {total_row_blocks}, Total column blocks = {total_col_blocks}.")

    return True, "All constraints are valid."

# List of constraint sets
constraints = [
    (
        [[4], [1], [4], [2], [4]],
        [[1], [1, 3], [1, 1, 1], [1, 1, 1], [3, 1]]
    ),
    (
        [[4], [1, 1], [1, 1, 1], [8], [1, 5], [2, 1], [2], [2]],
        [[5], [1, 1], [1, 1], [5], [5], [5], [3], [3]]
    ),
    (
        [[1, 3], [3, 1, 1], [3, 3], [5, 3], [3, 1], [5, 1], [10], [5, 3], [9], [10]],
        [[1, 5], [9], [10], [9], [1, 5], [1, 2], [3, 4], [1, 8], [1, 2, 4], [2, 1, 1]]
    ),
    (
        [[3], [6, 2], [4], [4], [1, 1, 3], [1, 1, 3], [2, 4, 2], [4, 2], [1, 7], [9]],
        [[1, 3, 1], [1, 1, 2], [1, 1], [1, 6], [1, 4], [1, 4], [1, 8], [1, 4, 2], [10], [3, 3]]
    ),
    (
        [[3, 2], [3], [2, 1, 2], [1, 1, 2], [1, 2], [6], [2, 3], [1, 3], [2, 4], [5, 3]],
        [[3], [1, 2, 2], [1, 1, 1], [1, 4, 1], [2, 5], [1, 5], [9], [1, 1, 2], [2, 1], [2, 1]]
    ),
    (
        [[4], [7], [3, 3], [3, 4], [1, 4], [8], [1, 4], [1, 4], [2, 4], [8]],
        [[2, 2], [2, 5], [4, 1], [1, 1, 1], [2, 1, 1], [10], [10], [10], [1, 6], [1]]
    ),
    (
        [[6], [2, 2], [2, 2], [2], [3], [4], [2], [], [2], [2]],
        [[], [2], [3], [1], [1, 2, 2], [1, 2, 2], [1, 2], [6], [4], []]
    )
]

# Randomly select constraints
row_constraints, col_constraints = constraints[6]

# Validate constraints
valid, message = validate_constraints(
    len(row_constraints),
    len(col_constraints),
    row_constraints,
    col_constraints
)
if not valid:
    print(f"Constraint Validation Failed: {message}")
else:
    print(message)
    # Solve and visualize if constraints are valid
    solution = solve_nonogram_repeatedly(len(row_constraints), len(col_constraints), row_constraints, col_constraints)
    visualize_solution(solution, row_constraints, col_constraints)
