from sqlalchemy import (
    Column,
    String,
    Text,
    Integer,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import CreatedAtMixin
from .post_tags import post_tags_association_table


class Post(CreatedAtMixin, Base):
    title = Column(String(200), unique=False, nullable=False)
    body = Column(Text, nullable=False, default="")
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)

    # orm
    author = relationship("Author", back_populates="posts", uselist=False)

    tags = relationship(
        "Tag", secondary=post_tags_association_table, back_populates="posts"
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r})"

    def __repr__(self):
        return str(self)
