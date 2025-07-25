import streamlit as st

st.set_page_config(page_title="🎂 Happy Birthday", layout="centered")

st.markdown(f"""
<style>
body {{
    background-color: #fff0f5;
}}
.container {{
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 20px;
    width: 90%;
    max-width: 400px;
    margin-left: auto;
    margin-right: auto;
}}

.cake {{
    width: 180px;
    height: 200px;
    position: relative;
    margin-bottom: 40px;
}}

.cake .base {{
    width: 100%;
    height: 100px;
    background: #ff4d6d;
    border-radius: 10px;
    position: absolute;
    bottom: 0;
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}}

.cake .frosting {{
    width: 100%;
    height: 30px;
    background: #fff;
    border-radius: 15px 15px 0 0;
    position: absolute;
    bottom: 100px;
    box-shadow: inset 0 2px 5px rgba(0,0,0,0.1);
}}

.cake .candle {{
    width: 10px;
    height: 30px;
    background: #ffd700;
    position: absolute;
    top: 10px;
    left: 50%;
    transform: translateX(-50%);
}}

.cake .flame {{
    width: 12px;
    height: 12px;
    background: orange;
    border-radius: 50%;
    position: absolute;
    top: -12px;
    left: -1px;
    animation: flicker 0.4s infinite alternate;
}}

@keyframes flicker {{
    from {{opacity: 0.6; transform: scale(1);}}
    to {{opacity: 1; transform: scale(1.2);}}
}}

.envelope-container {{
    position: relative;
    width: 280px;
    height: 160px;
    perspective: 1000px;
}}

.envelope-body {{
    width: 100%;
    height: 100%;
    background: #ffccd5;
    border-radius: 0 0 10px 10px;
    position: relative;
    z-index: 1;
    box-shadow: 0 5px 15px rgba(0,0,0,0.3);
}}

.envelope-flap {{
    position: absolute;
    width: 100%;
    height: 80px;
    background: #ff4d6d;
    top: 0;
    left: 0;
    transform-origin: top center;
    animation: openFlap 2.5s ease-out forwards;
    z-index: 2;
    border-radius: 10px 10px 0 0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
}}

.envelope-flap::before {{
    content: "❤";
}}

@keyframes openFlap {{
    0% {{ transform: rotateX(0deg); }}
    100% {{ transform: rotateX(-120deg); }}
}}

.message {{
    position: absolute;
    top: 30px;
    left: 15px;
    right: 15px;
    color: #4b0082;
    font-family: 'Georgia', serif;
    font-size: 15px;
    text-align: center;
    z-index: 0;
    white-space: pre-wrap;
    line-height: 1.5;
}}

/* 📱 Responsive */
@media (max-width: 480px) {{
    .cake {{
        transform: scale(0.9);
    }}
    .message {{
        font-size: 14px;
    }}
}}
</style>

<div class="container">
    <!-- 🎂 Decorative Cake -->
    <div class="cake">
        <div class="frosting"></div>
        <div class="base"></div>
        <div class="candle">
            <div class="flame"></div>
        </div>
    </div>

    <!-- 💌 Envelope -->
    <div class="envelope-container">
        <div class="envelope-flap"></div>
        <div class="envelope-body"></div>
        <div class="message">
            HAPPY BIRTHDAY BUDDHU,🫶🏻
            I LOVE YOU SO MUCH BABY!!❤

            I know you are not very excited but baby it's your 21st birthday, so be happy and smile, enjoy your day.....

            I wish I could be with you, but nvm I'm sending you my love and wish digitally 😂...

            Thank you for being there with me in every ups and downs....

            You're so so so special to me I can't tell you...❤
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
