#!/usr/bin/env ipython
from datetime import date
from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()


@router.get("/points/", response_model=List[schemas.DublinPoints])
def read_dublin_meta_by_line(
    *,
    db: Session = Depends(deps.get_db),
    # line_id: Optional[int] = None,
    journey_id: Optional[str] = None,
    turn: Optional[str] = None,
    start_date: Optional[date],
    end_date: Optional[date],
) -> Any:
    """
    Get dublin_points by "meta" parameters
    """

    if turn:
        try:
            delta = settings.TURNOS[turn]
        except:
            raise HTTPException(
                status_code=404,
                detail="Turn must be within: \
            DAWN, MORNING, AFTERNOON, EVENING",
            )
    else:
        delta = None

    param = {
        # "line_id": line_id,
        "journey_id": journey_id,
        "turn": turn,
        "start_date": start_date,
        "end_date": end_date,
    }
    print(start_date)
    kwargs = {k: v for k, v in param.items() if v is not None}

    if kwargs:
        dp = crud.dublin_points.get_traj_by_multiparam(db=db, **kwargs)
    else:
        dp = crud.dublin_points.get_random_traj(db=db)

    if not dp:
        raise HTTPException(status_code=404, detail="DublinPoints not found")

    return dp


# @router.get("/trajectory/{traj_id}", response_model=List[schemas.DublinPoints])
# def read_dublin_points(*, db: Session = Depends(deps.get_db), traj_id: int,) -> Any:
#     """
#     Get dublin_points by trajectory_id.
#     """
#     dp = crud.dublin_points.get_by_trajectory(db=db, traj_id=traj_id)
#
#     if not dp:
#         raise HTTPException(status_code=404, detail="DublinPoints not found")
#     return dp
#
