#!/bin/bash

CUDA_VISIBLE_DEVICES=2,3 CUDA_CACHE_PATH=/st2/samsungds/tmp python train.py --train_file_path ./korquad1.0/KorQuAD_v1.0_train.json --valid_file_path ./korquad1.0/KorQuAD_v1.0_dev.json --base_config korquad/bert_base_multilingual_cased --cuda_devices 2 3
