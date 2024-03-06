# AraEGI-Arabic-Gender-Identification-Using-Transformers-for-Egyptian-Dialects  
In this repo we present 
-  **AraEGI**:  Our newly annotated dataset for gender identification of both of the *Speaker* and the *Listener* in Arabic Egyptian Dialect Tweets. 
- **Models Checkpoint**: We present best performing model checkpoints, all trained with our dataset, to serve as benchmarks for all future research.

All details are in [our paper]()

## AraEGI Datasets

Our training dataset consists of 3 different versions

- [AraEGI-E](https://github.com/AhmedHamdi101/AraEGI-Arabic-Gender-Identification-Using-Transformers-for-Egyptian-Dialect/tree/main/AraEGI/AraEGI-E)
- [AraEGI-P](https://github.com/AhmedHamdi101/AraEGI-Arabic-Gender-Identification-Using-Transformers-for-Egyptian-Dialect/tree/main/AraEGI/AraEGI-P)
- [AraEGI-All](https://github.com/AhmedHamdi101/AraEGI-Arabic-Gender-Identification-Using-Transformers-for-Egyptian-Dialect/tree/main/AraEGI/AraEGI-All)



## Models Checkpoints

### 3-label Classification Models
| Model | Training Dataset | Task |
|----------|----------|----------|
| [araBERTv0.2-twitter-base](https://drive.google.com/drive/folders/1U82AquuO121sCh6gZYJSaqvh3JcT93TD)    | AraEGI-All   |  *Speaker* Classification |
| [araELECTRA-discriminator-base](https://drive.google.com/drive/folders/1jhVPm6RMRl5nb07aIgmUQov5pmUeW0Dm)   | AraEGI-All  | *Speaker* Classification  |
| [araBERTv0.2-twitter-Base](https://drive.google.com/drive/folders/18zBXvKuRg0knrNxbXbavQeNhJFver3-S)  | AraEGI-All  | *Listener* Classification   |
| [MARBERT](https://drive.google.com/drive/folders/1NigiVJ1PIWK797U8fSPtem81YLFc04s7)  | AraEGI-All  | *Listener* Classification  |
| [camelBERT-mix-base](https://drive.google.com/drive/folders/1b7X3XPRXL-fTZBIPZ-LO3Y8u60_cIVPa)  | AraEGI-All  | *Listener* Classification  |

### 9-label Classification Models

| Model | Training Dataset |
|----------|----------|
| [araBERTv0.2-twitter-base](https://drive.google.com/drive/folders/1_NCPKb15_Bafy73rJn4aFPf4Zxo-33z3) | AraEGI-All |
| [araBERTv0.2-base](https://drive.google.com/drive/folders/1TRXjK1WAfZL6fV_imllLJGCnvgjVFgqz)   | AraEGI-All |
| [araBERTv2-base](https://drive.google.com/drive/folders/1XudbkuJ1O5PFz9eslU4Ipv7zLTQjTbfK)    | AraEGI-All |
| [camelBERT-mix-base](https://drive.google.com/drive/folders/1XiAwTLRhGmWzIphG0YST-G-9_Lw0M5X5) | AraEGI-All |

