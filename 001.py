import streamlit as st
from sklearn.linear_model import LinearRegression
import feedparser

st.sidebar.title("🎶 Music artist list")
selected_artist = st.sidebar.radio("Choose a music artist:", ["Đen Vâu", "Hà Anh Tuấn", "Sơn Tùng M-TP"])

videos = {
    "Đen Vâu": [
        ("Bữa ăn cho em", "https://www.youtube.com/watch?v=ukHK1GVyr0I"),
        ("Mang tiền về cho mẹ", "https://www.youtube.com/watch?v=UVbv-PJXm14"),
        ("Trời hôm nay nhiều mây cực!", "https://www.youtube.com/watch?v=MBaF0l-PcRY"),
        ("Hai triệu năm", "https://www.youtube.com/watch?v=LSMDNL4n0kM")
    ],
    "Hà Anh Tuấn": [
        ("Tuyết rơi mùa hè", "https://www.youtube.com/watch?v=pTh3KCD7Euc"),
        ("Nước ngoài", "https://www.youtube.com/watch?v=pU3O9Lnp-Z0"),
        ("Tháng tư là lời nói dối của em", "https://www.youtube.com/watch?v=UCXao7aTDQM"),
        ("Xuân thì", "https://www.youtube.com/watch?v=3s1r_g_jXNs")
    ],
    "Sơn Tùng M-TP": [
        ("Lạc trôi", "https://www.youtube.com/watch?v=Llw9Q6akRo4"),
        ("Chúng ta không thuộc về nhau", "https://www.youtube.com/watch?v=qGRU3sRbaYw"),
        ("Muộn rồi mà sao còn", "https://www.youtube.com/watch?v=xypzmu5mMPY"),
        ("Hãy trao cho anh", "https://www.youtube.com/watch?v=knW7-x7Y7RE")
    ]
}

st.title("🎧 Entertainment and health app")

tab1, tab2, tab3 = st.tabs(["🎤 Favorite music artist", "💤 Guessing sleeping hours", "📰 News" ])

with tab1:
    st.header(f"{selected_artist}'s music 🎵")
    for title, url in videos[selected_artist]:
        st.subheader(title)
        st.video(url)
with tab2:
    st.title("🕘 Guessing the sleeping hours")
    x = [
        [10, 8, 1],
        [20, 6, 5],
        [25, 3, 8],
        [30, 2, 6],
        [50, 2, 2],
        [15, 9, 2],
        [40, 4, 3]
    ]
    y = [10, 8, 6, 6, 5, 7, 9.5]
    model = LinearRegression()
    model.fit(x, y)
    st.write("Please enter your info:")
    age = st.number_input("Your age:", min_value=5, max_value=100, value= 25)
    activity = st.slider("Physical activity level (1 = few, 10 = energetic)", 1, 10, 5)
    screen_time = st.number_input("Screen usage per day (hour)", min_value=0, max_value=24, value=6)
    if st.button("🥱 Guess the sleeping time"):
        input_data = [[age, activity, screen_time]]
        result = model.predict(input_data)[0]
        st.success(f"You should sleep {result:.1f} hour per night")
        if result < 6.5:
            st.warning("Maybe you need to sleep much to recover your health")
        elif result > 9:
            st.info("Maybe you are having physical activity hard - Sleep well is necessary to recover your body")
        else:
            st.success("Perfect sleeping time. Keep it going")
with tab3:
    st.header("The latest news from VnExpress")
    feed = feedparser.parse("https://e.vnexpress.net/news/news")
    for entry in feed.entries[:5]:
        st.subheader(entry.title)
        st.write(entry.published)
        st.write(entry.link)
