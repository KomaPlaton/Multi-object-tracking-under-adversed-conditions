# Modified by Xinzhu Niu for transfer learning in SSY340 dml project
import os
import cv2
import numpy as np
import random


def add_snow(image, snow_density=0.02): 
    snow_mask = np.zeros_like(image)
    height, width = image.shape[:2]
    

    num_snowflakes = int(snow_density * width * height)
    for _ in range(num_snowflakes):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        radius = random.randint(1, 3)  
        cv2.circle(snow_mask, (x, y), radius, (255, 255, 255), -1)  

    snowy_image = cv2.addWeighted(image, 1, snow_mask, 0.3, 0)  
    return snowy_image


def add_snow_to_image_sequence(input_folder, output_folder, snow_density=0.02): 

    img1_output_folder = os.path.join(output_folder, 'img1')
    if not os.path.exists(img1_output_folder):
        os.makedirs(img1_output_folder)
    
    image_files = sorted([f for f in os.listdir(os.path.join(input_folder, 'img1')) if f.endswith('.jpg') or f.endswith('.png')])
    
    for i, image_file in enumerate(image_files):
        image_path = os.path.join(input_folder, 'img1', image_file)
        image = cv2.imread(image_path)
        

        snowy_image = add_snow(image, snow_density=snow_density)
        
        output_image_path = os.path.join(img1_output_folder, image_file)
        cv2.imwrite(output_image_path, snowy_image)
        print(f"Processed {i + 1}/{len(image_files)}: {image_file}")

# test
sequences = [
    'MOT17-01-FRCNN', 'MOT17-03-FRCNN', 'MOT17-06-FRCNN','MOT17-07-FRCNN'
] 
for sequence in sequences:
    input_folder = f'/data/mot_slim/test/{sequence}'
    output_folder = f'/data/mot_snow/test/{sequence}'
    add_snow_to_image_sequence(input_folder, output_folder, snow_density=0.01)

# #  train
# sequences = ['MOT17-11-FRCNN', 'MOT17-13-FRCNN'
# ] 
# for sequence in sequences:
#     input_folder = f'/data/mot_slim/train/{sequence}'
#     output_folder = f'/data/mot_slim/train/{sequence}'
#     add_snow_to_image_sequence(input_folder, output_folder, snow_density=0.01)