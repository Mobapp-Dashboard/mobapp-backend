from .crud_dublin_meta import dublin_meta
from .crud_dublin_model import dublin_model
from .crud_dublin_model_detection_region import dublin_model_detection_region
from .crud_dublin_model_eval import dublin_model_eval
from .crud_dublin_model_points import dublin_model_points
from .crud_dublin_model_scores import dublin_model_scores
from .crud_dublin_points import dublin_points
from .crud_item import item
from .crud_user import user

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
