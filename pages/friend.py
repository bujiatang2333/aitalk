import streamlit as st
st.title("他的性格选择页面")
if "xingge" not in st.session_state:
    st.session_state.xingge = ""
bt = st.button("温柔贴心涂山璟")
if bt:
    st.session_state.xingge="温柔知性"
    st.switch_page("pages/aibot.py")
bt1 = st.button("理智清醒相柳")
if bt1:
    st.session_state.xingge="霸道冷漠"
    st.switch_page("pages/aibot.py")
bt2 = st.button("阳光小狗赤水丰隆")
if bt2:
    st.session_state.xingge="活泼可爱"
    st.switch_page("pages/aibot.py")
st.image("https://k.sinaimg.cn/n/sinakd20230816s/794/w939h655/20230816/0999-d993630144b4bb739d49f3f9cf03a953.jpg/w700d1q75cms.jpg?by=cms_fixed_width", use_column_width=True)