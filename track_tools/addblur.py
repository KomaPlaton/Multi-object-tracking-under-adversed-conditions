import cv2
import numpy as np
import os

def add_motion_blur(image, intensity=15):
    # 创建运动模糊的卷积核
    kernel = np.zeros((intensity, intensity))
    kernel[intensity // 2, :] = np.ones(intensity)  # 在中心行设置为1
    kernel /= intensity  # 归一化

    # 使用卷积操作应用运动模糊
    blurred_image = cv2.filter2D(image, -1, kernel)
    return blurred_image

# 处理图片序列的函数
def add_motion_blur_to_image_sequence(input_folder, output_folder, intensity=15):
    # 确保输出文件夹包含 'img1' 子文件夹
    img1_output_folder = os.path.join(output_folder, 'img1')
    if not os.path.exists(img1_output_folder):
        os.makedirs(img1_output_folder)

    image_files = sorted([f for f in os.listdir(os.path.join(input_folder, 'img1')) if f.endswith('.jpg') or f.endswith('.png')])

    for i, image_file in enumerate(image_files):
        image_path = os.path.join(input_folder, 'img1', image_file)
        image = cv2.imread(image_path)

        # 添加运动模糊效果
        blurred_image = add_motion_blur(image, intensity=intensity)

        # 保存处理后的图像
        output_image_path = os.path.join(img1_output_folder, image_file)
        cv2.imwrite(output_image_path, blurred_image)
        print(f"Processed {i + 1}/{len(image_files)}: {image_file}")

# 示例用法
sequences = [
    'MOT17-01-FRCNN', 'MOT17-03-FRCNN', 'MOT17-06-FRCNN','MOT17-07-FRCNN'
]
for sequence in sequences:
    input_folder = f'/data/mot_slim/test/{sequence}'
    output_folder = f'/data/mot_blur/test/{sequence}'
    add_motion_blur_to_image_sequence(input_folder, output_folder, intensity=15)
