from PIL import Image, ImageSequence

# 读取GIF
im = Image.open("E:images/girlgif.gif")
# GIF图片流的迭代器
iter = ImageSequence.Iterator(im)

index = 1
# 遍历图片流的每一帧
for frame in iter:
    print("image %d: mode %s, size %s" % (index, frame.mode, frame.size))
    #  frame.save("E:images/frame%d.png" % index) 保存每一帧
    index += 1

# frame0 = frames[0]
# frame0.show()

# 把GIF拆分为图片流
imgs = [frame.copy() for frame in ImageSequence.Iterator(im)]
# 把图片流重新成成GIF动图, 每两帧取一帧
imgs[0].save('E:images/compressed.gif', save_all=True, append_images=imgs[1::2])

# 图片流反序
imgs.reverse()
# 将反序后的所有帧图像保存下来
imgs[0].save('E:images/reverse_out.gif', save_all=True, append_images=imgs[1:])
