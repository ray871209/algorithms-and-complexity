"""Pure Python educational sorting routines; inputs are not mutated."""
def insertion_sort(xs):
 a=list(xs)
 for i in range(1,len(a)):
  x=a[i];j=i-1
  while j>=0 and a[j]>x:a[j+1]=a[j];j-=1
  a[j+1]=x
 return a

def merge(a,b):
 out=[];i=j=0
 while i<len(a) and j<len(b):
  if a[i]<=b[j]:out.append(a[i]);i+=1
  else:out.append(b[j]);j+=1
 return out+a[i:]+b[j:]

def merge_sort(xs):
 a=list(xs)
 if len(a)<2:return a
 m=len(a)//2
 return merge(merge_sort(a[:m]),merge_sort(a[m:]))

def hybrid_sort(xs,threshold=24):
 if threshold<1:raise ValueError('threshold must be positive')
 a=list(xs)
 if len(a)<=threshold:return insertion_sort(a)
 m=len(a)//2
 return merge(hybrid_sort(a[:m],threshold),hybrid_sort(a[m:],threshold))
