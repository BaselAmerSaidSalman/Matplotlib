# Matplotlib => مسئولة عن الرس البياني للبيانات
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x = [1,2,3,4,5,6,7,8,9,10]
y = [10,20,30,40,50,60,70,80,90,100]

# Make a graph with x & y axis => parameters => (label, color, linewidth, linestyle, marker) => (label => الاسماء, color => اللون, linewidth => عرض الخط البياني, linestyle => نوع الخط البياني, marker => شكل الخط البياني)
plt.plot(x, y ,color='graph_color' ,label='graph_name' , linestyle='line_style' ,marker='graph_shape', linewidth='line_width')  # in color => (r => red, k => black, w => white, b => blue, y => yellow), in linestyle => (-- => خط مقطع, - => خط عادي), in marker => (o => عمل دوائر مكان البيانات على الجراف), in linewidth => سمك الخط

# Make a bar with x & y axis => parameters => (label, color, width) => (label => الاسماء, color => اللون, width => العرض)
plt.bar(x,y, color='bar_color' ,label='bar_name', width='bar_width')

# Make a pie with x & y axis => parameters => (color, labels, explode, shadow, wedgeprops, startangle, autopct='%1.1f%%', rotatelabels) => (color => اللون, labels => الاسماء, explode => مقدار خروج الجزء من الفطيرة, shadow => الظل(True, False), wedgeprops => لون حدود الاجزاء, startangle => الزاويه التي تبدا من عندها عرض البيانات, autopct => كتابة النسب على الرسم, rotatelabels => دوران الفطيرة(True, False)) 
data = [60, 20, 15, 5]
labels = ['Python', 'HTML', 'CSS', 'JavaScript']
explode = [0,0,0,0]
plt.pie(data, labels=labels, explode=explode, shadow=True, wedgeprops={'edgecolor' : 'black'}, startangle=50, autopct="%1.1f%%", rotatelabels=True)



# Make a histogram with x & y axis => parameter => (bins, edgecolor) => (bins => تحديد ما يكتب على محور س, edgecolor => لون الحواف)
z = [10,20,30,40,50,60,10,20,25,30,40,80,50]
plt.hist(z, edgecolor='red', bins=[1,5,10])

# Make a vertical line that = mean
mean = np.mean(z)
plt.axvline(mean)



# Make a Scatter Plots with x & y axis => parameter => (c, s, edgecolors, linewidths, alpha, cmap) => (c => color, s => size, edgecolors => لون الحواف بتاعت النقط, linewidths => عرض او سمك الحافه, alpha => شفافيه النقاط, cmap => تدرج الوان النقاط(Greens, Reds))
plt.scatter(x, y, c='red', s=2, edgecolors='black', linewidths=2, alpha=0.75, cmap='Reds')

# Make a color bar & Make a name for color bar
plt.colorbar().set_label('color_bar_name')



# Make a subplots with x & y axis => (subplots => تقسيم البيانات بتاعت الجراف اي الخط البياني الى اكثر من صف او عمود) => parameter => (nrows, ncols, sharex, sharey, figsize) => (nrows => عدد الصفوف, ncols => عدد الاعمدة, sharex => جعل محور س مشترك بين الرسمتين, sharey => جعل محور ص مشترك بين الرسمتين, figsize => طول وعرض الرسمة البيانيه (width, height))
fig, axis = plt.subplots(nrows=1, ncols=2)
x = [1,2,3,4,5,6,7,8,9,10]
y = [10,20,30,40,50,60,70,80,90,100]
z = [5,15,25,35,45,55,65,75,85,95]

axis[0].plot(x, y, color='r')
axis[0].set_title('graph_one_name')
axis[0].set_xlabel('X_1')
axis[0].set_ylabel('Y_1')

axis[1].plot(x, z, color='k')
axis[1].set_title('graph_two_name')
axis[1].set_xlabel('X_2')
axis[1].set_ylabel('Y_2')
plt.show()

# Separate between 2 graphs that made with subplot
plt.tight_layout()



# Show the graph
plt.show()

# Title
plt.title('My first graph')

# X-axis name
plt.xlabel('x-axis_name')

# Y-axis name
plt.ylabel('y-axis_name')


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

# Replace list instead of another list in x-axis
plt.xticks('list that in x-axis', 'list that you want to put it in x-axis')

# Replace list instead of another list in y-axis
plt.yticks('list that in y-axis', 'list that you want to put it in y-axis') 


# to put 2 bars Side by Side
import numpy as np
x = [1,2,3,4,5,6,7,8,9,10]
y = [10,20,30,40,50,60,70,80,90,100]

w = [10,26,30,42,50,57,75,80,90,100]

x_1 = np.arange(len(x))
width = 0.35

plt.bar(x_1 - width/2, y, width=width, label='first')
plt.bar(x_1 + width/2, w, width=width, label='second')
plt.xticks(x_1, x)

plt.show()


# to put 3 or above Side by Side
x = [1,2,3,4,5,6,7,8,9,10]
y = [10,20,30,40,50,60,70,80,90,100]

w = [10,26,30,42,50,57,75,80,90,100]

d = [15,20,33,40,49,60,73,82,90,100]

x_1 = np.arange(len(x))
width = 0.25

plt.bar(x_1 - width, y, width=width, label='first')
plt.bar(x_1, w, width=width, label='second')
plt.bar(x_1 + width, d, width=width, label='third')
plt.xticks(x_1, x)

plt.show()
