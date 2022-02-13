#!/usr/bin/env ipython
from datetime import date
from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()


@router.get("/", response_model=List[schemas.DublinPoints])
def read_dublin_meta_by_line(
    *,
    db: Session = Depends(deps.get_db),
    # line_id: Optional[int] = None,
    dataset: Optional[str] = None,
    journey_id: Optional[str] = None,
    turn: Optional[str] = None,
    start_date: Optional[date],
    end_date: Optional[date],
) -> Any:
    """
    Get GPD points by meta-parameters
    """

    param = {
        "journey_id": journey_id,
        "turn": turn,
        "start_date": start_date,
        "end_date": end_date,
    }
    kwargs = {k: v for k, v in param.items() if v is not None}

    if kwargs:
        dp = crud.dublin_points.get_traj_by_multiparam(db=db, **kwargs)
    else:
        dp = crud.dublin_points.get_random_traj(db=db)

    if not dp:
        raise HTTPException(status_code=404, detail="DublinPoints not found")

    return dp
