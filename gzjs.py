import streamlit as st
# 页面标题
st.title("入")
# 输入框
ji = st.number_input('请输入您的绩效：', min_value=0.8, max_value=1.2, step=0.1)
chu = st.number_input('请输入您的出勤天数：', step=1)
ying = st.number_input('请输入您的应出勤天数：', min_value=1,step=1)
wan = st.number_input('请输入您的晚班天数：', min_value=0, max_value=31, step=1)
jiang = st.number_input('请输入您的其他奖金：', min_value=0.0, step=0.1)
kou = st.number_input('请输入其他扣除：', min_value=0.0, step=0.1)
jia = st.number_input('加班了多少小时：',step=1)
# 计算按钮
if st.button("牛马一个月的工资"):
# 判断输入合法性
    if jia > 8.0 or jia < 0.0:
        st.error('加班时长不对哈')
    elif ji > 1.2 or ji < 0.8:
        st.error('绩效在0.8到1.2这个区间')
    elif chu > 31 or ying > 31 or wan > 31:
        st.error('一月夺少天？')
    elif chu < 0 or ying <= 0 or wan < 0:
        st.error('出勤天数不能为负数。。。')
    elif chu < ying:
        res = round((2700*ji+300)*(chu+jia*0.13)/ying+wan*20+jiang-kou,2)
        st.success(f"你的本月薪资：{res} 元")
    else:
        res = round(2700*ji*(chu+jia*0.13)/ying+300+wan*20+jiang-kou,2)
        st.success(f"你的本月薪资：{res} 元")
