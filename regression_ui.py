import streamlit as st
import requests


def main():
    st.title("Score Prediction")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;"> Score Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    hours = st.slider("Hours Studied", min_value=1.0, max_value=12.0, step=0.1)
    prev_score = st.slider("Previous Score", min_value=40.0, max_value=100.0, step=0.5)

    safe_html = """  
        <div style="background-color:#80ff80; padding:10px >
        <h2 style="color:white;text-align:center;"> Lets see</h2>
        </div>
        """

    if st.button("Predict Score"):
        url = "http://127.0.0.1:8000/regression"
        data = {"1": hours, "2": prev_score}
        response = requests.post(url, json=data)
        output = response.text
        output = output.strip('"')
        st.success("Your score would be {}".format(output))

        st.markdown(safe_html, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
