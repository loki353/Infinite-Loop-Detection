# Infinite Loop Detection in Software
## CLA-2 Task 4 — Formal Language and Automata

> **Team submission template:** Fill in the four members' actual names, registration details and contributions before submission.

## Abstract
This project studies infinite-loop detection using Turing-machine and computability concepts. The general question of deciding whether an arbitrary program halts on a given input is the Halting Problem, which is undecidable. The practical demonstration uses a timeout-based monitor for a small set of predefined Python programs. A timeout indicates that a program did not finish within the selected time; it is not proof of non-termination.

## 1. Introduction
Loops repeat instructions while a condition remains true. An infinite loop does not reach a normal stopping point and may consume processor time or make software unresponsive.

## 2. Problem Statement
Given a program P and input w, determine whether execution eventually stops or continues indefinitely. The general problem asks for a correct answer for every possible program and input.

## 3. Objectives
- Explain infinite loops and their effects.
- Model computation using Turing-machine concepts.
- Explain the Halting Problem and undecidability.
- Distinguish decidability from recognizability.
- Demonstrate timeout-based monitoring.
- Discuss practical limitations.

## 4. Real-World Relevance
- **Web services:** a stuck request handler can occupy a worker.
- **Banking software:** a non-terminating operation can delay transactions.
- **Industrial control:** a stuck computation can interrupt expected control behaviour.
- **Desktop/mobile applications:** a loop that does not yield can make an interface unresponsive.

## 5. Turing Machine Model
A deterministic Turing machine can be represented as M = (Q, Σ, Γ, δ, q₀, B, F), where Q is the set of states, Σ is the input alphabet, Γ is the tape alphabet, δ is the transition function, q₀ is the initial state, B is the blank symbol, and F is the set of halting/accepting states under the chosen convention. A computation halts when it reaches a halting configuration; otherwise its configuration sequence may continue indefinitely.

## 6. Formal Computational Formulation
HALT = {⟨M, w⟩ | Turing machine M halts on input w}. Here ⟨M, w⟩ is an encoding of a machine and its input. The decision question is whether that computation eventually halts.

## 7. Halting Problem and Undecidability
The Halting Problem is undecidable: no total algorithm correctly answers YES or NO for every program and input. In the diagonal contradiction argument, assume a perfect halting predictor H exists. Construct a program that behaves opposite to H's prediction: it loops if H predicts that it halts, and halts if H predicts that it loops. Running this constructed program on its own description creates a contradiction. Therefore, a perfect universal halting decider cannot exist.

## 8. Decidability and Recognizability
A problem is decidable if an algorithm halts on every input and returns the correct YES/NO answer. HALT is recognizable: simulate M on w and accept if it halts. If M does not halt, the simulation continues forever. The complement of HALT is not recognizable in general.

## 9. Proposed Practical Approach
The implementation runs only predefined sample scripts in separate Python processes and applies a fixed timeout. It reports:
- completion when a sample exits successfully;
- timeout when it exceeds the time limit;
- error when it exits with a non-zero status.

## 10. Demonstration Cases
### 10.1 Finite loop
```python
count = 1
while count <= 5:
    print(count)
    count += 1
print("Program completed")
```
The counter eventually becomes 6, so the condition becomes false.

### 10.2 Non-terminating loop
```python
count = 1
while True:
    count += 1
```
The condition is always true, so the sample does not terminate on its own.

### 10.3 Error case
```python
print("Starting")
raise ValueError("Demonstration error")
```
The process terminates with an exception.

## 11. System Architecture
1. Select a trusted predefined sample.
2. Launch it as a separate Python process.
3. Capture standard output and standard error.
4. Apply a fixed execution time limit.
5. Report completion, timeout or error.

## 12. Results and Discussion
| Test case | Expected result | Meaning |
|---|---|---|
| Normal loop | Completed | This input halted |
| Infinite loop | Timeout | Exceeded the limit; not proof |
| Error program | Non-zero exit | Program ended due to an exception |

## 13. Limitations
- A timeout cannot prove that a program runs forever.
- A slow but valid program can time out.
- A program waiting for input or a network response can time out.
- Testing covers selected inputs, not all possible executions.
- The general Halting Problem remains undecidable.

## 14. Conclusion
The Halting Problem shows that a universal exact algorithm for deciding termination of every arbitrary program is impossible. Practical methods such as timeout monitoring, static analysis and testing still help identify and manage suspicious behaviour. The demonstration illustrates a restricted engineering workaround, not a solution to the general Halting Problem.

## 15. References
1. Turing, A. M. (1936). *On Computable Numbers, with an Application to the Entscheidungsproblem*. Proceedings of the London Mathematical Society.
2. Sipser, M. *Introduction to the Theory of Computation*. Cengage Learning.
3. SRM Institute of Science and Technology, Tiruchirappalli. 21CSC301T Formal Language and Automata, CLA-2 Task 4 assignment instructions, 2026–2027.
4. Python Software Foundation. *subprocess — Subprocess management*. https://docs.python.org/3/library/subprocess.html

## 16. Individual Contributions
| Member | Responsibility | Actual contribution |
|---|---|---|
| Member 1 | Introduction, problem definition, applications | Fill in |
| Member 2 | Turing-machine model and formal formulation | Fill in |
| Member 3 | Halting Problem, decidability and recognizability | Fill in |
| Member 4 | Python demo, tests and practical approach | Fill in |

## 17. Browser Demonstration
The Streamlit interface is the root-level `app.py`. Install dependencies with `pip install -r requirements.txt`, then run `streamlit run app.py`. It offers three predefined tests and displays their results in the browser. Do not claim that timeout proves non-termination.
