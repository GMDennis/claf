#!/bin/bash

python train.py --train_file_path ./korquad1.0/KorQuAD_v1.0_train.json --valid_file_path ./korquad1.0/KorQuAD_v1.0_dev.json --base_config korquad/bidaf --cuda_devices 0
