# GetParamsOcrClassSvm (Operator)

## Name

`GetParamsOcrClassSvm` — Return the parameters of an OCR classifier.

## Signature

`static void HOperatorSet.GetParamsOcrClassSvm(HTuple OCRHandle, out HTuple widthCharacter, out HTuple heightCharacter, out HTuple interpolation, out HTuple features, out HTuple characters, out HTuple kernelType, out HTuple kernelParam, out HTuple nu, out HTuple mode, out HTuple preprocessing, out HTuple numComponents)`

`void HOCRSvm.GetParamsOcrClassSvm(out int widthCharacter, out int heightCharacter, out string interpolation, out HTuple features, out HTuple characters, out string kernelType, out double kernelParam, out double nu, out string mode, out string preprocessing, out int numComponents)`

`void HOCRSvm.GetParamsOcrClassSvm(out int widthCharacter, out int heightCharacter, out string interpolation, out string features, out HTuple characters, out string kernelType, out double kernelParam, out double nu, out string mode, out string preprocessing, out int numComponents)`

## Description

`GetParamsOcrClassSvm` returns the parameters of an OCR
classifier that were specified when the classifier was created with
[`CreateOcrClassSvm`](create_ocr_class_svm.md). This is particularly useful if the
classifier was read with [`ReadOcrClassSvm`](read_ocr_class_svm.md). The output of
`GetParamsOcrClassSvm` can, for example, be used to check
whether a character to be read is contained in the classifier. For
a description of the parameters, see [`CreateOcrClassSvm`](create_ocr_class_svm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_svm `→` [HOCRSvm](HOCRSvm.md), [HTuple](HTuple.md) (*IntPtr*)

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

**`kernelType`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

The kernel type.

**`kernelParam`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Additional parameters for the kernel function.

**`nu`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Regularization constant of the SVM.

**`mode`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

The mode of the SVM.

**`preprocessing`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of preprocessing used to transform the
feature vectors.

**`numComponents`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Preprocessing parameter: Number of transformed
features (ignored for *`preprocessing`* =
*"none"* and *`preprocessing`* =
*"normalization"*).

## Result

If the parameters are valid the operator
`GetParamsOcrClassSvm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`CreateOcrClassSvm`,
`ReadOcrClassSvm`

## Possible Successors

`DoOcrSingleClassSvm`,
`DoOcrMultiClassSvm`

## See also

`TrainfOcrClassSvm`,
`GetParamsClassSvm`

## Module

OCR/OCV
