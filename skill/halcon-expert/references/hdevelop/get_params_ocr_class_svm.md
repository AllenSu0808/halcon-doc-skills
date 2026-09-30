# get_params_ocr_class_svm (Operator)

## Name

`get_params_ocr_class_svm` — Return the parameters of an OCR classifier.

## Signature

`get_params_ocr_class_svm( : : OCRHandle : WidthCharacter, HeightCharacter, Interpolation, Features, Characters, KernelType, KernelParam, Nu, Mode, Preprocessing, NumComponents)`

## Description

`get_params_ocr_class_svm` returns the parameters of an OCR
classifier that were specified when the classifier was created with
[`create_ocr_class_svm`](create_ocr_class_svm.md). This is particularly useful if the
classifier was read with [`read_ocr_class_svm`](read_ocr_class_svm.md). The output of
`get_params_ocr_class_svm` can, for example, be used to check
whether a character to be read is contained in the classifier. For
a description of the parameters, see [`create_ocr_class_svm`](create_ocr_class_svm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_svm `→`  (handle)

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

**`KernelType`** (output_control)  string `→`  (string)

The kernel type.

**`KernelParam`** (output_control)  real `→`  (real)

Additional parameters for the kernel function.

**`Nu`** (output_control)  real `→`  (real)

Regularization constant of the SVM.

**`Mode`** (output_control)  string `→`  (string)

The mode of the SVM.

**`Preprocessing`** (output_control)  string `→`  (string)

Type of preprocessing used to transform the
feature vectors.

**`NumComponents`** (output_control)  integer `→`  (integer)

Preprocessing parameter: Number of transformed
features (ignored for *`Preprocessing`* =
*'none'* and *`Preprocessing`* =
*'normalization'*).

## Result

If the parameters are valid the operator
`get_params_ocr_class_svm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`create_ocr_class_svm`,
`read_ocr_class_svm`

## Possible Successors

`do_ocr_single_class_svm`,
`do_ocr_multi_class_svm`

## See also

`trainf_ocr_class_svm`,
`get_params_class_svm`

## Module

OCR/OCV
