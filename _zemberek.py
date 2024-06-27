from zemberek import (
    TurkishSpellChecker,
    TurkishSentenceNormalizer,
    TurkishSentenceExtractor,
    TurkishMorphology,
    TurkishTokenizer
)


morphology = TurkishMorphology.create_with_defaults()

normalizer = TurkishSentenceNormalizer(morphology)

tokenizer = TurkishTokenizer.DEFAULT


def zbrk(sentence):
    return normalizer.normalize(sentence)

def zbrky(sentence):
    core=""
    analysis = morphology.analyze_sentence(sentence)
    
    for e in analysis:
        for s in e:
            s=s.format_string()
            s=s.split(":")
            s=s[1].split(" ")
            s=s[0]
            core=s[0:-1]
    return core

def zbrkc(data):
    datas=[]
    datas.append(data)
    for token in datas:
        tokenler = tokenizer.tokenize(token)
        cumle=""
        for t in tokenler:
            analiz = morphology.analyze(t.normalized)
            if analiz.analysis_results:
                p=str(analiz.analysis_results[0])
                p=p.split(" ")
                p=p[0]
                p=p.split(":")
                a=p[0]
                a=a[1:]
                cumle=a
        return cumle
