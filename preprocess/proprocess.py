### File for preprocessing the data (imgs) ###

import tensorflow as tf


def preprocess(file_path):
    """Preprocess the image by resizing to 100x100x3 and scale between 0 and 1.

    Args:
        file_path ('tensorflow.python.framework.ops.Tensor'): File path which contains images to be preprocessed.

    Returns:
        <'tensorflow.python.framework.ops.Tensor': Proprocessed image.
    """
    # Read in image from file path
    byte_img = tf.io.read_file(file_path)
    # Load in the image 
    img = tf.io.decode_jpeg(byte_img)
    
    # Preprocessing steps - resizing the image to be 100x100x3
    img = tf.image.resize(img, (100,100))
    # Scale image to be between 0 and 1 
    img = img / 255.0
    
    # Return image
    return img


def preprocess_twin(input_img, validation_img, label):
    """Preprocess the given input, validation images with labels.

    Args:
        input_img ('tensorflow.python.framework.ops.Tensor'): Input image given to the network.
        validation_img ('tensorflow.python.framework.ops.Tensor'): Validation image given with the input image.
        label ('tensorflow.python.framework.ops.Tensor'): Label of the data.
    """
    return(preprocess(input_img), preprocess(validation_img), label)



