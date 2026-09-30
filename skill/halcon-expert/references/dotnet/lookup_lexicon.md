# LookupLexicon (Operator)

## Name

`LookupLexicon` — Check if a word is contained in a lexicon.

## Signature

`static void HOperatorSet.LookupLexicon(HTuple lexiconHandle, HTuple word, out HTuple found)`

`int HLexicon.LookupLexicon(string word)`

## Description

`LookupLexicon` checks whether *`word`* is
contained in the lexicon *`lexiconHandle`*, and returns
1 in *`found`* if the word is found, otherwise 0.

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

**`found`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Result of the search.

## Alternatives

`SuggestLexicon`

## See also

`CreateLexicon`

## Module

OCR/OCV
