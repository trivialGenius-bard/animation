import maya.cmds as cmd
import math

def mod(x, y, z):
    return (x**2+y**2+z**2)**(0.5)
    
def move_to(start, finish):
    vector_a = cmd.xform('pasted__pPlane2.f['+str(start)+']', worldSpace=True, query = True, t = True)
    cmd.select('master_ctrl', replace = True)
    cmd.move(vector_a[0], vector_a[1], vector_a[2])
    a=start
    b=finish
    s_p = 1
    is_left = True
    while(a!=b):
        vector_a = cmd.xform('pasted__pPlane2.f['+str(a)+']', worldSpace=True, query = True, t = True)
        xa = a//10
        ya = a%10
        xb = b//10
        yb = b%10
        cell = [0, 0, 0]
        if (xb>xa):
            cell[0] = a+10
        elif (xb < xa):
            cell[0] = a-10
        if (yb > ya):
            cell[1] = a+1
        elif (yb<ya):
            cell[1] = a-1
        else:
            cell[1] = cell[0]
        if (xa == xb):
            cell[0] = cell[1]
        if ((xa != xb) and (ya!=yb)):    
            cell[2] = (cell[0]+cell[1])-a
        else:
            cell[2] = cell[0]
        cell_coor = [[], [], []]
        cell_coor[0] = cmd.xform('pasted__pPlane2.f['+ str(cell[0])+']', worldSpace=True, t = True, q = True)
        cell_coor[1] = cmd.xform('pasted__pPlane2.f['+ str(cell[1])+']', worldSpace=True, t = True, q = True)
        cell_coor[2] = cmd.xform('pasted__pPlane2.f['+ str(cell[2])+']', worldSpace=True, t = True, q = True)
        mod_cell = [cell_coor[0][1]**2, cell_coor[1][1]**2, cell_coor[2][1]**2]
        
        min_y_mod = min(mod_cell)
        min_y_index = mod_cell.index(min_y_mod)
        
        print(cell[min_y_index])
        s_p = step(cell_coor[min_y_index][0]-vector_a[0], cell_coor[min_y_index][1]-vector_a[1],
                        cell_coor[min_y_index][2]-vector_a[2], is_left, s_p)
        #is_left = not is_left
        a = cell[min_y_index]