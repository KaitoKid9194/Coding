import streamlit as st
from sklearn.linear_model import LinearRegression
import feedparser
import numpy as np
st.title("🎧 Entertainment and health app")
menu = st.selectbox("Choose the application you want to use: ", [
    "🎤 Favorite music artist", 
    "💤 Nap amount recommendation", 
    "📰 News",
    "Gold price 💰", 
    "Health check ❤️", 
    "Heartbeat check 🩺", 
    "Step recommendations 👣", 
    "Daily water recommended 💧", 
    "DISC test 🧠"
])
if menu == "🎤 Favorite music artist":
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
    st.header(f"{selected_artist}'s music 🎵")
    for title, url in videos[selected_artist]:
        st.subheader(title)
        st.video(url)
elif menu == "💤 Nap amount recommendation":
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
elif menu == "📰 News":
    st.header("The latest news from VnExpress")
    feed = feedparser.parse("https://vnexpress.net/rss/tin-moi-nhat.rss")
    for entry in feed.entries[:10]:
            st.subheader(entry.title)
            st.write(entry.published)
            st.write(entry.link)
elif menu == "Gold price 💰":
    st.header("💰 Updating gold price news from Vietnamnet")
    feed = feedparser.parse("https://vietnamnet.vn/rss/kinh-doanh.rss")
    gold_news = [entry for entry in feed.entries if "vàng" in entry.title.lower() or "giá vàng" in entry.summary.lower()]
    if gold_news:
        for entry in gold_news[:5]:
            st.subheader(entry.title)
            st.write(entry.published)
            st.write(entry.link)
    else:
        st.warning("No gold price news found.")
elif menu == "Health check ❤️":
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
elif menu == "Heartbeat check 🩺":
    st.header("Heartbeat check, are you need to meet a doctor?")
    x = np.array([
        [100, 2, 12],
        [95, 4, 15],
        [90, 6, 18],
        [85, 9, 20],
        [80, 12, 25],
        [75, 20, 50],
        [72, 30, 65],
        [70, 40, 70],
        [68, 50, 75],
        [66, 58, 78],
        [70, 65, 70],
        [75, 70, 68],
        [80, 75, 65],
        [85, 80, 60],
        [90, 85, 58],
    ])
    y = np.array([
        1.2, 1.3, 1.5, 1.6, 1.7,
        2.0, 2.3, 2.7, 3.0, 3.2,
        3.5, 3.8, 4.0, 4.3, 4.6
    ])
    model = LinearRegression()
    model.fit(x, y)
    st.subheader("Enter health information")
    hr = st.number_input("Heartbeat (bpm)", min_value = 40, max_value = 200, value = 75)
    age = st.number_input("Age", min_value = 1, max_value = 120, value = 30)
    weight = st.number_input("Weight (kg)", min_value = 10.0, max_value = 200.0, value = 60.0)
    if st.button("Check"):
        score = model.predict([[hr, age, weight]])[0]
        st.success(f"chỉ số rủi ro: **{score: .2f}**")
        if score < 1.5:
            st.info("You're good. No need to meet a doctor.")
        elif score < 2.5:
            st.warning("Need to wait for a bit more time, rest and check again later.")
        elif score < 3.5:
            st.warning("You have some unusual points. Need some advice from the doctor.")
        else:
            st.error("High risk! Meet a doctor as soon as possible!")
elif menu == "Step recommendations 👣":
    age = st.number_input("How old are you?", min_value= 1, max_value= 100, value= 25)
    if st.button("Info"):
        if age < 18:
            st.info("You should walk 12000 - 15000 steps per day.")
        elif age < 40:
            st.info("You should walk 8000 - 10000 steps per day.")
        elif age < 65:
            st.info("You should walk 7000 - 9000 steps per day.")
        else:
            st.info("You should walk 6000 - 8000 steps per day.")
elif menu == "Daily water recommended 💧":
    age1 = st.number_input("How old are you?", min_value= 1, max_value= 100, value= 25, key="abc")
    if st.button("Recommend"):
        if age1 < 4:
            st.info("You should drink 1.3 liter of water a day.")
        elif age1 < 9:
            st.info("You should drink 1.7 liter of water a day.")
        elif age1 < 14:
            st.info("You should drink 2.1 - 1.4 liter of water a day.")
        elif age1 < 19:
            st.info("You should drink 2.3 - 3.3 liter of water a day.")
        elif age1 < 51:
            st.info("You should drink 1.3 liter of water a day.")
        else:
            st.info("You should drink 1.3 liter of water a day.")
elif menu == "DISC test 🧠":
    st.header("Personality check based on DISC")
    st.markdown("Choose a most likely discription and a least likely description.")
    group = [
        {
            "D": "I'm assertive and like to control.",
            "I": "I like friendly and easy to talk to.",
            "S": "I am patient and trustworthy.",
            "C": "I am precise and systematic."
        },
        {
            "D": "I like challenges and fast action.",
            "I": "I'm energetic and optimistic.",
            "S": "I'm stable and supportive to others.",
            "C": "I work according to clear rules."
        },
        {
            "D": "I like to control the result.",
            "I": "I like to be recognized.",
            "S": "I aprecciate harmony.",
            "C": "I pay attention to detail and analysis."
        }
    ]
    score = {"D": 0, "I": 0, "S": 0, "C": 0}
    for idx, group in enumerate(group):
        st.markdown(f"### group {idx + 1}")
        options = list(group.values())
        key = list(group.keys())
        most = st.radio("Your best fitting desciprtion", options, key = f"most_{idx}")
        least = st.radio("Your least fitting desciprtion", options, key = f"least_{idx}")
        for key, val in group.items():
            if val == most:
                score[key] += 1
            if val == least:
                score[key] -= 1
    if st.button("Check the DISC result"):
        st.header("Your result:")
        max_type = max(score, key = score.get)
        for style, score in score.items():
            st.write(f"{style}: {score} scores")
        st.markdown(f"Your most outstanding feature is:  {max_type}**")
        descriptions = {
            "D": "Quyết đoán, định hướng kết quả và thích kiểm soát",
            "I": "Giao tiếp tốt, tràn đầy năng lượng và truyền cảm hứng",
            "S": "Kiên nhẫn, đáng tin cậy và hỗ trợ người khác",
            "C": "Chính xác, tuân thủ quy trình và thích phân tích logic"            
        }
        st.info(descriptions[max_type])
        st.markdown("-----")
        st.markdown("Mô tả chi tiết các nhóm DISC")
        st.markdown("""
            - **D (Dominance)**: Người lãnh đạo, chủ động, thích cạnh tranh. Ví dụ: CEO, nhà sáng lập.  
            - **I (Influence)**: Người truyền cảm hứng, thích giao tiếp, có sức hút. Ví dụ: người làm marketing, diễn giả.  
            - **S (Steadiness)**: Người hỗ trợ, trung thành, kiên nhẫn. Ví dụ: giáo viên, điều dưỡng.  
            - **C (Conscientiousness)**: Người phân tích, tỉ mỉ, theo quy trình. Ví dụ: kế toán, kỹ sư.
        """)
        st.caption("Đây chỉ là bài tham khảo về chỉ số DISC")
