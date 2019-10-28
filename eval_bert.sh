#!/bin/bash

CUDA_CACHE_PATH=/st2/samsungds/tmp python eval.py ./korquad1.0/KorQuAD_v1.0_train_wQA_f1_BEST_x3.json ./logs/squad_bert/20191023_base/checkpoint/model_6000_for_filtering_2.pkl --cuda_devices 0 1 2 3
