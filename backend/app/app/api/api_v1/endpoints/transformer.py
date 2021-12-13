#!/usr/bin/env ipython
from typing import Any

#from app.core.config.settings import DATA_DIR
from app.core.config import settings
from app.api import deps
#from core.errors import PredictException

from fastapi import APIRouter, HTTPException, Depends

#from models.transformer_prediction import TransformerModelResponse, TransformerHealthResponse
from app.services.transformer_predict import TransformerModelHandlerScores as model
import pandas as pd
import numpy as np

router = APIRouter()

#@router.get("/evaluation")
#async def predict_transformer():
#    try:
#        evaluation = model.predict('dsdsds', clf=tf_model)
#        return evaluation
#    except Exception as e:
#        raise HTTPException(status_code=404, detail=e)


@router.get("/evaluationX/{rota}/{traj}")
async def predict_transformerX(
        #tf_model = Depends(deps.model),
        #trajectories: dict = Depends(),
        rota: int = 0,
        traj: int = 0):
    try:
        evaluation = model.predict("asd", rota=rota, traj=traj)
        compare = list(map(lambda x, y: x != y,
                           evaluation["Prediction"][1:],
                           evaluation["RealData"]))
        trajectories = deps.load_trajectories_from_npy(rota)
        if (traj < 50):
            df = trajectories["traj"]
        else:
            df = trajectories["traj_anom"]
            traj = traj - 50
        df = df[df["traj"] == traj][["lat", "lng"]]
        return {
            "trajetoria": df.to_dict(),
            "anomalia_detectada": df[compare].to_dict()
        }
        # return evaluation
    except Exception as e:
        raise HTTPException(status_code=404, detail=e)

