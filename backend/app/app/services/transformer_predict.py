#!/usr/bin/env ipython

import os
import time
import pandas as pd
import tensorflow as tf

from app.services.transformer import get_accuracy_infer_single_traj, model
# from app.core.errors import PredictException, ModelLoadException
from app.core.config import settings


class TransformerModelHandlerScores(object):
    model = model

    @classmethod
    def predict(cls, input, load_wrapper=None, method="predict", rota=0, traj=0):
        start_time = time.time()
        clf = cls.get_model(load_wrapper)
        loaded_data = cls.load_evaluate_data(
            settings.DATA_DIR + f'/{rota}/processed_dublin_test_and_anom_evaluation.csv')
        if hasattr(clf, method):
            size = loaded_data[traj].size
            data = loaded_data[traj].reshape((1, size))
            results = get_accuracy_infer_single_traj(data)
            print(f'---seconds--{time.time() - start_time}')
            return {
                "Accuracy": float(results[0]),
                "Prediction": results[1],
                "RealData": loaded_data[50:51].reshape(-1).tolist()
            }
        raise PredictException(f"'{method}' attribute is missing")

    @classmethod
    def get_model(cls, load_wrapper):
        if cls.model is None and load_wrapper:
            cls.model = cls.load(load_wrapper)
        return cls.model

    @staticmethod
    def load(load_wrapper):
        model = None
        if settings.MODEL_PATH.endswith("/"):
            path = f"{MODEL_PATH}{MODEL_NAME_TRANSFORM}"
        else:
            path = f"{MODEL_PATH}/{MODEL_NAME_TRANSFORM}"
        if not os.path.exists(path):
            message = f"Machine learning model at {path} not exists!"
            #logger.error(message)
            raise FileNotFoundError(message)
        model = load_wrapper(path)
        if not model:
            message = f"Model {model} could not load!"
            #logger.error(message)
            raise ModelLoadException(message)
        return model

    
    @classmethod
    def load_evaluate_data(cls, path):
        trajectories = list()
        for i, eachlines in enumerate(open(path, 'r').readlines()):
            trajectories.append(eval(eachlines))
        trajectories = tf.keras.preprocessing.sequence.pad_sequences(trajectories, padding='post')
        return trajectories
