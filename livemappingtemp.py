import _thread
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import csv
import time

def firstfunc():
    count=0
    with open('airtabletest.txt','r') as dataset:
    	line=csv.reader(dataset)
    	arr=[]
    	for row in line:
    		if(len(arr)>=9):
    			arr.clear()
    		for i in range(1,10):
    			arr.append(int(row[i]))
    		t=time.time()+3
    		while(t>time.time()):
    				pass
    		if(count>=5):
    			with open('live_graph1','r') as file:
    				lines=file.readlines()
    			with open('live_graph1','w') as csvfile:
    				csvfile.writelines(lines[1:])
    		with open('live_graph1','a+') as file:
    			arr2=[]
    			writer=csv.writer(file)
    			arr2.append(row[0][11:])
    			arr2.append(sum(arr)/10)
    			writer.writerow(arr2)
    			count+=1

def secondfunc():
    style.use('fivethirtyeight')

    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    def animate(i):
    	xs = []
    	ys = []
    	count=0
    	label=[]
    	with open('live_graph1','r') as file:
    		reader=csv.reader(file)
    		for row in reader:
    			if(len(row) == 2):
    				x = float(row[1])
    				xs.append(count)
    				ys.append(x)
    				label.append(row[0])
    				count+=1
    		ax1.clear()
    		ax1.set_xticks(xs)
    		ax1.set_xticklabels(label)
    		ax1.plot(xs,ys)
    		fig.autofmt_xdate()
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()

def main():
    try:
        _thread.start_new_thread(secondfunc,())
        _thread.start_new_thread(firstfunc,())
    except RuntimeError:
        pass

    while 1:
        pass

if __name__=='__main__':main()
