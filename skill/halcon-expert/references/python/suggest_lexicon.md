# suggest_lexicon (Operator)

## Name

`suggest_lexicon` — Find a similar word in a lexicon.

## Signature

`def suggest_lexicon(lexicon_handle: HHandle, word: str) -> Tuple[str, int]`

## Description

`suggest_lexicon` compares *`word`* to all words in
the lexicon and calculates the minimum number of edit operations
*`num_corrections`* required to transform *`word`*
into a word from the lexicon. Valid edit operations are the
insertion, deletion and replacement of characters. The most
similar word found in the lexicon is returned in *`suggestion`*.
If there are multiple words with the same minimum number of
corrections, only the first of those words is returned.

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

**`suggestion`** (output_control)  string `→` str

Most similar word found in the lexicon.

**`num_corrections`** (output_control)  integer `→` int

Difference between the words in edit operations.

## Alternatives

`lookup_lexicon`,
`tuple_str_distance`

## See also

`create_lexicon`

## References

Vladimir I. Levenshtein, Binary codes capable of correcting deletions, insertions,
and reversals, Doklady Akademii Nauk SSSR, 163(4):845-848, 1965 (Russian).
English translation in Soviet Physics Doklady, 10(8):707-710, 1966.

## Module

OCR/OCV
