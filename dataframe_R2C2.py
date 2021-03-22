# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fileio_R2C2 import parse_args_R2C2, read_fasta, df_to_csv, df_to_fasta

# %%
cols = 'readName_averageQuality_originalReadLength_numberOfRepeats_subreadLength'.split('_') + ['sequence']

# %%
def reads_to_df(reads):
    print('construct a dataframe from reads dict, columns are:')
    readsData = [k[1:].split('_') + [reads[k]] for k in reads]
    print(cols)
    df = pd.DataFrame(readsData, columns=cols, dtype='string')
    df['averageQuality'] = pd.to_numeric(df['averageQuality'])
    df['originalReadLength'] = pd.to_numeric(df['originalReadLength'])
    df['numberOfRepeats'] = pd.to_numeric(df['numberOfRepeats'])
    df['subreadLength'] = pd.to_numeric(df['subreadLength'])
    return df

# %%
def plot_df_scatter(df, x, y):
    print('plot df scatter')
    print('x: ' + x)
    print('y: ' + y)
    df.plot(x = x, y = y, kind = 'scatter')
    plt.show()

# %%
def filter_df(df):
    filter_ = df['numberOfRepeats'] >= 3
    return df[filter_]
# %%
def main():
    input_reads, output_path = parse_args_R2C2()
    reads = read_fasta(input_reads)
    df = reads_to_df(reads)
    # plot_df_scatter(df, 'numberOfRepeats', 'averageQuality')
    dff = filter_df(df)
    df_to_csv(df.iloc[:, :-1], output_path + "/R2C2_Consensus_headers.csv")
    df_to_fasta(dff, output_path + "/R2C2_Consensus_filtered_numberOfRepeats_greater_3.fasta")

if __name__ == '__main__':
    main()