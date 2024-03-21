import json
import time
import requests
import streamlit as st

st.set_page_config(
    page_title="pattanan ",
    page_icon= ":bar_chart:",
)
st.sidebar.success("เลือกรายการด้านบน.")


html_1 = """
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3> การพยากรณ์ข้อมูล </h3></center>
</div>
"""

st.header("  การพยากรณ์ข้อมูล....!  ")
st.subheader(" 1.หลักการและเหตุผล")
st.info("""
        กราฟนี้เเสดงเพือทราบเกี่ยวกับการที่ผู้หญิงเเละผู้ชายมีความชอบเเตกต่างกันเรื่องสีเช่น
        Warm cool Neutral จึงนำมาทำการวิเคราะห์
        <br>
        
        """)
st.subheader(" 2.วัตถุประสงค์")
st.info("""
        เพื่อศึกษาเทคนิคการนำมาทำกราฟเกี่ยวกับความชอบเกี่ยวกับสีของผู้ชายเเละผู้หญิง
        """)
st.balloons()