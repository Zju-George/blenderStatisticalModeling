import bpy
import math
#from mathutils import Vector
import numpy as np


def Point_at(obj, direction):
    if(type(direction)!=Vector):
       direction=Vector(direction)
    # point the obj 'Y' and use its 'Z' as up
    rot_quat = direction.to_track_quat('Y', 'Z')

    # assume we're using euler rotation
    obj.rotation_euler = rot_quat.to_euler()
    return
def GaussianKernelValue(point1,point2, sigma=10.0):
    distance=(point1[0]-point2[0])**2+(point1[1]-point2[1])**2+(
        point1[2]-point2[2])**2
    tmp=-1*distance/sigma**2
    result = math.exp(tmp)
    print('result is: {}'.format(result))
    return

def SpawnArrows(number=5):
    #spawun 5 * 5 arrows
    arrow=bpy.data.objects['Arrow']
    arrow.location = [0,0,1]
    for y in range(0,number):
        for x in range(0,number):
            newarrow = arrow.copy()
            newarrow.name='Arrow'+str(y*number+x)
            newarrow.location=[x,y,0]
            bpy.context.scene.objects.link(newarrow)
    return

print('statical modeling imported!')

if __name__ == '__main__':
    #arrow = bpy.data.objects['Arrow']
    #point_at(arrow,(1,1,0))
    testMat=np.array([[1,2,2],[2,1,2],[2,2,1]])
    evals,evecs=np.linalg.eig(testMat)
    result=np.zeros((3,3))
    print(evals)
    big2small_indices = np.argsort(evals).tolist()
    big2small_indices.reverse()

    for i in range(3):
        eval=evals[big2small_indices[i]]
        print('eval is: {}'.format(eval))
        result+=eval*np.dot(evecs[:,[big2small_indices[i]]],
        np.reshape(evecs[:,big2small_indices[i]],(1,3)))
        print(result)
        pass
    



