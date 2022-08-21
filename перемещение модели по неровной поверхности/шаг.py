import maya.cmds as cmd
import math
def save():
    cmd.setKeyframe( ['head_ctrl', 'cog_ctrl', 'master_ctrl', 'l_leg_ik_ctrl', 'r_leg_ik_ctrl', 'r_toe_ctrl', 'l_toe_ctrl', 'l_arm_ik_ctrl', 'l_arm_elbow_ctrl', 'r_arm_ik_ctrl', 
    'r_arm_elbow_ctrl', 'spine_chest_isolated_ctrl'], breakdown = 0,  hierarchy='none', controlPoints = 0,  shape = 0)
def switch(left, right, is_left):
    if (is_left):
        return left
    else:
        return right
def turn(ang, time, starting_point):
    cmd.currentTime(starting_point)
    print(starting_point)
    save()
    
    t = (starting_point+time/2.0)
    cmd.currentTime(t)
    
    print(t)
    cmd.select('head_ctrl', replace = True)
    cmd.rotate(0, ang, 0, relative = True)
    cmd.select('l_leg_ik_ctrl', replace= True)
    cmd.move(0, 0, ang*(-10.0/90.0), relative = True)
    cmd.rotate(0, ang/2.0, 0, relative = True)
    cmd.select('spine_chest_isolated_ctrl', replace = True)
    cmd.rotate(ang/2.0, 0, 0, relative = True)
    save()
    
    cmd.currentTime(starting_point+time)
    print(starting_point+time)
    cmd.select('head_ctrl', replace = True)
    cmd.rotate(0, -ang, 0, relative = True)
    cmd.select('l_leg_ik_ctrl', replace= True)
    cmd.move(0, 0, -ang*(-10.0/90.0), relative = True)
    cmd.rotate(0, -ang/2, 0, relative = True)
    cmd.select('spine_chest_isolated_ctrl', replace = True)
    cmd.rotate(-ang/2, 0, 0, relative = True)
    cmd.select('master_ctrl', replace= True)
    cmd.rotate(0, ang, 0, relative = True)
    save()
    
    
