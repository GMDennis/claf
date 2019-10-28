#!/bin/bash

CUDA_CACHE_PATH=/st2/samsungds/tmp CUDA_VISIBLE_DEVICES=0 python train.py --train_file_path ./korquad1.0/aug_train_wQA.json --valid_file_path ./korquad1.0/KorQuAD_v1.0_dev.json --base_config korquad/bidaf --cuda_devices 0
