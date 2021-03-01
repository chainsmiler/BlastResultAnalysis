from Bio.Blast import NCBIXML

def fprint(*args):
    print(*args,file = f)

f = open('newresult.txt','a',encoding='utf-8')

result_handle=open('X11YA90F114-Alignment.xml','r')

blast_records = NCBIXML.parse(result_handle)
for record in blast_records:
    fprint('Query:'+ record.query)
    m = record.query_length
    fprint('Query长度为：'+ str(record.query_length))
    for element in record.alignments:
        fprint('--Subject:'+ element.title)
        i = 1 
        for hsp in element.hsps:
            b = int(hsp.align_length)/int(m)
            if b > 0.8:
                fprint('----第{0}个比对结果：'.format(i))
                fprint('----query序列：'+ hsp.query)
                fprint('----subject序列：'+ hsp.sbjct)
                fprint('----覆盖长度为：'+ str(hsp.align_length))
                fprint('----覆盖比率为：{:.2f}'.format(int(hsp.align_length)/int(m)))
                i = i + 1
            else:
                continue
    fprint('\n') 

f.close()