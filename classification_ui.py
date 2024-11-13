import streamlit as st
import requests


def main():

    result_dict = {"1": "setosa", "2": "versicolor", "3": "virginica"}

    st.title("Iris Prediction")
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

    safe_html = """  
        <div style="background-color:#80ff80; padding:10px >
        <h2 style="color:white;text-align:center;"> Lets see</h2>
        </div>
        """

    if st.button("Predict Iris"):
        url = "http://127.0.0.1:8000/classification"
        data = {"1": SepalLength, "2": SepalWidth, "3": PetalLength, "4": PetalWidth}
        response = requests.post(url, json=data)
        output = response.text
        output = output.strip('"')
        result = result_dict[output]
        st.success("This iris is {}".format(result))

        st.markdown(safe_html, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
