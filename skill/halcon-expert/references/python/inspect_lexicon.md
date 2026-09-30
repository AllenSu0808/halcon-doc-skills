# inspect_lexicon (Operator)

## Name

`inspect_lexicon` — Query all words from a lexicon.

## Signature

`def inspect_lexicon(lexicon_handle: HHandle) -> Sequence[str]`

`def inspect_lexicon_s(lexicon_handle: HHandle) -> str`

## Description

`inspect_lexicon` returns a tuple of all words in the
lexicon in the parameter *`words`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`lexicon_handle`** (input_control)  lexicon `→` HHandle

Handle of the lexicon.

**`words`** (output_control)  string(-array) `→` Sequence[str]

List of all words.

## Alternatives

`lookup_lexicon`

## See also

`create_lexicon`

## Module

OCR/OCV
