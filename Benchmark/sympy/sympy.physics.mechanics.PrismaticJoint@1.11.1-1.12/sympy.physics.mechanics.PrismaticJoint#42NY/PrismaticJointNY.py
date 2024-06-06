from sympy.physics.mechanics import Body, PrismaticJoint
parent = Body('P')
child = Body('C')
joint = PrismaticJoint('PC',  parent,  child,  None,  None,  None,  None, parent_axis=None, child_axis=None)
