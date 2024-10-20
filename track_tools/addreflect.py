import cv2
import numpy as np
import os

def add_strong_light_shadow(image, brightness_change=100, shadow_intensity=0.8):
    # 随机调整亮度
    brightness = np.random.randint(-brightness_change, brightness_change)
    bright_image = cv2.convertScaleAbs(image, alpha=1, beta=brightness)
    
    # 创建阴影图像
    shadow = np.zeros_like(image)
    height, width = image.shape[:2]

    # 随机选择阴影区域
    shadow_x_start = np.random.randint(0, width // 2)
    shadow_x_end = np.random.randint(shadow_x_start, width)
    shadow_y_start = np.random.randint(0, height // 2)
    shadow_y_end = np.random.randint(shadow_y_start, height)

    # 应用阴影
    shadow[shadow_y_start:shadow_y_end, shadow_x_start:shadow_x_end] = \
        bright_image[shadow_y_start:shadow_y_end, shadow_x_start:shadow_x_end] * shadow_intensity

    # 合并亮度变化图像和阴影
    light_shadow_image = cv2.addWeighted(bright_image, 1, shadow, 1, 0)
    return light_shadow_image

# 处理图片序列的函数
def add_strong_light_shadow_to_image_sequence(input_folder, output_folder, brightness_change=100, shadow_intensity=0.8):
    # 确保输出文件夹包含 'img1' 子文件夹
    img1_output_folder = os.path.join(output_folder, 'img1')
    if not os.path.exists(img1_output_folder):
        os.makedirs(img1_output_folder)

    image_files = sorted([f for f in os.listdir(os.path.join(input_folder, 'img1')) if f.endswith('.jpg') or f.endswith('.png')])

    for i, image_file in enumerate(image_files):
        image_path = os.path.join(input_folder, 'img1', image_file)
        image = cv2.imread(image_path)

        # 添加强烈光影变化效果
        strong_light_shadow_image = add_strong_light_shadow(image, brightness_change=brightness_change, shadow_intensity=shadow_intensity)

        # 保存处理后的图像
        output_image_path = os.path.join(img1_output_folder, image_file)
        cv2.imwrite(output_image_path, strong_light_shadow_image)
        print(f"Processed {i + 1}/{len(image_files)}: {image_file}")

# 示例用法
sequences = [
    'MOT17-01-FRCNN', 'MOT17-03-FRCNN', 'MOT17-06-FRCNN','MOT17-07-FRCNN'
]
for sequence in sequences:
    input_folder = f'/data/mot_slim/test/{sequence}'
    output_folder = f'/data/mot_ref/test/{sequence}'
    add_strong_light_shadow_to_image_sequence(input_folder, output_folder, brightness_change=100, shadow_intensity=0.8)


# #  train
# sequences = ['MOT17-04-FRCNN', 'MOT17-05-FRCNN'
# ] 
# for sequence in sequences:
#     input_folder = f'/data/mot_slim/train/{sequence}'
#     output_folder = f'/data/mot_slim/train/{sequence}'
#     add_strong_light_shadow_to_image_sequence(input_folder, output_folder, brightness_change=100, shadow_intensity=0.8)