import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
x=np.arange(0,10,0.01)
y=np.arange(0,10,0.1)

X,Y=np.meshgrid(x,y)
Z=0
for i in range(1,20,2):
      #Z=Z+(-1)**(i+1) * np.exp(-0.1*float(i)*np.pi*Y)*np.sin(float(i)*np.pi*x*0.1)*(1/float(i)) 
      #Z=Z+(1/float(i))*(np.cos(i*np.pi/2.0)-np.cos(i*np.pi))*np.sin(i*np.pi*X/20.0)*np.exp(i*np.pi*Y/20.0)
      #Z=Z+ (float(i)/(float(i)**2-1))*np.exp(-1*float(i)*Y)*np.sin(float(i)*X)
      #Z=Z+ (1/(float(i)*np.sinh(np.pi*i)))*np.sinh(i*np.pi*0.1*(10-Y))*np.sin(i*np.pi*X*0.1)
      #Z=Z+ (1/(float(i)*np.sinh(np.pi*i)))*np.sinh(i*np.pi*0.1*(10-Y))*np.sin(i*np.pi*X*0.1)+(1/(float(i)*np.sinh(np.pi*i)))*np.sinh(i*np.pi*0.1*(10-X))*np.sin(i*np.pi*Y*0.1)
      Z=Z+(1/float(i))*np.exp(-1*(i*np.pi*0.1)**2 *Y)*np.sin(i*np.pi*0.1*X)
#Z=Z*20.0/np.pi
#Z=Z*200.0/np.pi
#Z=Z*4.0/np.pi
Z=Z*400.0/np.pi
#Z=Z*100.0/np.pi

plt.figure()
plot=plt.contourf(X,Y,Z)
plt.xlabel('X')
plt.ylabel('t')
plt.colorbar(plot)
plt.savefig('diffusion2_ggplot.jpg')
plt.show()

