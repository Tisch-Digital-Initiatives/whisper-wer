from pathlib import Path
import os
import jiwer

whisper_transcript = str(Path(input("\nEnter filepath to whisper (hypothesis) transcript:\n")))

with open(whisper_transcript, 'r') as file:
    hypothesis = file.read()

original_transcript = str(Path(input("\nEnter filepath to reference transcript:\n")))

with open(original_transcript, 'r', encoding="utf-8") as file:
    reference = file.read()

transforms = jiwer.Compose(
   [
        jiwer.ToLowerCase(),
        jiwer.ExpandCommonEnglishContractions(),
        jiwer.RemoveKaldiNonWords(),
        jiwer.RemovePunctuation(),  
        jiwer.RemoveWhiteSpace(replace_by_space=True),
        jiwer.RemoveMultipleSpaces(),
        jiwer.RemoveEmptyStrings(),
        jiwer.Strip(),
        jiwer.ReduceToSingleSentence(),
        jiwer.ReduceToListOfListOfWords(),
    ]
)

align = jiwer.process_words(reference,
    hypothesis,
    reference_transform=transforms,
    hypothesis_transform=transforms,)

print(jiwer.visualize_alignment(align))
