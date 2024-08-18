from PIL import Image
img=Image.open("天象奇景.jpg")
# 创建两个变量


#缩放与拉伸
newsize=(50,150)
img_resize=img.resize(newsize)
plt.show()
