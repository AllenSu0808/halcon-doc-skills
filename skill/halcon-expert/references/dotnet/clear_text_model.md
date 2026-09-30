# ClearTextModel (Operator)

## Name

`ClearTextModel` — Clear a text model.

## Signature

`static void HOperatorSet.ClearTextModel(HTuple textModel)`

`static void HTextModel.ClearTextModel(HTextModel[] textModel)`

`void HTextModel.ClearTextModel()`

## Description

`ClearTextModel` clears the text model in *`textModel`* and
frees all underlying memory.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- textModel

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`textModel`** (input_control, state is modified)  text_model(-array) `→` [HTextModel](HTextModel.md), [HTuple](HTuple.md) (*IntPtr*)

Text model to be cleared.

## Result

`ClearTextModel` returns the value 2 (
H_MSG_TRUE)
.

## See also

`CreateTextModelReader`

## Module

OCR/OCV
