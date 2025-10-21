import jiwer
from pathlib import Path

raw_reference = Path("C:/Users/ct524/Documents/Transcripts/ComparisonTesting/reference/processed_r/mssa_hvt_1896_p1of1_transcript_control.txt").read_text(encoding = "utf-8")
#print(raw_reference)
#raw_hypothesis = Path("C:/Users/ct524/Documents/Transcripts/ComparisonTesting/generated/Processed_aTrain/mssa_hvt_1063_p1of2_aTrain.txt").read_text(encoding = "utf-8")  


strip_signal1 = jiwer.RemoveKaldiNonWords()(raw_reference)
strip_spaces1 = jiwer.RemoveMultipleSpaces()(strip_signal1)
strip_empty1 = jiwer.RemoveEmptyStrings()(strip_spaces1)
strip_newlines = jiwer.SubstituteRegexes({r"\n": r" "})(strip_empty1)
strip_punc1 = jiwer.RemovePunctuation()(strip_newlines)
#strip_punc1 = jiwer.ToLowerCase()(strip_e)
tolowercase1 = jiwer.ToLowerCase()(strip_punc1)
print(tolowercase1)
#reference = jiwer.ReduceToListOfListOfWords()(strip_punc1)
#print(reference)

'''
strip_spaces2 = jiwer.RemoveMultipleSpaces()(raw_hypothesis)
strip_empty2 = jiwer.RemoveEmptyStrings()(strip_spaces2)
strip_punc2 = jiwer.RemovePunctuation()(strip_empty2)
#normalize_diacritics = jiwer.SubstituteRegexes({r"Ã©": r"é",r"Ã¨": r"è",r"Ã.{1}xa0":r"à",r"Ã´": r"ô",r"Ãª": r"ê", r"Ãa": r"ça",r"Ã¹": r"ù"})(strip_punc2)
#normalize_diacritics2 = jiwer.SubstituteWords({'Ã':'à'})(normalize_diacritics)
#tolowercase2 = jiwer.ToLowerCase()(strip_punc2)
hypothesis = jiwer.ReduceToListOfListOfWords()(strip_punc2)

#str_reference = str(reference, encoding="utf=8")
#str_hypothesis = str(hypothesis, encoding="utf-8")

with open("C:/Users/ct524/Documents/Transcripts/ComparisonTesting/Hebrew_aTrain_compare_2025-10-20_5.txt", "a", encoding="utf-8") as f:
    f.write(str(reference))
    f.write('\nHypothesis: \n')
    f.write(str(hypothesis))

print('Done')

#hypothesis_l = jiwer.ReduceToListOfListOfWords()(raw_hypothesis)
#hypothesis = str(hypothesis_l)


tr1 = jiwer.Compose([jiwer.RemoveKaldiNonWords(),
        jiwer.RemoveEmptyStrings(),
        jiwer.RemoveMultipleSpaces(),
        jiwer.ExpandCommonEnglishContractions(),
        jiwer.RemovePunctuation(),
        jiwer.ReduceToListOfListOfChars()])

tr2 = jiwer.Compose([
    jiwer.RemoveEmptyStrings(),
    jiwer.RemoveMultipleSpaces(),
    jiwer.ExpandCommonEnglishContractions(),
    jiwer.RemovePunctuation(),
    jiwer.ReduceToListOfListOfChars()])   
    
output = jiwer.process_words(reference, hypothesis, reference_transform=tr1, hypothesis_transform=tr2)
'''