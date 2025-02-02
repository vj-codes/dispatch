from typing import List, Optional

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy_utils import TSVectorType

from dispatch.database.core import Base
from dispatch.models import DispatchBase


class Organization(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    default = Column(Boolean)
    description = Column(String)
    projects = relationship("Project", backref="organization")

    search_vector = Column(
        TSVectorType("name", "description", weights={"name": "A", "description": "B"})
    )


class OrganizationBase(DispatchBase):
    id: Optional[int]
    name: str
    description: Optional[str]
    default: Optional[bool]


class OrganizationCreate(OrganizationBase):
    pass


class OrganizationUpdate(OrganizationBase):
    pass


class OrganizationRead(OrganizationBase):
    id: int


class OrganizationPagination(DispatchBase):
    total: int
    items: List[OrganizationRead] = []
