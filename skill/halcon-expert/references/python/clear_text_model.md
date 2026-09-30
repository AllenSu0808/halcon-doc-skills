# clear_text_model (Operator)

## Name

`clear_text_model` — Clear a text model.

## Signature

`def clear_text_model(text_model: MaybeSequence[HHandle]) -> None`

## Description

`clear_text_model` clears the text model in *`text_model`* and
frees all underlying memory.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- text_model

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`text_model`** (input_control, state is modified)  text_model(-array) `→` MaybeSequence[HHandle]

Text model to be cleared.

## Result

`clear_text_model` returns the value 2 (
H_MSG_TRUE)
.

## See also

`create_text_model_reader`

## Module

OCR/OCV
