# clear_text_result (Operator)

## Name

`clear_text_result` — Clear a text result.

## Signature

`clear_text_result( : : TextResultID : )`

## Description

`clear_text_result` clears the text result in *`TextResultID`*
and frees all underlying memory.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- TextResultID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`TextResultID`** (input_control, state is modified)  text_result(-array) `→`  (handle)

Text result to be cleared.

## Result

`clear_text_result` returns the value 2 (
H_MSG_TRUE)
.

## Module

Foundation
