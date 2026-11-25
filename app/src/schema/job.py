from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class Status(Enum):
    PENDING = 'Pending'
    PROCESSING = 'Processing'
    COMPLETED = 'Completed'
    FAILED = 'Failed'


#     marital_status = Column(SqlEnum(MaritalStatus), nullable=True) uses for model
class UserSchema(BaseModel):
    job_id: int
    status: Status
    count_of_users: int
    format: str
    created_at: datetime
    result: str

    class Config:
        orm_mode = True