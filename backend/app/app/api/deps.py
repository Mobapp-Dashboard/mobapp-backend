from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.core import security
from app.core.config import settings
from app.db.session import SessionLocal
#import tensorflow as tf
#
import numpy as np
import pandas as pd

#model = tf.saved_model.load(settings.MODEL_PATH + settings.MODEL_NAME_TRANSFORM)

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> models.User:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = crud.user.get(db, id=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_current_active_user(
    current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not crud.user.is_active(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def get_current_active_superuser(
    current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user

def load_trajectories_from_npy(rota):
    traj_type = ["traj", "traj_anom"]
    traj_dict = {}
    for tt in traj_type:
        x = np.load(
            settings.DATA_DIR + f'/{rota}/dublin_test_{tt}.npy')

        dfs = []
        for i, xi in enumerate(x):
            df = pd.DataFrame(xi)
            df['traj'] = i
            df['point_num'] = df.index
            dfs.append(df)
        df = pd.concat(dfs)
        df.columns = ["lat", "lng", "a", "b", "traj", "point_num"]
        traj_dict[tt] = df
    return traj_dict
#
