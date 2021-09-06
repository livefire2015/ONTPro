# ONTPro
This is a repo of tools for processing data from Oxford Nanpore Technologies

## HTSeq

```bash
python -m venv .venv

pip install -r requirements-htseq.txt

cd htseq

python setup.py build

python setup.py install

cd ..

python count.py -h

python count.py -s=no htseq/example_data/3356_sample_1_aln_hg19.sam htseq/example_data/hg19.refGene.gtf
```