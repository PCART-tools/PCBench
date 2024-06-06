from sympy.physics.mechanics import Body, PinJoint
parent = Body('P')
child = Body('C')
joint = PinJoint('PC', parent=parent, child=child, coordinates=None, speeds=None)
