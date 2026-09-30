# ReadOcrClassKnn (Operator)

## Name

`ReadOcrClassKnn` — Read an OCR classifier from a file.

## Signature

`static void HOperatorSet.ReadOcrClassKnn(HTuple fileName, out HTuple OCRHandle)`

`public HOCRKnn(string fileName)`

`void HOCRKnn.ReadOcrClassKnn(string fileName)`

## Description

`ReadOcrClassKnn` reads an OCR classifier that has been
stored with [`WriteOcrClassKnn`](write_ocr_class_knn.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`onc`, .`okc`, .`fnt`

**`OCRHandle`** (output_control)  ocr_knn `→` [HOCRKnn](HOCRKnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

## Result

If the parameters are valid, the operator `ReadOcrClassKnn`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Successors

`ClassifyClassKnn`

## See also

`CreateOcrClassKnn`

## References

Marius Muja, David G. Lowe: “Fast Approximate Nearest Neighbors with
Automatic Algorithm Configuration”;
International Conference on Computer Vision Theory
and Applications (VISAPP 09); 2009.

## Module

OCR/OCV
