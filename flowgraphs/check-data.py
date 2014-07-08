import scipy

template_len = 20

temp = scipy.fromfile(open("/tmp/diff-encode-out.bin"), 
        dtype=scipy.uint8, count=1000)
template = temp[100:template_len+100]
print len(template)
match = False
rec = scipy.fromfile(open("/tmp/rec-map-out.bin"), dtype=scipy.uint8, count=100000)
for i in range(9950):
    if (template == rec[i:template_len+i]).all():
        print i
        break
