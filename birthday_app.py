import streamlit as st

st.set_page_config(page_title="Birthday Card", layout="centered")

name = st.text_input("Enter the Birthday Person's Name", "Friend")

st.markdown(f"""
<style>
body {{
    margin: 0;
    padding: 0;
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
    position: relative;
    width: 100%;
    height: 180px;
    margin-bottom: 30px;
}}

.cake .base {{
    width: 100%;
    height: 80px;
    background: #ff69b4;
    border-radius: 10px;
    position: absolute;
    bottom: 0;
}}

.cake .frosting {{
    width: 100%;
    height: 25px;
    background: #fff0f5;
    border-radius: 10px 10px 0 0;
    position: absolute;
    bottom: 80px;
}}

.cake .candle {{
    width: 8px;
    height: 25px;
    background: #ffd700;
    position: absolute;
    top: 10px;
    left: 50%;
    transform: translateX(-50%);
}}

.cake .flame {{
    width: 8px;
    height: 8px;
    background: orange;
    border-radius: 50%;
    position: absolute;
    top: -8px;
    left: 0;
    animation: flicker 0.3s infinite alternate;
}}

@keyframes flicker {{
    from {{opacity: 0.8;}}
    to {{opacity: 1;}}
}}

.envelope-container {{
    position: relative;
    width: 100%;
    height: 130px;
    perspective: 1000px;
}}

.envelope-body {{
    width: 100%;
    height: 100%;
    background: #e0c3fc;
    border-radius: 0 0 10px 10px;
    position: relative;
    z-index: 1;
    box-shadow: 0 8px 16px rgba(0,0,0,0.2);
}}

.envelope-flap {{
    position: absolute;
    width: 100%;
    height: 65px;
    background: #c084fc;
    top: 0;
    left: 0;
    transform-origin: top center;
    animation: openFlap 2s ease-out forwards;
    z-index: 2;
    border-radius: 10px 10px 0 0;
}}

@keyframes openFlap {{
    0% {{ transform: rotateX(0deg); }}
    100% {{ transform: rotateX(-120deg); }}
}}

.message {{
    position: absolute;
    top: 25px;
    left: 10px;
    right: 10px;
    color: #4b0082;
    font-family: 'Courier New', Courier, monospace;
    font-size: 15px;
    text-align: center;
    z-index: 0;
}}

/* 📱 Responsive text */
@media (max-width: 480px) {{
    .message {{
        font-size: 14px;
    }}
    .cake {{
        height: 150px;
    }}
}}
</style>

<!-- Card HTML -->
<div class="container" id="card">
    <div class="cake">
        <div class="frosting"></div>
        <div class="base"></div>
        <div class="candle">
            <div class="flame"></div>
        </div>
    </div>

    <div class="envelope-container">
        <div class="envelope-flap"></div>
        <div class="envelope-body"></div>
        <div class="message">
            🎉 Happy Birthday, <b>{name}</b>!<br><br>
            Wishing you laughter, love,<br> and lots of sweet memories! 🎂🎈
        </div>
    </div>
</div>

<!-- 📥 Download Button & JS -->
<br>
<button onclick="downloadCard()" style="padding: 10px 20px; font-size:16px; border-radius: 8px; background: #8e44ad; color: white; border: none;">📥 Download Card</button>

<script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script>
<script>
function downloadCard() {{
    const card = document.getElementById('card');
    html2canvas(card).then(function(canvas) {{
        let link = document.createElement('a');
        link.download = 'birthday_card.png';
        link.href = canvas.toDataURL();
        link.click();
    }});
}}
</script>
""", unsafe_allow_html=True)
