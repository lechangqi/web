'''我的首页'''
import streamlit as st
from PIL import Image

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区'])

def page_1():
    '''我的推荐'''
    st.write('我的电影推荐')
    st.write('-----------------------------')
    st.write('我的游戏推荐')
    st.write('-----------------------------')
    st.write('我的书籍推荐')
    st.write('-----------------------------')
    st.write('我的习题集推荐')
    st.write('-----------------------------')

def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img, 0, 2, 1))

def page_3():
    '''我的智能词典'''
    st.write('智能词典')
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    # 显示查询内容
    if word in words_dict:
        st.write(words_dict[word][1])
        # 注意词典中没有python，需要自行添加数据
        if word == 'python':
            st.code('''
                    # 恭喜你触发彩蛋，这是一行python代码
                    print('hello world')''')
        if word == 'snow' or word == 'winter':
            st.snow()
        if word == 'birthday':
            st.balloons()


def page_4():
    '''我的留言区'''
    pass

def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()