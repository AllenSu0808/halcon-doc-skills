# SuggestLexicon (Operator)

## Name

`SuggestLexicon` — Find a similar word in a lexicon.

## Signature

`static void HOperatorSet.SuggestLexicon(HTuple lexiconHandle, HTuple word, out HTuple suggestion, out HTuple numCorrections)`

`string HLexicon.SuggestLexicon(string word, out int numCorrections)`

## Description

`SuggestLexicon` compares *`word`* to all words in
the lexicon and calculates the minimum number of edit operations
*`numCorrections`* required to transform *`word`*
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

**`lexiconHandle`** (input_control)  lexicon `→` [HLexicon](HLexicon.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the lexicon.

**`word`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Word to be looked up.

Default:
"word"

**`suggestion`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Most similar word found in the lexicon.

**`numCorrections`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Difference between the words in edit operations.

## Alternatives

`LookupLexicon`,
`TupleStrDistance`

## See also

`CreateLexicon`

## References

Vladimir I. Levenshtein, Binary codes capable of correcting deletions, insertions,
and reversals, Doklady Akademii Nauk SSSR, 163(4):845-848, 1965 (Russian).
English translation in Soviet Physics Doklady, 10(8):707-710, 1966.

## Module

OCR/OCV
