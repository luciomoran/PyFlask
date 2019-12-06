import pandas as pd
import matplotlib.pyplot as plt

def read_csv(file):
    df = pd.read_csv('./pdfs/' + file)
    return df

def graph_dataframe(route, columnY, columnX, option, nameGraph):
    try:
        df = read_csv(route)
        if(option == 'barra'):
            plt.hist(df[columnY], df[columnX])
        elif option == 'pastel':
            plt.pie(df[columnY], labels=df[columnX])
        else:
            plt.plot(df[columnY], 'b--')
        plt.savefig("{}.png".format(nameGraph))
    except SystemError as err:
        print(err)

