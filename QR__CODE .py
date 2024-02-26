#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install QRcode


# In[1]:


import qrcode
import matplotlib.pyplot as plt
data = "www.youtube.com/@canaraengineeringcollegema3340"
filename = "My_QR_Code.png"
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save(filename)
plt.imshow(img, cmap='gray')
plt.axis('off')  
plt.show()


# In[ ]:




