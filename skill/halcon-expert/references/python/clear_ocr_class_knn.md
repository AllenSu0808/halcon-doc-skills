# clear_ocr_class_knn (Operator)

## Name

`clear_ocr_class_knn` — Clear an OCR classifier.

## Signature

`def clear_ocr_class_knn(ocrhandle: HHandle) -> None`

## Description

`clear_ocr_class_knn` clears the OCR classifier given by
*`ocrhandle`* that was created with
[`create_ocr_class_knn`](create_ocr_class_knn.md) and frees all memory required for the
classifier. After calling `clear_ocr_class_knn`, the
classifier can no longer be used. The handle *`ocrhandle`*
becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- ocrhandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`ocrhandle`** (input_control, state is modified)  ocr_knn `→` HHandle

Handle of the OCR classifier.

## Result

If *`ocrhandle`* is valid, the operator
`clear_ocr_class_knn` returns the value 2 (
H_MSG_TRUE)
. If necessary, an
exception is raised.

## Possible Predecessors

`trainf_ocr_class_knn`,
`read_ocr_class_knn`

## See also

`create_class_knn`

## References

Marius Muja, David G. Lowe: “Fast Approximate Nearest Neighbors with
Automatic Algorithm Configuration”;
International Conference on Computer Vision Theory
and Applications (VISAPP 09); 2009.

## Module

OCR/OCV
