from sympy.physics.mechanics import Body, PrismaticJoint
parent = Body('P')
child = Body('C')
joint = PrismaticJoint(name='PC', parent=parent, child=child, coordinates=None, speeds=None, parent_joint_pos=None, child_joint_pos=None, parent_axis=None, child_axis=None)