def step(dx, dy, dz, is_left, starting_point):
    mod = (dx**2+dy**2+dz**2)**(0.5)
    base_ang = cmd.xform('master_ctrl', worldSpace=True, ro = True, q = True)
    if (dz != 0):
        ang = math.atan(dx/dz)*180.0/math.pi
        if (dz<0):
            turn(ang-180, 5.0, starting_point)
        else:
            turn(ang, 5.0, starting_point)
    else:
        if (dx > 0):
            turn(90, 5.0, starting_point)
        else:
            turn(-90, 5.0, starting_point)
    starting_point+=5
    cmd.currentTime(starting_point)
    print(starting_point)
    cmd.setAttr('cog_ctrl.translate', 0, 0,0, type = "double3")
    
    cmd.setAttr('spine_chest_isolated_ctrl.rotate', 0, 0,0, type = "double3")
    
    cmd.setAttr('head_ctrl.translate', 0, 155,-5, type = "double3")
    
    cmd.setAttr(switch('l_arm_elbow_ctrl', 'r_arm_elbow_ctrl', is_left)+'.translate', 0, 0, 0, type = "double3")
    cmd.setAttr(switch('l_arm_elbow_ctrl', 'r_arm_elbow_ctrl', is_left)+'.rotateX', 0)
    
    cmd.setAttr(switch('l_arm_ik_ctrl', 'r_arm_ik_ctrl', not is_left)+'.translate', 30, -40, 0, type = "double3")
    cmd.setAttr(switch('l_arm_ik_ctrl', 'r_arm_ik_ctrl', not is_left)+
    '.rotate', 0, 25, 90, type = "double3")

    cmd.setAttr(switch('l_arm_ik_ctrl', 'r_arm_ik_ctrl', is_left)+'.translate', -30, -30, 10, type = "double3")
    cmd.setAttr(switch('l_arm_ik_ctrl', 'r_arm_ik_ctrl', is_left)+
    '.rotate', 0, -30, -90, type = "double3")
    
    cmd.setAttr(switch('l_leg_ik_ctrl', 'r_leg_ik_ctrl', is_left)+
    '.translate', 0, 0, 0, type = "double3")
    cmd.setAttr(switch('l_leg_ik_ctrl', 'r_leg_ik_ctrl', is_left)+
    '.rotate', 0, 0, 0, type = "double3")
    
    cmd.setAttr(switch('l_leg_ik_ctrl', 'r_leg_ik_ctrl', not is_left)+
    '.translate', 0, 0, 0, type = "double3")
    cmd.setAttr(switch('l_leg_ik_ctrl', 'r_leg_ik_ctrl', not is_left)+
    '.rotate', 0, 0, 0, type = "double3")

    cmd.setAttr(switch('l_toe_ctrl', 'r_toe_ctrl', not is_left)+
    '.translate', 0, 0, 0, type = "double3")
    cmd.setAttr(switch('l_toe_ctrl', 'r_toe_ctrl', not is_left)+
    '.rotate', 0, 0, 0, type = "double3") 

    cmd.setAttr(switch('l_arm_elbow_ctrl', 'r_arm_elbow_ctrl', not is_left)+
    '.translate', 0, 0, 0, type = "double3")
    cmd.setAttr(switch('l_arm_elbow_ctrl', 'r_arm_elbow_ctrl', not is_left)+
    '.rotateX', 0) 
    
    save()
    
    cmd.currentTime(starting_point + mod*0.13)
    print(starting_point + mod*0.13)
    cmd.select('master_ctrl', replace = True)   
    cmd.move(dx, dy, dz, relative = True)
    save()
    
    cmd.currentTime(starting_point+0.03*mod)
    print(starting_point+0.03*mod)
    cmd.select('cog_ctrl', replace = True)   
    cmd.move(0, mod*(-0.12), mod*(-0.03), relative = True)
    
    cmd.select('spine_chest_isolated_ctrl', replace = True)   
    cmd.rotate(0, 0, 0.13*mod/90, relative = True)
    
    cmd.select(switch('l_arm_ik_ctrl', 'r_arm_ik_ctrl', not is_left), replace = True)   
    cmd.move(0.067*mod, 0.067*mod, 0, relative = True)
    cmd.rotate(-1.13*mod/90, 0.73*mod/90, -1.2*mod/90, relative = True)    
    
    cmd.select(switch('l_arm_ik_ctrl', 'r_arm_ik_ctrl', is_left), replace = True)   
    cmd.rotate(-0.2*mod/90, -0.13*mod/90, -0.067*mod/90, relative = True) 
    
    cmd.select('head_ctrl', replace = True)   
    cmd.move(0, -0.1*mod, 0.06*mod, relative = True)
    cmd.rotate(5, 5, 0, relative = True)
    
    
    
    cmd.select(switch('l_arm_elbow_ctrl', 'r_arm_elbow_ctrl', is_left), replace = True)   
    cmd.move(0, -0.067*mod, -0.067*mod, relative = True)
    cmd.rotate(-0.13*mod/90, relative = True)
    
    cmd.select(switch('l_leg_ik_ctrl', 'r_leg_ik_ctrl', is_left), replace = True)   
    cmd.move(0, 0.067*mod, -0.1*mod, relative = True)
    cmd.rotate(0.13*mod/90, 0, 0, relative = True)
    
    cmd.select(switch('l_leg_ik_ctrl', 'r_leg_ik_ctrl', not is_left), replace = True)   
    cmd.move(0, 0.067*mod, -0.1*mod, relative = True)
    cmd.rotate(0.27*mod/90, 0, 0, relative = True)    

    cmd.select(switch('l_toe_ctrl', 'r_toe_ctrl', not is_left), replace = True)   
    cmd.rotate(-0.23*mod/90, relative = True)
    
    cmd.select(switch('l_arm_elbow_ctrl', 'r_arm_elbow_ctrl', not is_left), replace = True)   
    cmd.move(0, -0.067*mod, 0, relative = True)  
    
    save()
    
    cmd.currentTime(starting_point+0.06*mod);
    print(starting_point+0.06*mod)
    
    cmd.select('cog_ctrl', replace = True)   
    cmd.move(0, mod*(0.29), mod*(0.03), relative = True)
    
    cmd.select('spine_chest_isolated_ctrl', replace = True)   
    cmd.rotate(0, 0, -0.13*mod/90, relative = True)    
    
    cmd.select('head_ctrl', replace = True)   
    cmd.move(0, 0.27*mod, -0.06*mod, relative = True)
    cmd.rotate(-5, -5, 0, relative = True)
    
    cmd.select(switch('l_arm_elbow_ctrl', 'r_arm_elbow_ctrl', is_left), replace = True)   
    cmd.move(0, -0.067*mod, -0.067*mod, relative = True)
    cmd.rotate(-0.13*mod/90, relative = True)

    cmd.select(switch('l_arm_ik_ctrl', 'r_arm_ik_ctrl', not is_left), replace = True)   
    cmd.move(0, 0.2*mod, -0.17*mod, relative = True)
    cmd.rotate(1.07*mod/90, -0.8*mod/90, -1.2*mod/90, relative = True)    

    cmd.select(switch('l_leg_ik_ctrl', 'r_leg_ik_ctrl', is_left), replace = True)   
    cmd.move(0, 0.2*mod, 0.43*mod, relative = True)
    cmd.rotate(-0.3*mod/90, 0, 0, relative = True)  
    
    cmd.select(switch('l_leg_ik_ctrl', 'r_leg_ik_ctrl', not is_left), replace = True)   
    cmd.move(0.17*mod, 0.26*mod, 0, relative = True)

    cmd.select(switch('l_toe_ctrl', 'r_toe_ctrl', not is_left), replace = True)   
    cmd.rotate(0.23*mod/90, relative = True)    

    cmd.select(switch('l_arm_elbow_ctrl', 'r_arm_elbow_ctrl', not is_left), replace = True)   
    cmd.move(0, -0.067*mod, 0, relative = True)
    
    cmd.select(switch('l_arm_ik_ctrl', 'r_arm_ik_ctrl', is_left), replace = True)   
    cmd.move(-0.07*mod, 0.33*mod, 0.2*mod, relative = True)
    cmd.rotate(0.8*mod/90, 0, -1*mod/90, relative = True)

    save()
    
    cmd.currentTime(starting_point+0.093*mod)
    print(starting_point+0.093*mod)
    
    cmd.setAttr(switch('l_leg_ik_ctrl', 'r_leg_ik_ctrl', not is_left)+
    '.translate', 0.053*mod, 0.17*mod, 0.13*mod, type = "double3")    
    cmd.setAttr(switch('l_leg_ik_ctrl', 'r_leg_ik_ctrl', not is_left)+
    '.rotate', -0.03*mod, 0, 0, type = "double3")         
    
    save()
    
    cmd.currentTime(starting_point+0.047*mod)
    print(starting_point+0.047*mod)
    cmd.setAttr(switch('l_leg_ik_ctrl', 'r_leg_ik_ctrl', not is_left)+
    '.translate', 0, 0.17*mod, -0.23*mod, type = "double3")
    
    save()
    return starting_point + mod*0.13