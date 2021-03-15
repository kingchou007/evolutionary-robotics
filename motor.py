import numpy
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p
import os.path


class MOTOR:
    def __init__(self, joint_name):
        self.frequency = c.frontLegFrequency
        self.offset = c.frontLegPhaseOffset
        self.amplitude = c.frontLegAmplitude
        self.jointName = joint_name
        self.motorValues = numpy.zeros(c.timeSteps)
        self.Prepare_To_Act(self.jointName)

    def Prepare_To_Act(self, joint_name):
        if joint_name == 'Torso_BackLeg':
            self.amplitude = c.backLegAmplitude
            self.frequency = c.backLegFrequency
            self.offset = c.backLegPhaseOffset
            self.motorValues = self.amplitude * numpy.sin(numpy.linspace(
                -self.frequency * numpy.pi + self.offset, self.frequency * numpy.pi + self.offset, num=c.timeSteps))
        else:
            self.motorValues = self.amplitude * numpy.sin(numpy.linspace(
                -self.frequency * numpy.pi + self.offset, self.frequency * numpy.pi + self.offset, num=c.timeSteps))

    # def Set_Value(self, robot, time_step):
    #     pyrosim.Set_Motor_For_Joint(
    #         bodyIndex=robot,
    #         jointName=self.jointName,
    #         controlMode=p.POSITION_CONTROL,
    #         targetPosition=self.motorValues[time_step],
    #         maxForce=c.motorForce)

    def Set_Value(self, robot, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robot,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=c.motorForce)

    def Save_Values(self):
        numpy.save(os.path.join('data', str(self.jointName) + 'MotorValues.npy'), self.motorValues)









