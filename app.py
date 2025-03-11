import streamlit as st
import re
import random
import string
from streamlit_lottie import st_lottie
import requests

# Function to load Lottie animations from a URL
def load_lottieurl(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to load Lottie animation from {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"An error occurred while loading Lottie animation: {e}")
        return None

# Load Lottie animations
lottie_animation = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_3rwasyjy.json")
lottie_heading = load_lottieurl("https://raw.githubusercontent.com/fatii0999/myanimations/main/Animation%20-%201741582646923.json")
lottie_sidebar = load_lottieurl("https://raw.githubusercontent.com/fatii0999/myanimations/main/Animation%20-%201741573899249.json")
# Custom CSS for styling and animations
st.markdown(
    """
    <style>
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    .fadeIn {
        animation: fadeIn 1.5s ease-in-out;
    }
    .stButton>button {
        background-color: #3F51B5 !important;
        color: white !important;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #303F9F !important;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
    }
    .app-header {
        background: linear-gradient(90deg, #6a11cb 0%, #2575fc 100%);
        padding: 12px 20px;
        border-radius: 8px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
        flex-wrap: wrap;
    }
    .header-text-container {
        flex: 1;
        min-width: 200px;
        text-align: center;
    }
    .header-text {
        color: #ffffff;
        font-family: 'Arial', sans-serif;
        font-size: 28px;
        font-weight: bold;
        margin: 0;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        display: inline-block;
    }
    .header-animation {
        min-width: 80px;
        max-width: 100px;
        margin: 0 auto;
    }
    .stMarkdown h2 {
        color: #4CAF50;
        font-family: 'Arial', sans-serif;
    }
    .stMarkdown h3 {
        color: #4CAF50;
        font-family: 'Arial', sans-serif;
    }
    .lottie-container {
        background-color: transparent;
    }
    .password-strength-meter {
        width: 100%;
        height: 10px;
        background-color: #e0e0e0;
        border-radius: 5px;
        margin-top: 10px;
        overflow: hidden;
    }
    .password-strength-meter-fill {
        height: 100%;
        transition: width 0.5s ease-in-out;
    }
    .strength-0 { background-color: #ff5252; width: 25%; }
    .strength-1 { background-color: #ff5252; width: 50%; }
    .strength-2 { background-color: #ffd740; width: 75%; }
    .strength-3 { background-color: #69f0ae; width: 100%; }
    @media (max-width: 768px) {
        .app-header {
            flex-direction: column;
            padding: 12px;
        }
        .header-text-container {
            width: 100%;
            margin-bottom: 10px;
        }
        .header-text {
            font-size: 22px;
            text-align: center;
            display: block;
        }
        .header-animation {
            width: 100%;
            min-width: auto;
            margin: 0 auto;
        }
        .stMarkdown h2 {
            font-size: 20px;
        }
        .stMarkdown h3 {
            font-size: 18px;
        }
        .stTextInput>div>div>input {
            font-size: 14px;
        }
        .stButton>button {
            font-size: 14px;
            padding: 8px 16px;
        }
        .lottie-container {
            text-align: center;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least **8 characters** long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include **both uppercase and lowercase** letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least **one number (0-9)**.")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least **one special character (!@#$%^&*)**.")
    
    return score, feedback

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    with st.sidebar:
        st.markdown("## 📝 Project Notes")
        st.markdown("""
            - **Project Name**: Elite Password Strength Analyzer
            - **Purpose**: To help users create and check strong passwords.
            - **Features**:
                - Password Strength Checker
                - Password Generator
                - Visual Feedback
            - **Designed By**: Fatima Riaz
        """)
        if lottie_sidebar:
            st_lottie(lottie_sidebar, height=200, key="sidebar")
        
        st.markdown("---")
        st.markdown("## 🚀 Additional Features")
        st.markdown("""
            - **Password History**: View previously generated passwords.
            - **Security Tips**: Get tips on how to keep your accounts secure.
            - **Dark Mode**: Switch between light and dark themes.
            - **Export Passwords**: Export generated passwords to a CSV file.
            - **Multi-Language Support**: Use the app in multiple languages.
        """)
        
        st.markdown("---")
        st.markdown("## 🔒 Security Tips")
        st.markdown("""
            - Use unique passwords for each account.
            - Enable two-factor authentication (2FA) wherever possible.
            - Avoid using easily guessable information like birthdays or names.
            - Regularly update your passwords.
            - Use a password manager to store your passwords securely.
        """)

    st.markdown(
        """
        <div class="app-header">
            <div class="header-text-container">
                <span class="header-text">🔐 Elite Password Strength Analyzer🌐 </span>
            </div>
            <div class="header-animation">
        """,
        unsafe_allow_html=True,
    )
    if lottie_heading:
        st_lottie(lottie_heading, height=80, key="heading")
    st.markdown("</div></div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="fadeIn">
            <p>Welcome to <strong>Elite Password Strength Analyzer!</strong>  
            Ensure your password is secure by checking:</p>
            <ul>
                <li>✅ Length</li>
                <li>✅ Upper & Lowercase letters</li>
                <li>✅ Numbers</li>
                <li>✅ Special Characters</li>
            </ul>
            <blockquote>⚠️ <em>Improve your online security by creating strong passwords!</em></blockquote>
        </div>
        """,
        unsafe_allow_html=True,
    )

    password = st.text_input("🔑 Enter your password:", type="password")
    
    if password:
        score, _ = check_password_strength(password)
        st.markdown(f'<div class="password-strength-meter"><div class="password-strength-meter-fill strength-{score}"></div></div>', unsafe_allow_html=True)
    
    if st.button("🔐 Check Password Strength"):
        if password:
            score, feedback = check_password_strength(password)
            st.subheader("🔒 Password Strength Result:")
            if score == 4:
                st.success("✅ Strong Password! Your password is secure.", icon="✅")
            elif score == 3:
                st.warning("⚠️ Moderate Password - Consider adding more security features.", icon="⚠️")
            else:
                st.error("🚨 Weak Password - Improve it using the suggestions below.", icon="🚨")
            if feedback:
                st.info("💡 Suggestions to improve your password:")
                for tip in feedback:
                    st.write(tip)
        else:
            st.error("🚨 Please enter a password to check.")

    st.markdown("---")
    st.subheader("🔏 Password Generator")
    password_length = st.slider("Select password length:", min_value=8, max_value=32, value=12)
    if st.button("Generate Password"):
        generated_password = generate_password(password_length)
        st.success(f"🔑 Generated Password: `{generated_password}`")

    if lottie_animation:
        st.markdown('<div class="lottie-container">', unsafe_allow_html=True)
        st_lottie(lottie_animation, height=300, key="animation")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class="amazing-footer">
            <p class="footer-quote">"The only way to do great work is to love what you do."</p>
            <p class="designer-credit">Designed by Fatima Riaz</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()