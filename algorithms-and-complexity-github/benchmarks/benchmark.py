"""Synthetic median sorting runtimes (milliseconds)."""
import csv,random,statistics,sys,time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from sorting.algorithms import insertion_sort,merge_sort,hybrid_sort

def benchmark(sizes=(50,200,800,1500),repeats=5):
 rng=random.Random(42);rows=[]
 for n in sizes:
  data=[rng.randrange(-10000,10000) for _ in range(n)]
  for name,fn in [('insertion',insertion_sort),('merge',merge_sort),('hybrid',hybrid_sort)]:
   elapsed=[]
   for _ in range(repeats):
    t=time.perf_counter();result=fn(data);elapsed.append((time.perf_counter()-t)*1000)
    assert result==sorted(data)
   rows.append({'size':n,'algorithm':name,'median_ms':round(statistics.median(elapsed),5)})
 return rows

if __name__=='__main__':
 with open(Path(__file__).parent/'results.csv','w',newline='') as stream:
  writer=csv.DictWriter(stream,['size','algorithm','median_ms']);writer.writeheader();writer.writerows(benchmark())
 print('Saved benchmarks/results.csv')
