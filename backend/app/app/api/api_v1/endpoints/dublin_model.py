#!/usr/bin/env ipython

from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/meta_trajectory/", response_model=List[schemas.DublinModel])
def read_dublin_meta_by_line(
    *,
    db: Session = Depends(deps.get_db),
    trajectory_id: Optional[int],
    routes: Optional[int]
) -> Any:
    """
    Get dublin_meta by line_id.
    """
    # TODO: Ver uma forma de todas as colunas poderem ser parte da query
    # sem fazer todas as queries
    if (trajectory_id < 0) | (trajectory_id >= 100):
        raise HTTPException(
            status_code=406,
            detail="A trajetória deve estar compreendida entre 0 e 100")
    if (routes < 0) | (routes > 63):
        raise HTTPException(
            status_code=406,
            detail="A rota deve estar compreendida entre 0 e 63")

    dm = crud.dublin_model.get_predictions(
        db=db, trajectory_id=trajectory_id, routes=routes)

    if not dm:
        raise HTTPException(status_code=404, detail="DublinMeta not found")

    return dm
