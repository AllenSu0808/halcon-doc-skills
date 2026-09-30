# ReadDlTransformPipeline (Operator)

## Name

`ReadDlTransformPipeline` — Read a deep learning transform pipeline from a file.

## Signature

`static void HOperatorSet.ReadDlTransformPipeline(HTuple fileName, out HTuple transformPipeline)`

`static HDlTransformPipeline HDlTransform.ReadDlTransformPipeline(string fileName)`

`public HDlTransformPipeline(string fileName)`

`void HDlTransformPipeline.ReadDlTransformPipeline(string fileName)`

## Description

The operator `ReadDlTransformPipeline` reads a deep learning
transform pipeline.
As a result, the handle *`transformPipeline`* is returned.

The transform pipeline is loaded from the file *`fileName`*.
This file is thereby searched in the directory `$HALCONROOT/dl/`
as well as in the currently used directory.
The default HALCON file extension for deep learning transform pipeline is
`'.htp'`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

Filename

File extension:
.`htp`

**`transformPipeline`** (output_control)  dl_transform_pipeline `→` [HDlTransformPipeline](HDlTransformPipeline.md), [HTuple](HTuple.md) (*IntPtr*)

Transform pipeline handle

## Module

Foundation
