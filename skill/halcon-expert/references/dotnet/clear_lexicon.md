# ClearLexicon (Operator)

## Name

`ClearLexicon` — Clear a lexicon.

## Signature

`static void HOperatorSet.ClearLexicon(HTuple lexiconHandle)`

`void HLexicon.ClearLexicon()`

## Description

`ClearLexicon` clears a lexicon and releases its resources.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- lexiconHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`lexiconHandle`** (input_control, state is modified)  lexicon `→` [HLexicon](HLexicon.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the lexicon.

## See also

`CreateLexicon`

## Module

OCR/OCV
