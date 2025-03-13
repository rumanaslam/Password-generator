import streamlit as st
import re
import secrets
import string

# Page configuration
st.set_page_config(page_title="Password Strength Checker", page_icon="🔏")

# Title
st.title("🔒 Password Strength Checker")
st.markdown("""
    Welcome to the ultimate password strength checker!  
    Enter a password below to see how secure it is.
""")

# User input
password = st.text_input("Enter Your Password", type="password")

# Strength calculation
feedback = []
score = 0

if password:
    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔹 Password should be at least **8 characters long**.")

    # Upper and lower case check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("🔹 Password should contain **both uppercase and lowercase** letters.")

    # Digit check
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("🔹 Password should contain **at least one digit (0-9).**")

    # Special character check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("🔹 Password should contain **at least one special character (!@#$%^&* etc.).**")

    # Strength assessment
    strength_levels = {0: ("❌ Very Weak", "red"), 
                       1: ("⚠ Weak", "orange"), 
                       2: ("🟡 Medium", "yellow"), 
                       3: ("🟢 Strong", "green"), 
                       4: ("✅ Very Strong", "blue")}

    strength_text, color = strength_levels[score]

    # Display results
    st.markdown(f"### **Password Strength:** `{strength_text}`")
    st.progress(score / 4)

    if score == 4:
        st.success("Your password is **very strong!** Great job! 🎉")
    elif score == 3:
        st.warning("Your password is **strong**, but could be improved!")
    else:
        st.error("Your password is **weak**. Try making it stronger!")

    # Show improvement tips
    if feedback:
        st.markdown("### 🔍 Improvement Suggestions:")
        for tip in feedback:
            st.write(tip)

    # Generate a strong password suggestion
    if score < 4:
        def generate_password(length=12):
            """Generate a strong random password."""
            all_chars = string.ascii_letters + string.digits + "!@#$%^&*()"
            return ''.join(secrets.choice(all_chars) for _ in range(length))

        suggested_password = generate_password()
        st.markdown("### 🔑 Suggested Strong Password:")
        st.code(suggested_password, language="plaintext")

        # Download button for password
        st.download_button("📥 Download Password", suggested_password, file_name="strong_password.txt")

else:
    st.info("👆 Please enter a password to check its strength.")
