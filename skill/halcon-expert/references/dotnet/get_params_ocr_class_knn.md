# GetParamsOcrClassKnn (Operator)

## Name

`GetParamsOcrClassKnn` — Return the parameters of an OCR classifier.

## Signature

`static void HOperatorSet.GetParamsOcrClassKnn(HTuple OCRHandle, out HTuple widthCharacter, out HTuple heightCharacter, out HTuple interpolation, out HTuple features, out HTuple characters, out HTuple preprocessing, out HTuple numTrees)`

`void HOCRKnn.GetParamsOcrClassKnn(out int widthCharacter, out int heightCharacter, out string interpolation, out HTuple features, out HTuple characters, out string preprocessing, out int numTrees)`

`void HOCRKnn.GetParamsOcrClassKnn(out int widthCharacter, out int heightCharacter, out string interpolation, out string features, out HTuple characters, out string preprocessing, out int numTrees)`

## Description

`GetParamsOcrClassKnn` returns the parameters of an OCR
classifier that were specified when the classifier was created with
[`CreateOcrClassKnn`](create_ocr_class_knn.md). This is particularly useful if the
classifier was read with [`ReadOcrClassKnn`](read_ocr_class_knn.md). The output of
`GetParamsOcrClassKnn` can, for example, be used to check
whether a character to be read is contained in the classifier. For
a description of the parameters, see [`CreateOcrClassKnn`](create_ocr_class_knn.md) and
[`TrainfOcrClassKnn`](trainf_ocr_class_knn.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_knn `→` [HOCRKnn](HOCRKnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

**`widthCharacter`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Width of the rectangle to which the gray values
of the segmented character are zoomed.

**`heightCharacter`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Height of the rectangle to which the gray values
of the segmented character are zoomed.

**`interpolation`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Interpolation mode for the zooming of the characters.

**`features`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Features to be used for classification.

**`characters`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Characters of the character set to be read.

**`preprocessing`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of preprocessing used to transform the
feature vectors.

**`numTrees`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of different trees used during the classification.

## Result

If the parameters are valid, the operator
`GetParamsOcrClassKnn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`CreateOcrClassMlp`,
`ReadOcrClassMlp`

## Possible Successors

`DoOcrSingleClassMlp`,
`DoOcrMultiClassMlp`

## See also

`TrainfOcrClassMlp`,
`GetParamsClassMlp`

## Module

OCR/OCV
