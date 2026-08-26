from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, relationship
from datetime import datetime

class Base(DeclarativeBase):
    pass

class ThreatActor(Base):
    __tablename__ = "threat_actors"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    country = Column(String)

class IPAddress(Base):
    __tablename__ = "ip_addresses"

    id = Column(Integer, primary_key=True)
    ip = Column(String, nullable=False, unique=True)

class ThreatEvent(Base):
    __tablename__ = "security_events"

    id = Column(Integer, primary_key=True)
    event_type = Column(String, nullable=False)
    severity = Column(String)
    severity_score = Column(Integer)
    event_time = Column(DateTime, default=datetime.utcnow)

    actor_id = Column(Integer, ForeignKey("threat_actors.id"))
    source_ip = Column(Integer, ForeignKey("ip_addresses.id"))

    actor = relationship("ThreatActor")
    ip_address = relationship("IPAddress")        