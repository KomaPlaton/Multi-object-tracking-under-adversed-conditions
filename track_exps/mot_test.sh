#!/usr/bin/env bash

python3 main_track.py --output_dir . --dataset_file /data/mot_ref --coco_path /data/mot_ref --batch_size 1 --resume output/checkpoint.pth --track_eval_split test --eval --with_box_refine  --num_queries 500