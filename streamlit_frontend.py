import streamlit as st

st.set_page_config(page_title="CodeCounselor", page_icon="🧠", layout="wide")

# Apply the same background color scheme as static/style.css and style the main container as white
st.markdown(
    """
    <style>
    html, body, .stApp, [data-testid=\"stAppViewContainer\"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        min-height: 100vh;
    }
    /* Make Streamlit header/toolbar transparent so the gradient shows through */
    [data-testid=\"stHeader\"], [data-testid=\"stToolbar\"] {
        background: transparent;
    }
    /* Ensure the main content wrapper is transparent so the outside columns show the gradient */
    .block-container {
        background: transparent;
    }
    /* White card container around our main content */
    [data-testid=\"stVerticalBlock\"]:has(#therapy-card-anchor) {
        background: #ffffff;
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.title("🧠 CodeCounselor")
    st.markdown("Your AI-Powered Code Therapist")

    with st.container():
        st.markdown('<div id="therapy-card-anchor"></div>', unsafe_allow_html=True)
        st.markdown("Share your thoughts with Dr.CodeBot:")
        prompt = st.chat_input("Paste your troubled code here.. Dr. Codebot is here to help!🩺")
        if prompt:
            st.markdown("Your therapy session has started. Dr. CodeBot is analyzing your code...")
