#!/usr/bin/env bash

python3 -m torch.distributed.launch --nproc_per_node=1 --use_env main_track.py  --output_dir ./output --dataset_file /data/mot_snow --coco_path /data/mot_snow --batch_size 2  --with_box_refine  --num_queries 500 --resume /data/671mot17_crowdhuman_mot17.pth --epochs 10 --lr_drop 8
