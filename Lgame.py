def common_member(a,b):
    l1=set(a)
    l2=set(b)
    if(l1 & l2):
        s=[]
        s= l1 & l2
        return f'-----------ELEMENTS OF LIST ARE AS FOLLOWS----------- List 1  : {l1} List 2  : {l2} Common element in lists  : {s}'
    else:return f'No common elements'

def equal(a,b):
	l1=len(a)
	l2=len(b)
	if(l1==l2):
		return f'Lists are of equal length and can be multiplied element wise'
		s=[]
		s=[a[i] * b[i] for i in range(l1)]
		return f'Multiplied list is : {s}'
	else:
		return f'Lists are not of equal length'


	
