# read_dl_transform_pipeline (Operator)

## Name

`read_dl_transform_pipeline` — Read a deep learning transform pipeline from a file.

## Signature

`read_dl_transform_pipeline( : : FileName : TransformPipeline)`

## Description

The operator `read_dl_transform_pipeline` reads a deep learning
transform pipeline.
As a result, the handle *`TransformPipeline`* is returned.

The transform pipeline is loaded from the file *`FileName`*.
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

**`FileName`** (input_control)  filename.read `→`  (string)

Filename

File extension:
.`htp`

**`TransformPipeline`** (output_control)  dl_transform_pipeline `→`  (handle)

Transform pipeline handle

## Module

Foundation
