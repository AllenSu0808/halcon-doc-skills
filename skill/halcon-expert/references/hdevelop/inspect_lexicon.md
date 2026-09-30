# inspect_lexicon (Operator)

## Name

`inspect_lexicon` — Query all words from a lexicon.

## Signature

`inspect_lexicon( : : LexiconHandle : Words)`

## Description

`inspect_lexicon` returns a tuple of all words in the
lexicon in the parameter *`Words`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`LexiconHandle`** (input_control)  lexicon `→`  (handle)

Handle of the lexicon.

**`Words`** (output_control)  string(-array) `→`  (string)

List of all words.

## Alternatives

`lookup_lexicon`

## See also

`create_lexicon`

## Module

OCR/OCV
