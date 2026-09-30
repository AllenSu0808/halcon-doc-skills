# write_dl_transform_pipeline (Operator)

## Name

`write_dl_transform_pipeline` — Write a deep learning transform pipeline to a file

## Signature

`write_dl_transform_pipeline( : : TransformPipeline, FileName : )`

## Description

`write_dl_transform_pipeline` writes the deep learning transform
pipeline *`TransformPipeline`* to the file given by *`FileName`*.

The default HALCON file extension for deep learning transform pipelines is
`'.htp'`.

The transform pipeline can be read with [`read_dl_transform_pipeline`](read_dl_transform_pipeline.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`TransformPipeline`** (input_control)  dl_transform_pipeline `→`  (handle)

Transform pipeline handle

**`FileName`** (input_control)  filename.write `→`  (string)

Filename

File extension:
.`htp`

## Module

Foundation
