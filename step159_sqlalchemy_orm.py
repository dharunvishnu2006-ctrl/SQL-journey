from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, joinedload

Base = declarative_base()

class Experiment(Base):
    __tablename__ = 'experiments'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    runs = relationship('Run', back_populates='experiment')

class Run(Base):
    __tablename__ = 'runs'

    id = Column(Integer, primary_key=True)
    model_name = Column(String, nullable=False)
    accuracy = Column(Float, nullable=False)

    experiment_id = Column(Integer, ForeignKey('experiments.id'))
    experiment = relationship('Experiment', back_populates='runs')

engine = create_engine('sqlite:///orm_demo.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

exp1 = Experiment(name='Fraud Detection Sprint 1')

run1 = Run(model_name='RandomForest', accuracy=0.91, experiment=exp1)
run2 = Run(model_name='XGBoost', accuracy=0.95, experiment=exp1)

session.add(exp1)

session.commit()

print("--- Without joinedload ---")
experiments = session.query(Experiment).all()
for exp in experiments:
    print(exp.name)
    for run in exp.runs: 
        print("  -", run.model_name, run.accuracy)

print("--- With joinedload (N+1 fixed) ---")
experiments2 = session.query(Experiment).options(joinedload(Experiment.runs)).all()
for exp in experiments2:
    print(exp.name)
    for run in exp.runs:
        print("  -", run.model_name, run.accuracy)

session.close()