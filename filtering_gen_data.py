import os
import sys
import torch
import pickle

def run_eval(sample_dir_name, sample_file_name, model_dir_name):
    command = 'CUDA_CACHE_PATH=/st2/samsungds/tmp '
    command += 'CUDA_VISIBLE_DEVICES=0 '
    command += 'python eval.py '
    command += sample_dir_name + sample_file_name + ' '
    command += model_dir_name + ' '
    command += '--cuda_devices 0'

    os.system(command)

def get_score(log_name):
    return torch.load(log_name)['valid/f1'][0]

if __name__ == '__main__':

    sample_dir_name = "/st2/samsungds/claf/korquad1.0/Single_Json_files/"
    filenames = os.listdir(sample_dir_name)
    model_dir_name = './logs/squad_bert/20191023_base/checkpoint/model_6000.pkl'
    log_name = './logs/squad_bert/tmp_for_filtering.pt'

    score_dic = {}
    
    count_for_test = 0

    for filename in filenames:
        run_eval(sample_dir_name, filename, model_dir_name)
        score = get_score(log_name) 
        score_dic[filename] = score
        
        count_for_test += 1
        if count_for_test == 3:
            break

    with open('scores.pkl','wb') as f:
        pickle.dump(score_dic, f)
