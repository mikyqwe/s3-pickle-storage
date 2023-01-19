import smart_open
import cloudpickle

def save_pickle_on_s3(object, s3_path):
    """
    Save a pickle object to a specified S3 path.
    """
    with smart_open.open(s3_path, 'wb') as f:
        cloudpickle.dump(object, f)

def load_pickle_on_s3(s3_path):
    """
    Load a pickle object from a specified S3 path.
    """
    with smart_open.open(s3_path, 'rb') as f:
        return cloudpickle.load(f)