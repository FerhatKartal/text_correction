# pip install zemberek-python

from zemberek import (
    TurkishSpellChecker,
    TurkishSentenceNormalizer,
    TurkishSentenceExtractor,
    TurkishMorphology,
    TurkishTokenizer
)

# examples = ["kırmzı bir arba yolda duryor"]

morphology = TurkishMorphology.create_with_defaults()

normalizer = TurkishSentenceNormalizer(morphology)

def zbrk(sentence):
    core=""
    # for example in examples:
    #     print(example)
    #     print(normalizer.normalize(example), "\n")

    # results = morphology.analyze("kalemin")
    # for result in results:
    #     print(result)
    # print("\n")

    # SENTENCE ANALYSIS AND DISAMBIGUATION

    analysis = morphology.analyze_sentence(sentence)
    # after = morphology.disambiguate(sentence, analysis)

    # print("\nBefore disambiguation")
    for e in analysis:
        # print(f"Word = {e.inp}")
        for s in e:
            s=s.format_string()
            s=s.split(":")
            s=s[1].split(" ")
            s=s[1]
            core=s
    return core
    # print("\nAfter disambiguation")
    # son=""
    # for s in after.best_analysis():
    #     s=s.format_string()
    #     s=s.split(" ")
    #     son+=s[0]+"-"
    # print(son)


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
