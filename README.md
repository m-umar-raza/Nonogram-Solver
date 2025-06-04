# 🖼️ Nonogram Puzzle Solver – “Picture Logic made Easy”

Welcome! This tiny **Python** project shows you how a computer can **solve Nonogram puzzles** (also called *Picross* or *Paint‑by‑Numbers*).  
If you have never heard of a Nonogram, don’t worry – by the end of this README you’ll both **understand the puzzle** *and* know how our code cracks it.

---

## 📌 1. What is a Nonogram?

A **Nonogram** is a grid of empty squares. Numbers next to each **row** and **column** tell you how many squares must be filled in and in which groups.

Example 5 × 5 puzzle:

```
Row clues →   Col clues ↓
        2               1 1
    1   1               3
1   3   1   1           1
    1   1           1   1
        4               5
```

Your job is to shade squares so every row & column matches its clues.  
Do it right and a little image appears – like 8‑bit pixel art!

---

## 🔍 2. Why did we build a solver?

* Fun final‑year AI assignment (see **docs/** for our report & slides).
* Great demo of **Simulated Annealing** – a famous optimisation trick.
* Lets you verify puzzles automatically or generate puzzle art quickly.

---

## 🛠️ 3. How does the program work? (Plain English)

1. **Guess first, ask later** – start with a *random* grid (some squares filled, others blank).
2. **Score the guess** – compare every row & column to its clues.  
   More matched clues = higher score.
3. **Tweak one square** – flip a random cell (filled ➞ blank or vice‑versa).
4. **Keep or Throw?**  
   * If the tweak makes the score *better*, keep it.  
   * If it’s worse, maybe still keep it *early on* (our “metal is hot”).  
   * As the “temperature” cools, we become pickier, only keeping good moves.
5. **Repeat** until all clues satisfied → puzzle solved, image revealed! 🎉

This “heat & cool” approach is called **Simulated Annealing**. Think of heating metal so atoms can move, then slowly cooling to lock them into a perfect crystal.

---

## 🚀 4. Quick Start – Run the Demo

> Works with **Python 3.8+** – no extra packages to install.

```bash
# 1. Get the code
git clone https://github.com/your‑username/NonogramSolver.git
cd NonogramSolver

# 2. Run the built‑in sample puzzle
python src/nonogram_solver.py
```

You’ll see a simple text progress bar in the terminal and, at the end, a neat **ASCII picture** of the solved grid.

*Optional bonus*: Open the script and switch `VISUALISE = True` to watch the grid solve live using the built‑in `turtle` graphics window (fun!).

---

## 🖋️ 5. Solve **your** puzzle

1. Find the section at the bottom of `src/nonogram_solver.py` labelled `### EDIT BELOW FOR CUSTOM PUZZLE ###`.
2. Replace the example **row_clues** and **col_clues** with your own numbers.
3. Save & run again – voilà, instant solution.

Tip: keep row clues and column clues the same length as your grid size (e.g. 10 clues each for a 10×10 puzzle).

---

## 🗂️ 6. Project Files Explained

| Path | What’s inside? |
|------|----------------|
| `src/nonogram_solver.py` | **All** the Python logic – easy to read & edit. |
| `docs/research_paper.pdf` | Short paper describing algorithm choices and results. |
| `docs/full_report.docx` | Long write‑up for the course (methodology, tests, screenshots). |
| `docs/class_presentation.pptx` | Slides from our classroom demo. |
| `tests/test_solver.py` | Tiny automated test: make sure scoring works. |
| `README.md` | This guide – shareable with beginners & teachers. |
| `LICENSE` | MIT – free for everyone. |

---

## ⚙️ 7. Under the Hood (for curious minds)

* **State representation**: 2D list of 0 (blank) / 1 (filled).  
* **Fitness function**: Counts how many row & column clues are satisfied.  
* **Annealing schedule**:  
  * Start temperature = `1.0`  
  * Cool rate = `0.995` per iteration  
  * Stop when temperature < `0.01` *or* perfect score achieved.  
* **Runtime**: Around 1–2 s for a 15 × 15 puzzle on a typical laptop.

---

## ❓ 8. FAQ

**Q:** Do I need NumPy or fancy libraries?  
**A:** Nope! Pure Python.

**Q:** Does it always find a solution?  
**A:** Yes – if the clues describe a valid puzzle. For nearly‑impossible puzzles, you can raise `MAX_ITER`.

**Q:** Can I make it faster?  
**A:** Sure – tune `COOL_RATE`, limit neighbourhood flips, or parallelise rows.

---

## 🤲 9. Contributing & Feedback

* **Bug report?** Open an *Issue* on GitHub.  
* **Have an idea?** Fork → branch → pull request.  
* We happily accept improvements, especially clearer comments or GUI demos.

---

## 📜 10. License

Released under the **MIT License** – you can reuse, remix, and share freely.

---

## 📖 11. Cite our work

If this helped your homework, project or paper, please cite:

```
@misc{arshad2025nonogram,
  author  = {Arshad, Mohid and Raza, Mohammad Umar and Hasnain, Mohammad},
  title   = {Solving Nonogram Puzzles with Simulated Annealing},
  year    = 2025,
  howpublished = {GitHub},
  note    = {https://github.com/your-username/NonogramSolver}
}
```

Happy puzzling! 🧩✨