#!/usr/bin/env bash

python3 main_track.py  --output_dir . --dataset_file /data/mot_snow --coco_path /data/mot_snow --batch_size 1 --resume output/checkpoint.pth --eval --with_box_refine --num_queries 500