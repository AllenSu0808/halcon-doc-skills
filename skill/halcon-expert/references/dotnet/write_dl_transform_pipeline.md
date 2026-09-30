# WriteDlTransformPipeline (Operator)

## Name

`WriteDlTransformPipeline` — Write a deep learning transform pipeline to a file

## Signature

`static void HOperatorSet.WriteDlTransformPipeline(HTuple transformPipeline, HTuple fileName)`

`static void HDlTransform.WriteDlTransformPipeline(HDlTransformPipeline transformPipeline, string fileName)`

`void HDlTransformPipeline.WriteDlTransformPipeline(string fileName)`

## Description

`WriteDlTransformPipeline` writes the deep learning transform
pipeline *`transformPipeline`* to the file given by *`fileName`*.

The default HALCON file extension for deep learning transform pipelines is
`'.htp'`.

The transform pipeline can be read with [`ReadDlTransformPipeline`](read_dl_transform_pipeline.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`transformPipeline`** (input_control)  dl_transform_pipeline `→` [HDlTransformPipeline](HDlTransformPipeline.md), [HTuple](HTuple.md) (*IntPtr*)

Transform pipeline handle

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

Filename

File extension:
.`htp`

## Module

Foundation
