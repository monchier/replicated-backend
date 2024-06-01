import streamlit as st
import subprocess
from subprocess import PIPE, STDOUT
import shlex

text = st.text_area("Enter commands")

if text:
    commands =  [shlex.split(x) for x in text.splitlines()]
    for c in commands:
        try:
            p = subprocess.run(c, capture_output=True, check=True, text=True)
            st.info(p.stdout)
            st.info(p.stderr)
        except subprocess.CalledProcessError as e:
            st.error(e)
        except Exception as e:
            st.error(e)
