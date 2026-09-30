# lookup_lexicon (Operator)

## Name

`lookup_lexicon` — Check if a word is contained in a lexicon.

## Signature

`lookup_lexicon( : : LexiconHandle, Word : Found)`

## Description

`lookup_lexicon` checks whether *`Word`* is
contained in the lexicon *`LexiconHandle`*, and returns
1 in *`Found`* if the word is found, otherwise 0.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`LexiconHandle`** (input_control)  lexicon `→`  (handle)

Handle of the lexicon.

**`Word`** (input_control)  string `→`  (string)

Word to be looked up.

Default:
'word'

**`Found`** (output_control)  integer `→`  (integer)

Result of the search.

## Alternatives

`suggest_lexicon`

## See also

`create_lexicon`

## Module

OCR/OCV
