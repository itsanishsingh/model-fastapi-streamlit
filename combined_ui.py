import streamlit as st
import requests


def main():

    result_dict = {"1": "setosa", "2": "versicolor", "3": "virginica"}

    st.title("Prediction Apps")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;"> Iris Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    SepalLength = st.slider("SepalLength", min_value=4.0, max_value=8.0, step=0.1)
    SepalWidth = st.slider("SepalWidth", min_value=2.0, max_value=4.5, step=0.1)
    PetalLength = st.slider("PetalLength", min_value=1.0, max_value=7.0, step=0.1)
    PetalWidth = st.slider("PetalWidth", min_value=0.1, max_value=2.5, step=0.1)

    if st.button("Predict Iris"):
        url = "http://127.0.0.1:8000/classification"
        data = {"1": SepalLength, "2": SepalWidth, "3": PetalLength, "4": PetalWidth}
        response = requests.post(url, json=data)
        output = response.text
        output = output.strip('"')
        result = result_dict[output]
        st.success("This iris is {}".format(result))

    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;"> Score Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    hours = st.slider("Hours Studied", min_value=1.0, max_value=12.0, step=0.1)
    prev_score = st.slider("Previous Score", min_value=40.0, max_value=100.0, step=0.5)

    if st.button("Predict Score"):
        url = "http://127.0.0.1:8000/regression"
        data = {"1": hours, "2": prev_score}
        response = requests.post(url, json=data)
        output = response.text
        output = output.strip('"')
        st.success("Your score would be {}".format(output))


if __name__ == "__main__":
    main()
