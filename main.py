import os
import pathlib
import textwrap

import google.generativeai as genai

# Used to securely store your API key
genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel('gemini')
