from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class Agent(Base):
    __tablename__ = 'agents_orm'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(String)


engine = create_engine('sqlite:///sentinel_orm.db')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

agent1 = Agent(name='Agent-01', status='active')
agent2 = Agent(name='Agent-02', status='idle')

session.add(agent1)
session.add(agent2)

session.commit()

agents = session.query(Agent).all()

for agent in agents:
    print(agent.name, agent.status)

session.close()