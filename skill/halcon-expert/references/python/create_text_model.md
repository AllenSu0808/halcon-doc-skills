# create_text_model (Operator)

## Name

`create_text_model` — Create a text model.

## Warning

**`create_text_model` is obsolete and is only provided for reasons
of backward compatibility. New applications should use
[`create_text_model_reader`](create_text_model_reader.md) instead.**

## Signature

`def create_text_model() -> HHandle`

## Description

`create_text_model` creates a new *`text_model`* which
describes the text to be segmented by [`find_text`](find_text.md).
Set and query Parameters of *`text_model`* via
[`set_text_model_param`](set_text_model_param.md) and [`get_text_model_param`](get_text_model_param.md).

Calls of `create_text_model` are equivalent to (and should be
replaced by) calls of [`create_text_model_reader`](create_text_model_reader.md) with `mode`
set to *"manual"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`text_model`** (output_control)  text_model `→` HHandle

New text model.

## Result

`create_text_model` returns the value 2 (
H_MSG_TRUE)
.

## Module

OCR/OCV
