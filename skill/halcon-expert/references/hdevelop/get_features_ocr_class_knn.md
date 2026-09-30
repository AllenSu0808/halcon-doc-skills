# get_features_ocr_class_knn (Operator)

## Name

`get_features_ocr_class_knn` — Compute the features of a character.

## Signature

`get_features_ocr_class_knn(Character : : OCRHandle, Transform : Features)`

## Description

`get_features_ocr_class_knn` computes the features of the
character given by *`Character`* with the k-NN classifier
*`OCRHandle`* and returns them in *`Features`*. In
contrast to [`do_ocr_single_class_knn`](do_ocr_single_class_knn.md) and
[`do_ocr_multi_class_knn`](do_ocr_multi_class_knn.md), the character is passed as a single
image object. Hence, before calling
`get_features_ocr_class_knn`, [`reduce_domain`](reduce_domain.md) must
typically be called. The parameter *`Transform`* determines
whether the feature transformation specified with
`Preprocessing` in [`create_ocr_class_knn`](create_ocr_class_knn.md) for the
classifier should be applied (*`Transform`* =
*'true'*) or whether the untransformed features should be
returned (*`Transform`* = *'false'*).
`get_features_ocr_class_knn` can be used to inspect the
features that are used for the classification.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Character`** (input_object)  singlechannelimage `→` object (byte / uint2)

Input character.

**`OCRHandle`** (input_control)  ocr_knn `→`  (handle)

Handle of the k-NN classifier.

**`Transform`** (input_control)  string `→`  (string)

Should the feature vector be transformed with
the preprocessing?

Default:
'true'

List of values:
'false', 'true'

**`Features`** (output_control)  real-array `→`  (real)

Feature vector of the character.

## Result

If the parameters are valid, the operator
`get_features_ocr_class_knn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`trainf_ocr_class_knn`

## See also

`create_ocr_class_knn`

## Module

OCR/OCV
