from pathlib import Path
import subprocess
import sys
import streamlit as st

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
TIMEOUT_SECONDS = 3

CASES = {
    "Normal loop": {"file": SRC / "normal_program.py", "description": "A finite counter loop that should complete."},
    "Infinite loop": {"file": SRC / "infinite_program.py", "description": "A deliberate endless loop for timeout demonstration."},
    "Program error": {"file": SRC / "error_program.py", "description": "A sample that raises an exception."},
}

def run_case(label):
    script = CASES[label]["file"]
    if not script.is_file():
        return {"kind":"error","status":"Demo file missing","output":f"Could not find {script.name}.","explanation":"Ensure all src files are committed."}
    try:
        result = subprocess.run([sys.executable, str(script)], cwd=str(SRC), capture_output=True, text=True, timeout=TIMEOUT_SECONDS, check=False)
        if result.returncode == 0:
            return {"kind":"success","status":"Program completed successfully","output":result.stdout.strip() or "(No output)","explanation":"The sample finished within the time limit."}
        return {"kind":"error","status":"Program exited with an error","output":(result.stdout + "\n" + result.stderr).strip(),"explanation":f"Exit code: {result.returncode}"}
    except subprocess.TimeoutExpired:
        return {"kind":"warning","status":"Possible infinite loop detected — timeout","output":f"The sample did not finish within {TIMEOUT_SECONDS} seconds.","explanation":"A timeout is not proof of an infinite loop. A slow or blocked program may also time out."}

st.set_page_config(page_title="Infinite Loop Detection System", page_icon="🔁", layout="wide")
st.title("🔁 Infinite Loop Detection System")
st.caption("Formal Language and Automata · CLA-2 Task 4")
st.write("A practical demonstration of timeout-based program monitoring.")
st.info(f"Each predefined sample runs in a separate process with a {TIMEOUT_SECONDS}-second time limit.")
cols = st.columns(3)
for col, label in zip(cols, CASES):
    with col:
        with st.container(border=True):
            st.subheader(label)
            st.write(CASES[label]["description"])
            if st.button("Run test", key=label, use_container_width=True):
                with st.spinner("Running demonstration..."):
                    st.session_state["last_result"] = (label, run_case(label))
if "last_result" in st.session_state:
    label, result = st.session_state["last_result"]
    st.divider()
    st.subheader(f"Result: {label}")
    if result["kind"] == "success":
        st.success(result["status"])
    elif result["kind"] == "warning":
        st.warning(result["status"])
    else:
        st.error(result["status"])
    st.code(result["output"], language="text")
    st.info(result["explanation"])
left, right = st.columns(2)
with left:
    st.subheader("How it works")
    st.markdown("1. Select a trusted sample.\n2. Start a separate Python process.\n3. Capture output.\n4. Apply a fixed timeout.\n5. Report completion, timeout, or error.")
with right:
    st.subheader("Connection to theory")
    st.write("The general Halting Problem is undecidable. This app demonstrates a restricted practical workaround, not a universal halting detector.")
st.caption("Educational demonstration only. A timeout is a warning, not mathematical proof of non-termination.")
