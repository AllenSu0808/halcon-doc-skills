# create_lexicon (Operator)

## Name

`create_lexicon` — Create a lexicon from a tuple of words.

## Signature

`def create_lexicon(name: str, words: Sequence[str]) -> HHandle`

## Description

`create_lexicon` creates a new lexicon based on a tuple of
*`words`*. By specifying a unique textual *`name`*, you
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

**`name`** (input_control)  string `→` str

Unique name for the new lexicon.

Default:
"lex1"

**`words`** (input_control)  string-array `→` Sequence[str]

Word list for the new lexicon.

Default:
["word1","word2","word3"]

**`lexicon_handle`** (output_control)  lexicon `→` HHandle

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
