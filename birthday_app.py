import streamlit as st

st.set_page_config(page_title="Birthday Card", layout="centered")

st.markdown("""
    <style>
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 30px;
    }

    .cake {
        position: relative;
        width: 200px;
        height: 200px;
        margin-bottom: 50px;
    }

    .cake .base {
        width: 100%;
        height: 100px;
        background: #ff69b4;
        border-radius: 10px;
        position: absolute;
        bottom: 0;
    }

    .cake .frosting {
        width: 100%;
        height: 30px;
        background: #fff0f5;
        border-radius: 10px 10px 0 0;
        position: absolute;
        bottom: 100px;
    }

    .cake .candle {
        width: 10px;
        height: 30px;
        background: #ffd700;
        position: absolute;
        top: 10px;
        left: 50%;
        transform: translateX(-50%);
    }

    .cake .flame {
        width: 10px;
        height: 10px;
        background: orange;
        border-radius: 50%;
        position: absolute;
        top: -10px;
        left: 0;
        animation: flicker 0.3s infinite alternate;
    }

    @keyframes flicker {
        from {opacity: 0.8;}
        to {opacity: 1;}
    }

    .envelope {
        position: relative;
        width: 250px;
        height: 150px;
        background: #e0c3fc;
        margin-top: 30px;
        border-radius: 10px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.3);
    }

    .envelope::before {
        content: "";
        position: absolute;
        width: 0;
        height: 0;
        border-left: 125px solid transparent;
        border-right: 125px solid transparent;
        border-bottom: 75px solid #c084fc;
        top: -75px;
        left: 0;
    }

    .message {
        position: absolute;
        top: 30px;
        left: 20px;
        right: 20px;
        color: #4b0082;
        font-family: 'Courier New', Courier, monospace;
        font-size: 16px;
        text-align: center;
    }

    </style>

    <div class="container">
        <div class="cake">
            <div class="frosting"></div>
            <div class="base"></div>
            <div class="candle">
                <div class="flame"></div>
            </div>
        </div>

        <div class="envelope">
            <div class="message">
                🎉 Happy Birthday buddhu\n I LOVE YOU SO MUCH BABY!<br><br>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)
