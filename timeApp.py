import streamlit as st
import datetime

# Function to calculate time differences
def calculate_time_difference(input_str):
    input_str = input_str.strip()
    if not input_str:
        return None, "Please enter a valid time period."
    
    lower_input = input_str.lower()
    is_bc = False
    is_ad = False

    if 'bc' in lower_input:
        is_bc = True
        lower_input = lower_input.replace('bc', '').replace('.', '').strip()
    elif 'ad' in lower_input:
        is_ad = True
        lower_input = lower_input.replace('ad', '').replace('.', '').strip()

    try:
        year = int(lower_input)
    except ValueError:
        return None, "Please enter a valid year."
    
    # Convert to astronomical numbering (BC as negative)
    input_year = -year if is_bc else year

    # Get the current year
    current_year = datetime.datetime.now().year

    # 1) Difference from today
    diff_today = current_year - input_year
    today_relation = "ago" if diff_today >= 0 else "in the future"
    diff_today = abs(diff_today)
    diff_today_thousand = round(diff_today / 1000, 1)

    # 2) Relative to the foundation of Oxford University (c. 1096 AD)
    oxford_year = 1096
    if input_year < oxford_year:
        diff_oxford = oxford_year - input_year
        oxford_relation = "before"
    else:
        diff_oxford = input_year - oxford_year
        oxford_relation = "after"
    diff_oxford_thousand = round(diff_oxford / 1000, 1)

    # 3) Relative to the oldest recorded civilization (representative date: 3500 BC)
    oldest_civ_year = -3500
    if input_year < oldest_civ_year:
        diff_old = oldest_civ_year - input_year
        old_relation = "before"
    else:
        diff_old = input_year - oldest_civ_year
        old_relation = "after"
    diff_old_thousand = round(diff_old / 1000, 1)

    # Prepare the result message (using Markdown formatting)
    result_msg = (
        f"**Time Period:** {input_str}\n\n"
        f"- The entered time period is approximately **{diff_today_thousand}** thousand years {today_relation} today.\n\n"
        f"- It is approximately **{diff_oxford_thousand}** thousand years {oxford_relation} the foundation of Oxford University (c. 1096 AD).\n\n"
        f"- It is approximately **{diff_old_thousand}** thousand years {old_relation} the oldest recorded civilization (representative date: 3500 B.C.)."
    )
    
    return result_msg, None

# Set Streamlit page configuration
st.set_page_config(page_title="Time Traveler", page_icon="⏳")

# Custom CSS to give a papyrus-like background and style buttons
papyrus_css = """
<style>
body {
    background-color: #f7e7ce;
}
.reportview-container .main .block-container{
    background-color: #fdf5e6;
    border: 10px solid #d2b48c;
    border-radius: 15px;
    padding: 30px;
}
div.stButton > button {
    background-color: #d2b48c;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
}
div.stButton > button:hover {
    background-color: #c4a484;
}
</style>
"""
st.markdown(papyrus_css, unsafe_allow_html=True)

# App title and input instructions
st.title("Time Traveler")
st.write("Enter a time period (e.g., **1900 B.C.** or **2020 AD**):")

# Text input for the time period
time_input = st.text_input("Time Period", "")

# Calculate button and result display
if st.button("Calculate"):
    result, error = calculate_time_difference(time_input)
    if error:
        st.error(error)
    else:
        st.markdown(result)
