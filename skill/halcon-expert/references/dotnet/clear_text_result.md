# ClearTextResult (Operator)

## Name

`ClearTextResult` — Clear a text result.

## Signature

`static void HOperatorSet.ClearTextResult(HTuple textResultID)`

`static void HTextResult.ClearTextResult(HTextResult[] textResultID)`

`void HTextResult.ClearTextResult()`

## Description

`ClearTextResult` clears the text result in *`textResultID`*
and frees all underlying memory.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- textResultID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`textResultID`** (input_control, state is modified)  text_result(-array) `→` [HTextResult](HTextResult.md), [HTuple](HTuple.md) (*IntPtr*)

Text result to be cleared.

## Result

`ClearTextResult` returns the value 2 (
H_MSG_TRUE)
.

## Module

Foundation
