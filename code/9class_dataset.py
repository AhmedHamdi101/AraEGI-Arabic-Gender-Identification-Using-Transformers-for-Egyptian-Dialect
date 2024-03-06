
import numpy as np
import pandas as pd
from torch.utils.data import Dataset
import random
import re
import torch

class TrainMixDatasetMultiClass9class(Dataset):
    def __init__(self, file_path, tokenizer,preprocessor, max_length , mode):
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.mode = mode
        self.arabert_prep = preprocessor 
        self.data = []
        # Read text data from files
        self.data_category = pd.read_csv(file_path)
        self.data_category.dropna(subset=['Tweet'], inplace=True)
        self.tweets = self.data_category["Tweet"].values
        self.labels = self.data_category["B_Label"].values

        for i in range(len(self.data_category)):
            line = self.tweets[i]
            label = self.labels[i]
            label =label.astype(np.float32)

            self.data.append([line, label])


    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):


        text = self.data[idx][0].strip()
        text = self.arabert_prep.preprocess(text)
        
        

        label_id = self.data[idx][1]
        label = np.zeros((1,9))

        #  {'BB': 0, 'BM': 1, 'BF': 2, 'MB': 3, 'FB':4, 'MM': 5, 'MF': 6, 'FF':7, 'FM':8}
        label[0][int(label_id)] = 1
        # Tokenize and process text
        tokens = self.tokenizer.encode_plus(
            text,
            max_length=self.max_length,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )

        input_ids = tokens['input_ids'].squeeze()
        attention_mask = tokens['attention_mask'].squeeze()
        return {
            'input_ids': input_ids,
            'attention_mask': attention_mask,
            'label': torch.tensor(label),
            'text': text
        }
