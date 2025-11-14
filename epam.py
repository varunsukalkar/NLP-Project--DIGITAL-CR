import streamlit as st
import time

# ----------------- Streamlit Setup -----------------
st.set_page_config(page_title="College Chatbot (Static)", layout="centered")
st.title("🎓 College Info Chatbot (Static Version)")
st.markdown("Ask anything related to your college schedule or faculty below 👇")

# ----------------- Hardcoded Answers -----------------
qa_data = {
    "semester start": "Classes for the semester will commence on December 16, 2024.",
    "registration": "Registration for open electives, honors, and minor courses will begin on December 5, 2024.",
    "unit test 1": "Unit Test 1 will be conducted from February 14 to February 19, 2025.",
    "teacher assessment": "Teacher's Assessment 1 marks will be displayed from February 4 to February 6, 2025.",
    "feedback": "Student feedback session 1 will take place from February 10 to February 13, 2025.",
    "remedial": "Remedial classes for slow learners will be conducted from February 26 to March 2, 2025.",
    "parent teacher meeting": "Parent teacher meeting is scheduled on March 1, 2025.",
    "provisional detention": "Display of provisional detention list will occur on April 3, 2025.",
    "unit test 2": "Unit Test 2 will be conducted from April 14 to April 20, 2025.",
    "final detention": "Final detention list will be displayed on April 21, 2025.",
    "end exam": "End semester examination will start on April 29, 2025.",
    "result": "Results for end semester examination will be declared on May 23, 2025.",
    "make up exam": "Make-up examinations will begin on May 30, 2025 and results will be declared on June 16, 2025.",
    "semester break": "Semester break will be from May 5 to June 30, 2025.",
    "new semester": "New semester classes will commence on July 5, 2025.",
    "sports day": "Annual Sports Day will be held from January 25 to January 27, 2025.",
    "rina damdoo": "Prof. Rina S. Damdoo is an Assistant Professor in Computer Science and Engineering with 18 years of teaching experience. She can be reached at damdoor@rknec.edu.",
    "purva vyawahare": "Prof. Purva Vyawahare is an Assistant Professor in Computer Science and Engineering. Her Vidwan ID is https://vidwan.inflibnet.ac.in/profile/626039 and her email is vyawaharepn@rknec.edu.",
    "cloud computing": "Cloud Computing (CST421) class is at 9:00 AM in room CS207 by Professor H. Gehani on Monday, Thursday, and Friday.",
    "business intelligence": "Business Intelligence (CST422) class is at 10:00 AM in room CS207 by Professor Khushboo Shah on Monday, Thursday, and Friday.",
    "nlp": "Natural Language Processing (CST423) class is at 2:00 PM in room CS207 by Professor Amit Pimpalkar on Monday and at 10:00 AM in CS207 on Friday.",
    "project ii": "Project-II (CSP424) guidance session is scheduled at 9:00 AM on Saturday.",
    "mentor mentee": "Mentor-Mentee Meeting Slot is scheduled at 10:00 AM on Tuesday.",
    "lab": "NLP Lab (CSP423) is scheduled at 3:00 PM in lab DT-405 by Professor P. Vyawahare on Thursday."
}

# ----------------- Chat Section -----------------
user_input = st.text_input("💬 Ask your question:", key="input_box")

if st.button("Send"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("🤖 Thinking..."):
            time.sleep(4.1)  # ⏳ Simulate chatbot thinking delay
            query = user_input.lower()
            response = None

            # Check for partial keyword matches
            for key, ans in qa_data.items():
                if key in query:
                    response = ans
                    break

            # Display response or fallback
            if response:
                st.success(f"**Answer:** {response}")
            else:
                time.sleep(1)
                st.error("❌ Sorry, I don’t have that information in my records. Please check the academic notice.")

st.markdown("---")
st.caption("Built with Streamlit 💡 | Static Data extracted from nlp data.pdf")
