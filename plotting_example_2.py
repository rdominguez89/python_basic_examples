import matplotlib.pyplot as plt
import numpy as np

n = 10
x = np.arange(n)
y = np.arange(n)
x_err = np.zeros(n)+0.25
y_err = np.zeros(n)+0.5
[var1,var2] = [1,1.1234]

fig = plt.figure(figsize = plt.figaspect(0.3)*1.0)

plt.subplot(1,2,1)
plt.errorbar(x,y,xerr=x_err ,yerr=y_err ,marker='.' ,color='blue' , ms=9 ,fmt='--' ) 
plt.xlabel(r"x , $\alpha$ -- %i -- %.2f" %(var1,var2), fontsize=15)
plt.ylabel(r"y , $\beta$ -- %i -- %.3f" %(var1,var2), fontsize=15)
plt.title("Plot with associated error")
plt.text(0.2, 8, r"Text, $\sum_a^b - \int_c^d$ -- %i -- %.2f" %(var1,var2), fontsize=15)
plt.ylim(0,10)
plt.xlim(0,10)
plt.legend(['Data_test_1','Data_test_2'],loc=4 , shadow=True , ncol=1 ,fontsize= 15)
plt.show()
