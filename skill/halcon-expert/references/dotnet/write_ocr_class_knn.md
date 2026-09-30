# WriteOcrClassKnn (Operator)

## Name

`WriteOcrClassKnn` — Write a k-NN classifier for an OCR task to a file.

## Signature

`static void HOperatorSet.WriteOcrClassKnn(HTuple OCRHandle, HTuple fileName)`

`void HOCRKnn.WriteOcrClassKnn(string fileName)`

## Description

`WriteOcrClassKnn` writes the k-NN classifier for an OCR task with
the *`OCRHandle`* to the file given by *`fileName`*. If a
file extension is not specified in *`fileName`* the default
extension `'.onc'` is appended to *`fileName`*.
`WriteOcrClassKnn` is typically called after the classifier
has been trained with [`TrainfOcrClassKnn`](trainf_ocr_class_knn.md). The classifier
can be read with [`ReadOcrClassKnn`](read_ocr_class_knn.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_knn `→` [HOCRKnn](HOCRKnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the k-NN classifier for an OCR task.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`onc`

## Result

If the parameters are valid, the operator
`WriteOcrClassKnn` returns the value 2 (
H_MSG_TRUE)
. If necessary, an
exception is raised.

## Possible Predecessors

`TrainfOcrClassKnn`,
`ReadOcrClassKnn`

## See also

`CreateClassKnn`,
`ReadOcrClassKnn`

## References

Marius Muja, David G. Lowe: “Fast Approximate Nearest Neighbors with
Automatic Algorithm Configuration”;
International Conference on Computer Vision Theory
and Applications (VISAPP 09); 2009.

## Module

OCR/OCV
