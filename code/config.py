import numpy as np

g_batch_size = 128
d_batch_size = 128
lambda_gen = 1e-4
lambda_dis = 1e-4
lr_gen = 1e-5
#lr_dis = 1e-4
lr_dis = 1e-5
n_epoch = 10
sig = 1.0
label_smooth = 0.0
d_epoch = 5
g_epoch = 15
n_emb = 400
pre_d_epoch = 0
pre_g_epoch = 0
neg_weight = [1, 1, 1, 1]

dataset = 'DGATKG'
experiment = 'link_prediction'
train_file = '../data/%s/train_0.5' % dataset
test_file = '../data/%s/test_0.5' % dataset
pretrain_ckpt = ''
pretrain_dis_node_emb = ['../data/DGATKG/dggat-drug_embeddingdata.tsv']
pretrain_gen_node_emb = ['../data/DGATKG/dggat-drug_embeddingdata.tsv']
#pretrain_dis_node_emb = []
#pretrain_gen_node_emb = []
save = True
save_path = '../results/%s/%s/' % (experiment, dataset)
save_last = True
verbose = 1
log = True
dropout_rate = 0.3