# S3 Pickle IO

This repository contains two functions `save_pickle_on_s3` and `load_pickle_on_s3` that allows to save and load pickle object to and from S3 storage.

## Requirements
* python 3.x
* smart_open
* cloudpickle
* boto3
* AWS credentials

You can install the required libraries by running the following command:
```bash
pip install -r requirements.txt
```
or
```bash
pip install smart_open cloudpickle boto3