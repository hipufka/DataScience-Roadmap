import matplotlib.pyplot as plt

#Classic plotting
def plot_time(d, x_label=None, title=None, out_file=None):

    plt.figure(figsize=(12, 6))

    plt.plot(list(d.keys()), list(d.values()), label='time')
    
    for x,y in zip(list(d.keys()), list(d.values())):
        label = "{:.0f}".format(y)
        plt.annotate(label, (x,y), textcoords="offset points", xytext=(0,10), ha='center') 
    
    plt.xlabel(x_label)
    plt.ylabel('Time')
    
    if title:
        plt.title(title)

    #plt.legend(prop={'size': 12})
    
    if out_file:
        plt.savefig(out_file)
        
    plt.show()
   
#Nice alternative for Pandas
def plot_pd(d):
    ax = d[['orders']].plot.bar(rot=0,title='Orders by groups',color='blue',bins=[0,10,20,30,40,50,100,200,500])
    plt.show()
    
#Correlations heatmap
def plot_heatmap(d):
    
    import seaborn as sns
    
    c = df[['order_cnt','AOV','comment_name_cnt','has_loyalty']].corr()
    f, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(c, vmax=.8, square=True, annot=True, cmap="Blues")
