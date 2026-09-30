# CreateTextModel (Operator)

## Name

`CreateTextModel` — Create a text model.

## Warning

**`CreateTextModel` is obsolete and is only provided for reasons
of backward compatibility. New applications should use
[`CreateTextModelReader`](create_text_model_reader.md) instead.**

## Signature

`static void HOperatorSet.CreateTextModel(out HTuple textModel)`

`public HTextModel()`

`void HTextModel.CreateTextModel()`

## Description

`CreateTextModel` creates a new *`textModel`* which
describes the text to be segmented by [`FindText`](find_text.md).
Set and query Parameters of *`textModel`* via
[`SetTextModelParam`](set_text_model_param.md) and [`GetTextModelParam`](get_text_model_param.md).

Calls of `CreateTextModel` are equivalent to (and should be
replaced by) calls of [`CreateTextModelReader`](create_text_model_reader.md) with `mode`
set to *"manual"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`textModel`** (output_control)  text_model `→` [HTextModel](HTextModel.md), [HTuple](HTuple.md) (*IntPtr*)

New text model.

## Result

`CreateTextModel` returns the value 2 (
H_MSG_TRUE)
.

## Module

OCR/OCV
