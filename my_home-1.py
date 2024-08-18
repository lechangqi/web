'''我的主页'''
#python -m streamlit run C:\Users\Administrator\Desktop\我的网络根据地\my_home.py
import streamlit as st
from PIL import Image
page = st.sidebar.radio('我的首页',["我的兴趣推荐","我的图片处理工具","我的智能词典","我的留言区"])
def page_1():
    '''我的兴趣推荐'''
    pass
        
        
def page_2():
    '''我的图片处理工具'''
    st.write(":u7981:图片换色小程序:u7981:")
    uploaded_file = st.file_uploader("上传图片",type=["png","jpeg","jpg"])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab1, tab2, tab3, tab4 = st.tabs(["原图","改色1","改色2","改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))



def page_3():
    '''我的智能词典'''
    st.write('智能词典')
    with open('words_space.txt','r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    word = st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word])
        if word == 'python':
            st.code('''
                    #恭喜你触发彩蛋，这是一行python代码
                    print('hello world')
                    ''')
        if word == 'sonw' or word == 'winter':
            st.snow()
        if word == 'birthday':
            st.balloons()

            
def page_4():
    '''我的留言区'''
    pass
def img_change(img, rc,gc,bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r, g, b)
    return img
if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()



