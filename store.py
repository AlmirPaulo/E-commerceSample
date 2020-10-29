from browser import document as doc
from browser.local_storage import storage 
from browser import console 

def buy(ev):
    for i in doc['opt']:
        if i.selected:
            storage[i.value] = i.value + ' size T-Shirt'
            doc['cart'] <= storage[i.value]+ ' '
doc['btn'].bind('click', buy)
