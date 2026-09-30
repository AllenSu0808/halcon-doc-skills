# create_lexicon (Operator)

## Name

`create_lexicon` — Create a lexicon from a tuple of words.

## Signature

`create_lexicon( : : Name, Words : LexiconHandle)`

## Description

`create_lexicon` creates a new lexicon based on a tuple of
*`Words`*. By specifying a unique textual *`Name`*, you
can later refer to the lexicon from syntax expressions like those
used, e.g., by [`do_ocr_word_mlp`](do_ocr_word_mlp.md).

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

**`Name`** (input_control)  string `→`  (string)

Unique name for the new lexicon.

Default:
'lex1'

**`Words`** (input_control)  string-array `→`  (string)

Word list for the new lexicon.

Default:
['word1','word2','word3']

**`LexiconHandle`** (output_control)  lexicon `→`  (handle)

Handle of the lexicon.

## Possible Successors

`do_ocr_word_mlp`,
`do_ocr_word_svm`

## Alternatives

`import_lexicon`

## See also

`lookup_lexicon`,
`suggest_lexicon`

## Module

OCR/OCV
