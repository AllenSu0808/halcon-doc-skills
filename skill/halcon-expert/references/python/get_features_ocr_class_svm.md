# get_features_ocr_class_svm (Operator)

## Name

`get_features_ocr_class_svm` — Compute the features of a character.

## Signature

`def get_features_ocr_class_svm(character: HObject, ocrhandle: HHandle, transform: str) -> Sequence[float]`

## Description

`get_features_ocr_class_svm` computes the features of the
character given by *`character`* with the OCR classifier
*`ocrhandle`* and returns them in *`features`*. In
contrast to [`do_ocr_single_class_svm`](do_ocr_single_class_svm.md) and
[`do_ocr_multi_class_svm`](do_ocr_multi_class_svm.md), the character is passed as a single
image object. Hence, before calling
`get_features_ocr_class_svm`, [`reduce_domain`](reduce_domain.md) must
typically be called. The parameter *`transform`* determines
whether the feature transformation specified with
`preprocessing` in [`create_ocr_class_svm`](create_ocr_class_svm.md) for the
classifier should be applied (*`transform`* =
*"true"*) or whether the untransformed features should be
returned (*`transform`* = *"false"*).
`get_features_ocr_class_svm` can be used to inspect the
features that are used for the classification.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`character`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Input character.

**`ocrhandle`** (input_control)  ocr_svm `→` HHandle

Handle of the OCR classifier.

**`transform`** (input_control)  string `→` str

Should the feature vector be transformed with
the preprocessing?

Default:
"true"

List of values:
"false", "true"

**`features`** (output_control)  real-array `→` Sequence[float]

Feature vector of the character.

## Result

If the parameters are valid the operator
`get_features_ocr_class_svm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`trainf_ocr_class_svm`

## See also

`create_ocr_class_svm`

## Module

OCR/OCV
