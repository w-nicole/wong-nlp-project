#!/bin/bash

seed=${1:-42}
model=${2:-"bert-base-multilingual-cased"}
task=${3:-"udpos"}
freeze=${4:-"-1"}

model_name=$(echo "$model" | tr '/' '\n' | tail -n1)

save_path=${5:-"/nobackup/users/wongn/nlp-ox/wong-nlp-project/experiments"}

src="English"
tgt=(Bulgarian Danish German English Spanish Persian Hungarian Italian Dutch Polish Portuguese Romanian Slovak Slovenian Swedish)
data_path=${6:-"/nobackup/users/wongn/ud-treebanks-v1.4"}

python src/train.py \
    --seed "$seed" \
    --task "$task" \
    --data_dir "$data_path" \
    --trn_langs $src \
    --val_langs $src \
    --tst_langs "${tgt[@]}" \
    --pretrain "$model" \
    --batch_size=16 \
    --learning_rate=5e-5 \
    --max_epochs=3 \
    --warmup_portion=0.1 \
    --gpus=1 \
    --freeze_layer "$freeze" \
    --default_save_path "$save_path"/"$task"/0-shot-finetune-freeze"$freeze"/"$model_name" \
    --exp_name bs$bs-lr$lr-ep$ep \
    --gpus=1 \
    --weight_decay=0.01 \
    --warmup_portion=0.1 \
    --schedule "linear";
    
python src/train.py \
    --seed "$seed" \
    --task "$task" \
    --data_dir "$data_path" \
    --trn_langs $src \
    --val_langs $src \
    --tst_langs "${tgt[@]}" \
    --pretrain "$model" \
    --batch_size=16 \
    --learning_rate=5e-5 \
    --max_epochs=3 \
    --warmup_portion=0.1 \
    --gpus=1 \
    --freeze_layer "$freeze" \
    --default_save_path "$save_path"/"$task"/0-shot-finetune-freeze"$freeze"/"$model_name" \
    --exp_name bs$bs-lr$lr-ep$ep \
    --gpus=1 \
    --weight_decay=0.01 \
    --warmup_portion=0.1 \
    --schedule "linear";

python src/train.py \
    --seed "$seed" \
    --task "$task" \
    --data_dir "$data_path" \
    --trn_langs $src \
    --val_langs $src \
    --tst_langs "${tgt[@]}" \
    --pretrain "$model" \
    --batch_size=16 \
    --learning_rate=5e-5 \
    --max_epochs=3 \
    --warmup_portion=0.1 \
    --gpus=1 \
    --freeze_layer "$freeze" \
    --default_save_path "$save_path"/"$task"/0-shot-finetune-freeze"$freeze"/"$model_name" \
    --exp_name bs$bs-lr$lr-ep$ep \
    --gpus=1 \
    --weight_decay=0.01 \
    --warmup_portion=0.1 \
    --schedule "linear";

python src/train.py \
    --seed "$seed" \
    --task "$task" \
    --data_dir "$data_path" \
    --trn_langs $src \
    --val_langs $src \
    --tst_langs "${tgt[@]}" \
    --pretrain "$model" \
    --batch_size=16 \
    --learning_rate=5e-5 \
    --max_epochs=3 \
    --warmup_portion=0.1 \
    --gpus=1 \
    --freeze_layer "$freeze" \
    --default_save_path "$save_path"/"$task"/0-shot-finetune-freeze"$freeze"/"$model_name" \
    --exp_name bs$bs-lr$lr-ep$ep \
    --gpus=1 \
    --weight_decay=0.01 \
    --warmup_portion=0.1 \
    --schedule "linear";