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

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🎤 Favorite music artist", "💤 Guessing sleeping hours", "📰 News", "Gold price 💰", "Health check ❤️"])

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
    feed = feedparser.parse("https://vnexpress.net/rss/tin-moi-nhat.rss")
    for entry in feed.entries[:10]:
        st.subheader(entry.title)
        st.write(entry.published)
        st.write(entry.link)
with tab4:
    st.header("💰 Updating gold price news from Vietnamnet")
    feed = feedparser.parse("https://vietnamnet.vn/rss/kinh-doanh.rss")
    gold_news = [entry for entry in feed.entries if "vàng" in entry.title.lower() or "giá vàng" in entry.summary.lower()]

    if gold_news:
        for entry in gold_news[:5]:  # Hiện 5 bài gần nhất
            st.subheader(entry.title)
            st.write(entry.published)
            st.write(entry.link)
    else:
        st.warning("No gold price news found.")
with tab5:
    st.header("Check your BMI number")
    weight = st.number_input("Enter your weight (kg)", min_value = 10.0, max_value = 200.0, value = 60.0, step = 0.1)
    height = st.number_input("Enter your height (m)", min_value = 1.0, max_value = 2.5, value = 1.7, step = 0.01)
    if st.button("Calculate BMI"):
        bmi = weight/(height ** 2)
        st.success(f"Your BMI number is {bmi : .2f}")
        if bmi < 18.5:
            st.warning("You are underweight, so you should eat more nutritious food.")
        elif 18.5 <= bmi < 25:
            st.info("You are at a normal weight. Continue to maintain a healthy lifestyle.")
        elif 25 <= bmi < 30:
            st.warning("You're overweight. You need to balance diet and exercise.")
        else:
            st.error("You are overweight. See a nutritionist or doctor for advice.")
