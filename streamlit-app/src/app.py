from streamlit import st
import requests

st.title("Side Hustles and Money Quotes")

st.sidebar.header("Navigation")
option = st.sidebar.selectbox("Choose an option", ["Side Hustles", "Money Quotes"])

if option == "Side Hustles":
    response = requests.get("http://localhost:8000/side_hustles")
    if response.status_code == 200:
        side_hustle = response.json().get("side_hustle")
        st.subheader("Random Side Hustle Idea")
        st.write(side_hustle)
    else:
        st.error("Failed to fetch side hustle.")

elif option == "Money Quotes":
    response = requests.get("http://localhost:8000/money_quotes")
    if response.status_code == 200:
        money_quote = response.json().get("money_quote")
        st.subheader("Random Money Quote")
        st.write(money_quote)
    else:
        st.error("Failed to fetch money quote.")