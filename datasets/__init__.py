# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
import torch.utils.data
from .torchvision_datasets import CocoDetection

from .coco import build as build_coco
from .mot import build as build_mot
from .mix import build as build_mix
from .crowdhuman import build as build_crowdhuman

def get_coco_api_from_dataset(dataset):
    for _ in range(10):
        # if isinstance(dataset, torchvision.datasets.CocoDetection):
        #     break
        if isinstance(dataset, torch.utils.data.Subset):
            dataset = dataset.dataset
    if isinstance(dataset, CocoDetection):
        return dataset.coco


def build_dataset(image_set, args):
    if args.dataset_file == 'coco':
        return build_coco(image_set, args)
    if args.dataset_file == '/data/mot_slim':
        return build_mot(image_set, args)
    if args.dataset_file == '/data/mot_snow':
        return build_mot(image_set, args)
    if args.dataset_file == '/data/mot_blur':
        return build_mot(image_set, args)
    if args.dataset_file == '/data/mot_ref':
        return build_mot(image_set, args)
    if args.dataset_file == 'mix':
        return build_mix(image_set, args)
    if args.dataset_file == 'crowdhuman':
        return build_crowdhuman(image_set, args)
    if args.dataset_file == 'coco_panoptic':
        # to avoid making panopticapi required for coco
        from .coco_panoptic import build as build_coco_panoptic
        return build_coco_panoptic(image_set, args)
    raise ValueError(f'dataset {args.dataset_file} not supported')

