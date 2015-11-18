import os
import sys
import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class appInputs(Base):

    __tablename__ = 'app_inputs'
    id = Column(Integer, primary_key=True)
    kp = Column(Float)
    ki = Column(Float)
    kd = Column(Float)
    setpoint = Column(Float)
    description = Column(String(250))
    added_date = Column(DateTime, default=datetime.datetime.utcnow)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'kp': self.kp,
            'ki': self.ki,
            'kd': self.kd,
            'setpoint': self.setpoint,
            'description': self.description,
        }

class appOutputs(Base):

    __tablename__ = 'app_outputs'
    id = Column(Integer, primary_key=True)
    voltage = Column(Float)
    pwm_sent = Column(Float)
    input_id = Column(Integer, ForeignKey('app_inputs.id'))
    app_inputs = relationship(appInputs)
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'voltage': self.voltage,
            'pwm_sent': self.pwm_sent,
            'input_id': self.input_id,
            'app_inputs': self.app_inputs,
        }

engine = create_engine('sqlite:///appdata.db')

Base.metadata.create_all(engine)
