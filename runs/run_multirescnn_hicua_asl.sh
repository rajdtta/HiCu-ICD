python main.py \
    --MODEL_DIR ./models \
    --DATA_DIR ./data \
    --MIMIC_3_DIR ./data/mimic3 \
    --data_path ./data/mimic3/train_full.csv \
    --embed_file ./data/mimic3/processed_full_100.embed \
    --vocab ./data/mimic3/vocab.csv \
    --Y full \
    --model MultiResCNN \
    --decoder HierarchicalHyperbolic \
    --criterion prec_at_8 \
    --MAX_LENGTH 4096 \
    --batch_size 8  \
    --lr 5e-5 \
    --depth 5 \
    --n_epochs '2,3,5,10,50'  \
    --num_workers 8 \
    --hyperbolic_dim 50 \
    --loss ASL \
    --asl_config "1,0,0.05"
