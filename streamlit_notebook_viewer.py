import streamlit as st
import json

# Function to load the notebook from an in-memory file-like object
def load_notebook(file):
    # Use the 'BytesIO' object directly to read the content
    return json.load(file)

def display_notebook(notebook_json):
    for cell in notebook_json['cells']:
        if cell['cell_type'] == 'code':
            st.code("\n".join(cell['source']), language='python')
        elif cell['cell_type'] == 'markdown':
            st.markdown("\n".join(cell['source']))

def main():
    st.title('Jupyter Notebook Viewer')
    uploaded_file = st.file_uploader("Upload Jupyter Notebook", type="ipynb")
    
    if uploaded_file is not None:
        notebook_json = load_notebook(uploaded_file)
        display_notebook(notebook_json)

if __name__ == "__main__":
    main()
