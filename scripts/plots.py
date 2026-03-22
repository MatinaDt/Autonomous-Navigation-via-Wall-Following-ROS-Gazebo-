import numpy as np
import matplotlib.pyplot as plt
#import scipy.integrate as integrate
#from scipy.integrate import quad

# Constant Values
L1=0.018
L2=0.05
L3=0.1
L4=0.2

### import and store data
def data_proccess(file):
    time=[]
    sonar_R=[]
    sonar_FR=[]
    sonar_L=[]
    linear_vel=[]
    ang_vel=[]
    xyz=[]

    file=open(file)
    lines = file.readlines()

    for l in lines:
        val=l.split('\t')
        val_array=np.array(val)
        time.append(float(val_array[0]))
        sonar_R.append(float(val_array[1]))
        sonar_FR.append(float(val_array[2]))
        sonar_L.append(float(val_array[3]))
        linear_vel.append(float(val_array[4]))
        ang_vel.append(float(val_array[5]))
        xyz.append([float(val_array[6]),float(val_array[7]),float(val_array[8])])

    sonar_R_array=np.array(sonar_R)
    sonar_FR_array=np.array(sonar_FR)
    sonar_L_array=np.array(sonar_L)
    linear_vel_array=np.array(linear_vel)
    ang_vel_array=np.array(ang_vel)
    xyz_array=np.array(xyz)
    return (time, sonar_R_array,  sonar_FR_array, sonar_L_array,linear_vel_array,ang_vel_array,xyz_array)

time, sonar_R,  sonar_FR, sonar_L, linear_vel, ang_vel , xyz= data_proccess("values.txt")

def plot_with_time(time,sonar_R,  sonar_FR, sonar_L,n=[],sy=True,plot_line=True):
    d_FR_ref=0.5
    fig, ax = plt.subplots(nrows=3, ncols=1, figsize=(9, 4), sharey=sy,sharex=True)

    if plot_line:
        ax[0].axhline(y=d_FR_ref*np.sqrt(2)/2-L1, xmin=min(time), xmax=max(time), c="black", linewidth=2)
        ax[1].axhline(y=d_FR_ref, xmin=min(time), xmax=max(time), c="black", linewidth=2)
        #ax[2].axhline(y=2, xmin=min(time), xmax=max(time), c="black", linewidth=2)

    ax[0].plot(time,sonar_R,color='m')
    ax[1].plot(time,sonar_FR,color='m')
    ax[2].plot(time,sonar_L,color='m')

    ax[0].set_title(n[0])
    ax[1].set_title(n[1])
    ax[2].set_title(n[2])

    ax[2].set_xlabel('Time(sec)')

    # for j in range (0,2):
    #     ax[1,0].set_title('y-axis')
    #     ax[2,0].set_title('z-axis')
    #     ax[0,0].legend(["x=0.617","kp=0","kp=20"],loc="lower right")
    #     ax[1,0].legend(["kp=0","kp=20"],loc="lower right")
    #     ax[2,0].legend(["z=0.199","kp=0","kp=20"],loc="lower right")

    for i in range(0,3):
        ax[i].grid()
        ax[i].set_xlim((min(time),max(time)))
        ax[i].set_facecolor('#d8dcd6')
    
    plt.subplots_adjust(bottom=0.15, wspace=0.05)

plot_with_time(time,sonar_R,  sonar_FR, sonar_L,["Right Sonar", "F-Right Sonar", "Left Sonar"])
#plot_with_time(time,xyz[:,0],xyz[:,1],xyz[:,2],["x-axes","y-axes","z-axes"],False,False)

#plt.figure(3)
#plt.plot(xyz[:,1],xyz[:,2])

def plot_vel_with_time(time,linear_vel,ang_vel):
   
    fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(9, 4), sharey=False,sharex=True)


    # ax[0].axhline(y=0, xmin=min(time), xmax=max(time), c="black", linewidth=2)
    # ax[1].axhline(y=0, xmin=min(time), xmax=max(time), c="black", linewidth=2)

    ax[0].plot(time,linear_vel,color='m')
    ax[1].plot(time,ang_vel,color='m')

    ax[0].set_title('Angular Velocity')
    ax[1].set_title('Linear Velocity')

    ax[1].set_xlabel('Time(sec)')

    # for j in range (0,2):
    #     ax[1,0].set_title('y-axis')
    #     ax[2,0].set_title('z-axis')
    #     ax[0,0].legend(["x=0.617","kp=0","kp=20"],loc="lower right")
    #     ax[1,0].legend(["kp=0","kp=20"],loc="lower right")
    #     ax[2,0].legend(["z=0.199","kp=0","kp=20"],loc="lower right")

    for i in range(0,2):
        ax[i].grid()
        ax[i].set_xlim((min(time),max(time)))
        ax[i].set_facecolor('#d8dcd6')
    
    plt.subplots_adjust(bottom=0.15, wspace=0.05)

plot_vel_with_time(time,linear_vel,ang_vel)
plt.show()
