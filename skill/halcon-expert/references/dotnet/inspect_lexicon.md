# InspectLexicon (Operator)

## Name

`InspectLexicon` — Query all words from a lexicon.

## Signature

`static void HOperatorSet.InspectLexicon(HTuple lexiconHandle, out HTuple words)`

`HTuple HLexicon.InspectLexicon()`

## Description

`InspectLexicon` returns a tuple of all words in the
lexicon in the parameter *`words`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`lexiconHandle`** (input_control)  lexicon `→` [HLexicon](HLexicon.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the lexicon.

**`words`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

List of all words.

## Alternatives

`LookupLexicon`

## See also

`CreateLexicon`

## Module

OCR/OCV
