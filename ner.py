import hanlp

# Flask constructor takes the name of
# current module (__name__) as argument.

recognizer = hanlp.load(hanlp.pretrained.ner.MSRA_NER_BERT_BASE_ZH)

def extract_loc(text):
    res = recognizer([list(text)])
    ans = []
    if res != None and len(res) > 0:
        for entity in res[0]:
            if len(entity) != 4:
                continue
            (value,label,start,end) = entity
            if label == 'NT' or label == 'NS':
                if len(value) < 2:
                    continue
                loc = {
                    "value" : value,
                    "start" : start,
                    "end"   : end,
                }
                ans.append({"loc":loc})
    return ans
 
# main driver function
if __name__ == '__main__':
    ans = extract_loc("我在朝阳大望路")
    print(ans)
