import uuid
from sqlalchemy import Column, String, Text, Boolean, ForeignKey, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.mutable import MutableList
from datetime import datetime
from app.db.session import Base


# Projects Table
class Project(Base):
    __tablename__ = "projects"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    is_public = Column(Boolean, default=False, nullable=False)
    main_file = Column(String(255), nullable=True)
    compilation_settings = Column(JSON, nullable=True)
    papers = Column(MutableList.as_mutable(JSON), default=list, nullable=True)  # Stores the list of papers as BSON-like JSON
    
    owner = relationship("User", back_populates="projects")
    chat_messages = relationship("ChatMessage", back_populates="project")