from datetime import datetime
from enum import Enum
from sqlalchemy import Integer, String, DateTime, Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from app.src.db.database import Base


class Status(Enum):
    PENDING = "Pending"
    PROCESSING = "Processing"
    COMPLETED = "Completed"
    FAILED = "Failed"


class Job(Base):
    __tablename__ = "jobs"

    job_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    status: Mapped[Status] = mapped_column(
        SqlEnum(Status),
        nullable=False,
        default=Status.PENDING
    )

    count_of_users: Mapped[int] = mapped_column(Integer, nullable=False)
    format: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )
    result: Mapped[str] = mapped_column(String, nullable=True)