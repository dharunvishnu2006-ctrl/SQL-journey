from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, joinedload

Base = declarative_base()


class Agent(Base):
    __tablename__ = 'agents_orm'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(String)

    tasks = relationship('Task', back_populates='agent')


class Task(Base):
    __tablename__ = 'tasks_orm'

    id = Column(Integer, primary_key=True)
    title = Column(String)

    agent_id = Column(Integer, ForeignKey('agents_orm.id'))
    agent = relationship('Agent', back_populates='tasks')


engine = create_engine('sqlite:///sentinel_orm.db')

Session = sessionmaker(bind=engine)
session = Session()

print("--- Without joinedload ---")

agents = session.query(Agent).all()

for agent in agents:
    print(agent.name)

    for task in agent.tasks:
        print("  -", task.title)

print("--- With joinedload ---")

agents = (
    session.query(Agent)
    .options(joinedload(Agent.tasks))
    .all()
)

for agent in agents:
    print(agent.name)

    for task in agent.tasks:
        print("  -", task.title)


session.close()