#!/usr/bin/env ipython

from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/model_points/", response_model=List[schemas.DublinModelPoints])
def read_dublin_meta_by_line(
    *,
    db: Session = Depends(deps.get_db),
    trajectory_id: Optional[int] = None,
    rota: Optional[int]
) -> Any:
    """
    Get dublin_meta by line_id.
    """
    # TODO: Ver uma forma de todas as colunas poderem ser parte da query
    # sem fazer todas as queries
    if trajectory_id is not None:
        if (trajectory_id < 0) | (trajectory_id >= 100):
            raise HTTPException(
                status_code=406,
                detail="A trajetória deve estar compreendida entre 0 e 100",
            )
    if (rota < 0) | (rota > 63):
        raise HTTPException(
            status_code=406, detail="A rota deve estar compreendida entre 0 e 63"
        )

    dp = crud.dublin_model_points.get_points_by_rota_traj(
        db=db, trajectory_id=trajectory_id, rota=rota
    )

    if not dp:
        raise HTTPException(status_code=404, detail="DublinMeta not found")

    return dp


@router.get("/evals/{method}/{rota}", response_model=List[schemas.DublinModelEval])
def read_evals_by_method(
    *, db: Session = Depends(deps.get_db), method: str, rota: int
) -> Any:
    "Get pre-computed evals by models"
    evals = crud.dublin_model_eval.get_by_method_rota(db=db, method=method, rota=rota)
    if not evals:
        raise HTTPException(status_code=404, detail="Evals not found")
    return evals


@router.get("/scores/{route}", response_model=List[schemas.DublinModelScores])
def read_score_by_route(*, db: Session = Depends(deps.get_db), route: int) -> Any:
    "Get pre-computed scores by models"
    scores = crud.dublin_model_scores.get_score_by_route(db, route=route)
    if not scores:
        raise HTTPException(status_code=404, detail="Evals not found")
    return scores


@router.get(
    "/predictions/{method}/{route}",
    response_model=List[schemas.DublinModelDetectionRegion],
)
def read_evals_by_method(
    *, db: Session = Depends(deps.get_db), method: str, route: int
) -> Any:
    "Get pre-computed evals by models"
    preds = crud.dublin_model_detection_region.get_by_method_route(
        db=db, method=method, route=route
    )
    if not preds:
        raise HTTPException(status_code=404, detail="Evals not found")
    return preds
