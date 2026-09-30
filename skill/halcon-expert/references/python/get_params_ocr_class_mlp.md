# get_params_ocr_class_mlp (Operator)

## Name

`get_params_ocr_class_mlp` — Return the parameters of an OCR classifier.

## Signature

`def get_params_ocr_class_mlp(ocrhandle: HHandle) -> Tuple[int, int, str, Sequence[str], Sequence[str], int, str, int]`

`def get_params_ocr_class_mlp_s(ocrhandle: HHandle) -> Tuple[int, int, str, str, Sequence[str], int, str, int]`

## Description

`get_params_ocr_class_mlp` returns the parameters of an OCR
classifier that were specified when the classifier was created with
[`create_ocr_class_mlp`](create_ocr_class_mlp.md). This is particularly useful if the
classifier was read with [`read_ocr_class_mlp`](read_ocr_class_mlp.md). The output of
`get_params_ocr_class_mlp` can, for example, be used to check
whether a character to be read is contained in the classifier. For
a description of the parameters, see [`create_ocr_class_mlp`](create_ocr_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ocrhandle`** (input_control)  ocr_mlp `→` HHandle

Handle of the OCR classifier.

**`width_character`** (output_control)  integer `→` int

Width of the rectangle to which the gray values
of the segmented character are zoomed.

**`height_character`** (output_control)  integer `→` int

Height of the rectangle to which the gray values
of the segmented character are zoomed.

**`interpolation`** (output_control)  string `→` str

Interpolation mode for the zooming of the characters.

**`features`** (output_control)  string(-array) `→` Sequence[str]

Features to be used for classification.

**`characters`** (output_control)  string-array `→` Sequence[str]

Characters of the character set to be read.

**`num_hidden`** (output_control)  integer `→` int

Number of hidden units of the MLP.

**`preprocessing`** (output_control)  string `→` str

Type of preprocessing used to transform the
feature vectors.

**`num_components`** (output_control)  integer `→` int

Preprocessing parameter: Number of transformed
features.

## Result

If the parameters are valid, the operator
`get_params_ocr_class_mlp` returns the value 2 (
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
