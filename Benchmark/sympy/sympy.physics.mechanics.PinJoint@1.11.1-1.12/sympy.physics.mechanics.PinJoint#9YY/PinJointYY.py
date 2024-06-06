from sympy.physics.mechanics import Body, PinJoint
parent = Body('P')
child = Body('C')
joint = PinJoint(name='PC', parent=parent, child=child, coordinates=None)
