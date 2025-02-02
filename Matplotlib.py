# Matplotlib => مسئولة عن الرس البياني للبيانات
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9,10]
y = [10,20,30,40,50,60,70,80,90,100]

# Put data on x & y axis 
plt.plot(x, y ,color='graph_color' ,label='graph_name' ,linestyle='line_style' ,marker='graph_shape', linewidth='line_width')  # in color => (r => red, k => black, w => white, b => blue, y => yellow), in linestyle => (-- => خط مقطع, - => خط عادي), in marker => (o => عمل دوائر مكان البيانات على الجراف), in linewidth => سمك الخط

# Show the graph
plt.show()

# Title
plt.title('My first graph')

# X-axis name
plt.xlabel('x-axis')

# Y-axis name
plt.ylabel('y-axis')


# the graph line information
plt.legend(['first_graph_line_name', 'second_graph_line_name'])

# مربعات الرسم البياني
plt.grid()

# save 
plt.savefig('image_name.png or.jpg')

# graph styles
plt.style.available

# to use the graph style in your graph
plt.style.use('style_name')



