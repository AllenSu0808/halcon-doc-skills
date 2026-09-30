# write_ocr_class_knn (Operator)

## Name

`write_ocr_class_knn` — Write a k-NN classifier for an OCR task to a file.

## Signature

`write_ocr_class_knn( : : OCRHandle, FileName : )`

## Description

`write_ocr_class_knn` writes the k-NN classifier for an OCR task with
the *`OCRHandle`* to the file given by *`FileName`*. If a
file extension is not specified in *`FileName`* the default
extension `'.onc'` is appended to *`FileName`*.
`write_ocr_class_knn` is typically called after the classifier
has been trained with [`trainf_ocr_class_knn`](trainf_ocr_class_knn.md). The classifier
can be read with [`read_ocr_class_knn`](read_ocr_class_knn.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_knn `→`  (handle)

Handle of the k-NN classifier for an OCR task.

**`FileName`** (input_control)  filename.write `→`  (string)

File name.

File extension:
.`onc`

## Result

If the parameters are valid, the operator
`write_ocr_class_knn` returns the value 2 (
H_MSG_TRUE)
. If necessary, an
exception is raised.

## Possible Predecessors

`trainf_ocr_class_knn`,
`read_ocr_class_knn`

## See also

`create_class_knn`,
`read_ocr_class_knn`

## References

Marius Muja, David G. Lowe: “Fast Approximate Nearest Neighbors with
Automatic Algorithm Configuration”;
International Conference on Computer Vision Theory
and Applications (VISAPP 09); 2009.

## Module

OCR/OCV
