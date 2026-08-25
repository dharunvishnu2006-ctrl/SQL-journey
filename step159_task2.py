from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

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

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

agent3 = Agent(name='Agent-03', status='active')

task1 = Task(title='Scan network', agent=agent3)
task2 = Task(title='Analyze threats', agent=agent3)

session.add(agent3)
session.commit()

active_agents = session.query(Agent).filter(
    Agent.status == 'active'
).all()

for agent in active_agents:
    print(agent.name)

    for task in agent.tasks:
        print("  -", task.title)

session.close()