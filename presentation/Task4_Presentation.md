# Presentation: Infinite Loop Detection in Software

## Slide 1 — Title
Infinite Loop Detection in Software  
CLA-2 Task 4 — Formal Language and Automata  
Team of Four

## Slide 2 — Problem and Motivation
- Infinite loop: execution does not reach a normal stopping point.
- Can waste CPU time and make software unresponsive.
- Main question: can every program be classified as halting or non-halting?

## Slide 3 — Turing Machine Model
- A mathematical model of computation.
- Uses states, a tape, a read/write head and transitions.
- Halting computation reaches a halting configuration.

## Slide 4 — Formal Problem
HALT = {⟨M, w⟩ | M halts on input w}
- M is a machine/program.
- w is its input.
- Decide whether the computation eventually stops.

## Slide 5 — Undecidability
- Assume a perfect halting predictor exists.
- Construct a program that does the opposite of its prediction.
- Running it on its own description creates a contradiction.
- Therefore, the general Halting Problem is undecidable.

## Slide 6 — Practical Demonstration
- Normal finite loop: completes.
- Deliberate endless loop: exceeds timeout.
- Error sample: exits with an exception.
- Streamlit UI displays each result.

## Slide 7 — System Workflow
Choose predefined sample → launch child process → capture output → apply time limit → report completion, timeout or error.

## Slide 8 — Results and Limitations
- Timeout means only that the program did not finish in time.
- Slow valid programs can also time out.
- The tool is not a universal halting detector.

## Slide 9 — Conclusion and Contributions
- General exact halting decision is impossible.
- Practical analysis and monitoring still help manage risk.
- Add each member's actual name and contribution.
