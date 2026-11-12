# Infinite Loop Detection System

CLA-2 Task 4 — Formal Language and Automata.

A Streamlit demonstration of timeout-based monitoring, connected to the theory of the Halting Problem.

## Features
- Normal finite-loop demonstration
- Deliberate infinite-loop timeout demonstration
- Program-error demonstration
- Output and explanation displayed in the browser
- Three-second execution limit

## Run locally
```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud
1. Open https://share.streamlit.io/ and sign in with GitHub.
2. Create an app and select this repository and the `main` branch.
3. Set the main file path to `app.py`.
4. Deploy.

## Important limitation
A timeout means only that a program did not finish within the selected time. It does not prove that the program runs forever. The general Halting Problem is undecidable.

## Safety
The app runs only three predefined sample scripts. It does not accept arbitrary user-supplied code.
