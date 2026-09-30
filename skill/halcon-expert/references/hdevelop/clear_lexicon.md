# clear_lexicon (Operator)

## Name

`clear_lexicon` — Clear a lexicon.

## Signature

`clear_lexicon( : : LexiconHandle : )`

## Description

`clear_lexicon` clears a lexicon and releases its resources.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- LexiconHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`LexiconHandle`** (input_control, state is modified)  lexicon `→`  (handle)

Handle of the lexicon.

## See also

`create_lexicon`

## Module

OCR/OCV
