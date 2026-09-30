# write_dl_transform_pipeline (Operator)

## Name

`write_dl_transform_pipeline` — Write a deep learning transform pipeline to a file

## Signature

`def write_dl_transform_pipeline(transform_pipeline: HHandle, file_name: str) -> None`

## Description

`write_dl_transform_pipeline` writes the deep learning transform
pipeline *`transform_pipeline`* to the file given by *`file_name`*.

The default HALCON file extension for deep learning transform pipelines is
`'.htp'`.

The transform pipeline can be read with [`read_dl_transform_pipeline`](read_dl_transform_pipeline.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`transform_pipeline`** (input_control)  dl_transform_pipeline `→` HHandle

Transform pipeline handle

**`file_name`** (input_control)  filename.write `→` str

Filename

File extension:
.`htp`

## Module

Foundation
