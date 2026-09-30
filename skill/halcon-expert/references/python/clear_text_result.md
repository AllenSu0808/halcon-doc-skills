# clear_text_result (Operator)

## Name

`clear_text_result` — Clear a text result.

## Signature

`def clear_text_result(text_result_id: MaybeSequence[HHandle]) -> None`

## Description

`clear_text_result` clears the text result in *`text_result_id`*
and frees all underlying memory.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- text_result_id

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`text_result_id`** (input_control, state is modified)  text_result(-array) `→` MaybeSequence[HHandle]

Text result to be cleared.

## Result

`clear_text_result` returns the value 2 (
H_MSG_TRUE)
.

## Module

Foundation
