import collections
import numpy as np
import pandas as pd
import tensorflow as tf
import h5py
from tqdm import tqdm
import copy
from scipy.stats import entropy
from sklearn.metrics import precision_recall_curve, auc
from app.core.config import settings

model = tf.saved_model.load(settings.MODEL_PATH + settings.MODEL_NAME_TRANSFORM)

def accuracy_function(real, pred):
    accuracies = tf.equal(real, tf.argmax(pred, axis=2))
    mask = tf.math.logical_not(tf.math.equal(real, 0))
    accuracies = tf.math.logical_and(mask, accuracies)
    accuracies = tf.cast(accuracies, dtype=tf.float32)
    mask = tf.cast(mask, dtype=tf.float32)
    return tf.reduce_sum(accuracies)/tf.reduce_sum(mask)

def get_accuracy_infer_single_traj(input_test):
    size = input_test.shape[1]
    out, _, preds = model.predict(input_test)
    accuracies = accuracy_function(input_test, preds.numpy().reshape((1, size, -1)))
    return accuracies.numpy(), out.numpy().reshape(-1).tolist()
