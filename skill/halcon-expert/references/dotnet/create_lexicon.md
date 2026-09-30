# CreateLexicon (Operator)

## Name

`CreateLexicon` — Create a lexicon from a tuple of words.

## Signature

`static void HOperatorSet.CreateLexicon(HTuple name, HTuple words, out HTuple lexiconHandle)`

`public HLexicon(string name, HTuple words)`

`void HLexicon.CreateLexicon(string name, HTuple words)`

## Description

`CreateLexicon` creates a new lexicon based on a tuple of
*`words`*. By specifying a unique textual *`name`*, you
can later refer to the lexicon from syntax expressions like those
used, e.g., by [`DoOcrWordMlp`](do_ocr_word_mlp.md).

Note that lexicon support in HALCON is currently not aimed at
natural languages. Rather, it is intended as a post-processing
step in OCR applications that only need to distinguish between
a limited set of not more than a few thousand valid words, e.g.,
country or product names. MVTec itself does not provide any lexica.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`name`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Unique name for the new lexicon.

Default:
"lex1"

**`words`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Word list for the new lexicon.

Default:
["word1","word2","word3"]

**`lexiconHandle`** (output_control)  lexicon `→` [HLexicon](HLexicon.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the lexicon.

## Possible Successors

`DoOcrWordMlp`,
`DoOcrWordSvm`

## Alternatives

`ImportLexicon`

## See also

`LookupLexicon`,
`SuggestLexicon`

## Module

OCR/OCV
