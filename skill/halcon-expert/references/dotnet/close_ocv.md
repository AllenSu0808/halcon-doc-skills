# CloseOcv (Operator)

## Name

`CloseOcv` — Clear an OCV tool.

## Signature

`static void HOperatorSet.CloseOcv(HTuple OCVHandle)`

`void HOCV.CloseOcv()`

## Description

`CloseOcv` closes an open OCV tool and frees the memory.
The OCV tool has been created using [`CreateOcvProj`](create_ocv_proj.md) or
[`ReadOcv`](read_ocv.md). The handle is after this call no longer valid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- OCVHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`OCVHandle`** (input_control, state is modified)  ocv `→` [HOCV](HOCV.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCV tool which has to be freed.

## Example (C++)

```
read_ocv("ocv_file",&ocv_handle);
for (i=0; i<1000; i++)
{
  grab_image_async(&Image,fg_handle,-1);
  reduce_domain(Image,ROI,&Pattern);
  do_ocv_simple(Pattern,ocv_handle,"A",
                "true","true","false","true",10,
                &Quality);
}
close_ocv(ocv_handle);
```

## Result

`CloseOcv` returns 2 (
H_MSG_TRUE)
, if the handle is valid.
Otherwise, an exception is raised.

## Possible Predecessors

`ReadOcv`,
`CreateOcvProj`

## See also

`CloseOcr`

## Module

OCR/OCV
