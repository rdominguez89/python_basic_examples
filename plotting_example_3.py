import matplotlib.pyplot as plt
import numpy as np

x_1 = np.arange(0,9)+0.25
y_1 = np.linspace(1,10**6,9)

fig = plt.figure(figsize = plt.figaspect(0.3)*1.0)

plt.subplot(1,2,1)
[x_2,y_2] = [np.arange(2,11)-0.25,np.linspace(1,10**6,9)]
plt.plot(x_1,y_1,'-')
plt.plot(x_2,y_2,'--')
plt.xlabel(r"x , linear", fontsize=15)
plt.ylabel(r"y ,log10", fontsize=15)

plt.yscale('log')
plt.ylim(0.01,10**7)
plt.xlim(0,9.5)
plt.legend(['Data_test_1','Data_test_2'],loc=4 , shadow=True , ncol=1 ,fontsize= 15)

plt.subplot(1,2,2)
plt.subplots_adjust(wspace = 0.03)
[x_2,y_2] = [np.arange(2,11)-0.25,np.linspace(1,10**6,9)]
plt.plot(x_1,y_1,'.-')
plt.plot(x_2,y_2,'^-')
plt.xlabel(r"x , linear", fontsize=15)
plt.yscale('log')
plt.ylim(0.01,10**7)
plt.xlim(0,9.5)
plt.legend(['Data_test_1','Data_test_2'],loc=4 , shadow=False , ncol=2 ,fontsize= 15)
plt.tick_params(labelleft=False)
plt.show() 
