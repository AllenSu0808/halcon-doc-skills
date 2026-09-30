# read_ocv (Operator)

## Name

`read_ocv` — Reading an OCV tool from file.

## Signature

`read_ocv( : : FileName : OCVHandle)`

## Description

`read_ocv` reads an OCV tool from file.
The tool will contain the same information that it contained when saving
it with [`write_ocv`](write_ocv.md). After reading the tool the training
can be completed for those patterns which have not been trained
so far. Otherwise a pattern comparison can be
applied directly by calling [`do_ocv_simple`](do_ocv_simple.md).

As extension '.ocv' is used. If this extension is not given with
the file name it will be added automatically.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`FileName`** (input_control)  filename.read `→`  (string)

Name of the file which has to be read.

Default:
'test_ocv'

File extension:
.`ocv`

**`OCVHandle`** (output_control)  ocv `→`  (handle)

Handle of read OCV tool.

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

`read_ocv` returns 2 (
H_MSG_TRUE)
, if the file is correct. Otherwise, an
exception is raised.

## Possible Predecessors

`write_ocv`

## Possible Successors

`do_ocv_simple`,
`close_ocv`

## See also

`read_ocr`

## Module

OCR/OCV
