# %%
import argparse

# %%
def parse_args_R2C2():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_fasta', type=str)
    parser.add_argument('-o', '--output_path', type=str)
    args = parser.parse_args()
    output_path = args.output_path + '/'
    input_reads = args.input_fasta
    return input_reads, output_path

# %%
def read_fasta(infile):
    print('reading: ' + infile)
    reads = {}
    name, sequence = '', ''
    f = open(infile)
    for line in f:
      if line and line.strip():
        a = line.strip()
        if a[0] == '>':
            if sequence != '':
                reads[name] = sequence
            name = a[1:].split()[0]
            sequence = ''
        else:
            sequence += a
    if sequence != '':
        reads[name] = sequence
    f.close()
    return reads
# %%
def df_to_csv(dfR2C2, out):
    print("export dataframe to csv")
    dfR2C2.to_csv(out, index=False)
# %%
def df_to_fasta(dfR2C2, out):
    print("export dataframe to fasta")
    with open(out, "w") as f:
        for row_label, row in dfR2C2.iterrows():
            head = '>' + '_'.join(row.astype('string').iloc[:-1].to_list())
            seq = row['sequence']
            f.write('%s\n%s' %(head, seq))


# %%
