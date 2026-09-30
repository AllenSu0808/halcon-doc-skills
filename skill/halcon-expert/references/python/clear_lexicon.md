# clear_lexicon (Operator)

## Name

`clear_lexicon` — Clear a lexicon.

## Signature

`def clear_lexicon(lexicon_handle: HHandle) -> None`

## Description

`clear_lexicon` clears a lexicon and releases its resources.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- lexicon_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`lexicon_handle`** (input_control, state is modified)  lexicon `→` HHandle

Handle of the lexicon.

## See also

`create_lexicon`

## Module

OCR/OCV
