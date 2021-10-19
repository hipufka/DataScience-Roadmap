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
