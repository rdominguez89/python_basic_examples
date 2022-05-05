import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,10)
y = np.arange(1,10)
[var1,var2] = [1,1.1234]

fig = plt.figure(figsize = plt.figaspect(0.3)*1.0)

plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("Basic plot")
plt.xlabel(r"x , $\alpha$ -- %i -- %.2f" %(var1,var2), fontsize=15)
plt.ylabel(r"y , $\beta$ -- %i -- %.3f" %(var1,var2), fontsize=15)
plt.text(0.2, 8, r"Text, $\sum_a^b - \int_c^d$ -- %i -- %.2f" %(var1,var2), fontsize=15)
plt.ylim(0,10)
plt.xlim(0,10)
plt.legend(['Data_test_1'],loc=4 , shadow=True , ncol=1 ,fontsize= 15)

plt.subplot(1,2,2)
plt.plot(x,y)
plt.title("Basic plot, with values at 4 axis and more text presition")
plt.xlabel(r"x , $\alpha$ -- %i -- %.2f" %(var1,var2), fontsize=15)
plt.ylabel(r"y , $\beta$ -- %i -- %.3f" %(var1,var2), fontsize=15)
plt.text(0.2, 8, r"Text with four numbers after comma, %.4f" %(var2), fontsize=15)
plt.tick_params(labelright=True)
plt.tick_params(labeltop=True)
plt.ylim(0,10)
plt.xlim(0,10)
plt.legend(['Data_test_2']         
            ,loc=4 , shadow=True , ncol=1 ,fontsize= 15)
plt.show()
