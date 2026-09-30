# read_ocr_class_knn (Operator)

## Name

`read_ocr_class_knn` — Read an OCR classifier from a file.

## Signature

`def read_ocr_class_knn(file_name: str) -> HHandle`

## Description

`read_ocr_class_knn` reads an OCR classifier that has been
stored with [`write_ocr_class_knn`](write_ocr_class_knn.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`file_name`** (input_control)  filename.read `→` str

File name.

File extension:
.`onc`, .`okc`, .`fnt`

**`ocrhandle`** (output_control)  ocr_knn `→` HHandle

Handle of the OCR classifier.

## Result

If the parameters are valid, the operator `read_ocr_class_knn`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Successors

`classify_class_knn`

## See also

`create_ocr_class_knn`

## References

Marius Muja, David G. Lowe: “Fast Approximate Nearest Neighbors with
Automatic Algorithm Configuration”;
International Conference on Computer Vision Theory
and Applications (VISAPP 09); 2009.

## Module

OCR/OCV
