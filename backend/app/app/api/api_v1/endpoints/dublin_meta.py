from datetime import date
from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/journeys_by_date/", response_model=List[schemas.DublinJourneys])
def read_journeys_by_date(
    *,
    db: Session = Depends(deps.get_db),
    start_date: Optional[date],
    end_date: Optional[date]
) -> Any:
    """
    Get dublin trajectories (ROTAS)
    """
    dublin_meta = crud.dublin_meta.get_journey_by_date(
        db=db, start_date=start_date, end_date=end_date
    )

    if not dublin_meta:
        raise HTTPException(status_code=404, detail="DublinMeta not found")

    return dublin_meta


@router.get("/trajs_by_journey_date/", response_model=List[schemas.DublinTrajs])
def read_trajs_by_journeys_date(
    *,
    db: Session = Depends(deps.get_db),
    journey_id: Optional[str],
    start_date: Optional[date],
    end_date: Optional[date]
) -> Any:
    """
    Get dublin trajectories (ROTAS).
    """
    dublin_meta = crud.dublin_meta.get_traj_by_journey_date(
        db=db, journey_id=journey_id, start_date=start_date, end_date=end_date
    )

    if not dublin_meta:
        raise HTTPException(status_code=404, detail="DublinMeta not found")

    return dublin_meta


@router.get("/meta_trajectory/", response_model=List[schemas.DublinLines])
def read_dublin_meta_by_line(
    *,
    db: Session = Depends(deps.get_db),
    line_id: Optional[int] = None,
    journey_id: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None
) -> Any:
    """
    Get dublin_meta by line_id."
    TODO: Ver uma forma de todas as colunas poderem ser parte da query
    sem fazer todas as queries
    """
    if line_id and journey_id:
        dublin_meta = crud.dublin_meta.get_by_line_journey(
            db=db, line_id=line_id, journey_id=journey_id
        )
    elif line_id:
        dublin_meta = crud.dublin_meta.get_by_line(db=db, line_id=line_id)
    elif journey_id:
        dublin_meta = crud.dublin_meta.get_by_journey(
            db=db, journey_id=journey_id, start_date=start_date, end_date=end_date
        )
    else:
        dublin_meta = crud.dublin_meta.get_all_metas(db=db)

    if not dublin_meta:
        raise HTTPException(status_code=404, detail="DublinMeta not found")

    return dublin_meta
