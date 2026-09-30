# GetParamsOcrClassMlp (Operator)

## Name

`GetParamsOcrClassMlp` — Return the parameters of an OCR classifier.

## Signature

`static void HOperatorSet.GetParamsOcrClassMlp(HTuple OCRHandle, out HTuple widthCharacter, out HTuple heightCharacter, out HTuple interpolation, out HTuple features, out HTuple characters, out HTuple numHidden, out HTuple preprocessing, out HTuple numComponents)`

`void HOCRMlp.GetParamsOcrClassMlp(out int widthCharacter, out int heightCharacter, out string interpolation, out HTuple features, out HTuple characters, out int numHidden, out string preprocessing, out int numComponents)`

`void HOCRMlp.GetParamsOcrClassMlp(out int widthCharacter, out int heightCharacter, out string interpolation, out string features, out HTuple characters, out int numHidden, out string preprocessing, out int numComponents)`

## Description

`GetParamsOcrClassMlp` returns the parameters of an OCR
classifier that were specified when the classifier was created with
[`CreateOcrClassMlp`](create_ocr_class_mlp.md). This is particularly useful if the
classifier was read with [`ReadOcrClassMlp`](read_ocr_class_mlp.md). The output of
`GetParamsOcrClassMlp` can, for example, be used to check
whether a character to be read is contained in the classifier. For
a description of the parameters, see [`CreateOcrClassMlp`](create_ocr_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_mlp `→` [HOCRMlp](HOCRMlp.md), [HTuple](HTuple.md) (*IntPtr*)

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

**`numHidden`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of hidden units of the MLP.

**`preprocessing`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of preprocessing used to transform the
feature vectors.

**`numComponents`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Preprocessing parameter: Number of transformed
features.

## Result

If the parameters are valid, the operator
`GetParamsOcrClassMlp` returns the value 2 (
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
