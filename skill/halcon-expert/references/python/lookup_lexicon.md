# lookup_lexicon (Operator)

## Name

`lookup_lexicon` — Check if a word is contained in a lexicon.

## Signature

`def lookup_lexicon(lexicon_handle: HHandle, word: str) -> int`

## Description

`lookup_lexicon` checks whether *`word`* is
contained in the lexicon *`lexicon_handle`*, and returns
1 in *`found`* if the word is found, otherwise 0.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`lexicon_handle`** (input_control)  lexicon `→` HHandle

Handle of the lexicon.

**`word`** (input_control)  string `→` str

Word to be looked up.

Default:
"word"

**`found`** (output_control)  integer `→` int

Result of the search.

## Alternatives

`suggest_lexicon`

## See also

`create_lexicon`

## Module

OCR/OCV
