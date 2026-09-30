# get_params_ocr_class_knn (Operator)

## Name

`get_params_ocr_class_knn` — Return the parameters of an OCR classifier.

## Signature

`get_params_ocr_class_knn( : : OCRHandle : WidthCharacter, HeightCharacter, Interpolation, Features, Characters, Preprocessing, NumTrees)`

## Description

`get_params_ocr_class_knn` returns the parameters of an OCR
classifier that were specified when the classifier was created with
[`create_ocr_class_knn`](create_ocr_class_knn.md). This is particularly useful if the
classifier was read with [`read_ocr_class_knn`](read_ocr_class_knn.md). The output of
`get_params_ocr_class_knn` can, for example, be used to check
whether a character to be read is contained in the classifier. For
a description of the parameters, see [`create_ocr_class_knn`](create_ocr_class_knn.md) and
[`trainf_ocr_class_knn`](trainf_ocr_class_knn.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_knn `→`  (handle)

Handle of the OCR classifier.

**`WidthCharacter`** (output_control)  integer `→`  (integer)

Width of the rectangle to which the gray values
of the segmented character are zoomed.

**`HeightCharacter`** (output_control)  integer `→`  (integer)

Height of the rectangle to which the gray values
of the segmented character are zoomed.

**`Interpolation`** (output_control)  string `→`  (string)

Interpolation mode for the zooming of the characters.

**`Features`** (output_control)  string(-array) `→`  (string)

Features to be used for classification.

**`Characters`** (output_control)  string-array `→`  (string)

Characters of the character set to be read.

**`Preprocessing`** (output_control)  string `→`  (string)

Type of preprocessing used to transform the
feature vectors.

**`NumTrees`** (output_control)  integer `→`  (integer)

Number of different trees used during the classification.

## Result

If the parameters are valid, the operator
`get_params_ocr_class_knn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`create_ocr_class_mlp`,
`read_ocr_class_mlp`

## Possible Successors

`do_ocr_single_class_mlp`,
`do_ocr_multi_class_mlp`

## See also

`trainf_ocr_class_mlp`,
`get_params_class_mlp`

## Module

OCR/OCV
