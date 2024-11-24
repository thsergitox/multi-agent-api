import uuid
from sqlalchemy import Column, Text, ForeignKey, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.session import Base

class ChatMessage(Base):
    __tablename__ = "chat_messages"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    content = Column(Text, nullable=False)
    chatbot_data = Column(JSON, nullable=True)  # Stores chatbot-related data in JSON format
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    
    project = relationship("Project", back_populates="chat_messages")
    user = relationship("User", back_populates="chat_messages")