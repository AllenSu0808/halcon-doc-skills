# import_lexicon (Operator)

## Name

`import_lexicon` — Create a lexicon from a text file.

## Signature

`import_lexicon( : : Name, FileName : LexiconHandle)`

## Description

`import_lexicon` creates a new lexicon based on a list of words in
the file specified by *`FileName`*. The format of the file is a simple
text file with one word per line. By specifying a unique textual
*`Name`*, you can later refer to the lexicon from syntax expressions
like those used, e.g., by [`do_ocr_word_mlp`](do_ocr_word_mlp.md).

Note that lexicon support in HALCON is currently not aimed at
natural languages. Rather, it is intended as a post-processing
step in OCR applications that only need to distinguish between
a limited set of not more than a few thousand valid words, e.g.,
country or product names.
When the lexicon file contains entries with special, non-ASCII characters,
it is expected to be encoded in UTF-8.
However, old lexicon files which use the local 8-bit encoding, can still
be loaded as long as they contain at least one byte sequence, which cannot
be misinterpreted as UTF-8 character.
MVTec itself does not provide any lexica.

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

**`FileName`** (input_control)  filename.read `→`  (string)

Name of a text file containing words for the new lexicon.

Default:
'words.txt'

File extension:
.`txt`

**`LexiconHandle`** (output_control)  lexicon `→`  (handle)

Handle of the lexicon.

## Possible Successors

`do_ocr_word_mlp`,
`do_ocr_word_svm`

## Alternatives

`create_lexicon`

## See also

`lookup_lexicon`,
`suggest_lexicon`

## Module

OCR/OCV
