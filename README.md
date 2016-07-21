# Python 3 required
Reason: python module 'datetime' needs python 3

# Module usage
## datetime module in python
```python
import datetime
d1 = datetime.datetime.strptime('10/Apr/2013:00:00:04 +0800', '%d/%b/%Y:%H:%M:%S %z')
d2 = datetime.datetime.strptime('10/Apr/2013:00:01:04 +0800', '%d/%b/%Y:%H:%M:%S %z')
d3 = d2 - d1
print (d3.seconds)  # printed is 60
```
