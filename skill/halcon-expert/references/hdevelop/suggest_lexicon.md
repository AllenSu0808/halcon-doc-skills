# suggest_lexicon (Operator)

## Name

`suggest_lexicon` — Find a similar word in a lexicon.

## Signature

`suggest_lexicon( : : LexiconHandle, Word : Suggestion, NumCorrections)`

## Description

`suggest_lexicon` compares *`Word`* to all words in
the lexicon and calculates the minimum number of edit operations
*`NumCorrections`* required to transform *`Word`*
into a word from the lexicon. Valid edit operations are the
insertion, deletion and replacement of characters. The most
similar word found in the lexicon is returned in *`Suggestion`*.
If there are multiple words with the same minimum number of
corrections, only the first of those words is returned.

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

**`Suggestion`** (output_control)  string `→`  (string)

Most similar word found in the lexicon.

**`NumCorrections`** (output_control)  integer `→`  (integer)

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
