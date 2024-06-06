from sympy.physics.mechanics import Body, PrismaticJoint
parent = Body('P')
child = Body('C')
joint = PrismaticJoint('PC',  parent,  child,  None,  None, parent_joint_pos=None, child_joint_pos=None)
