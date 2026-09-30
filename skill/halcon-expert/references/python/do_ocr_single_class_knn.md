# do_ocr_single_class_knn (Operator)

## Name

`do_ocr_single_class_knn` — Classify a single character with an OCR classifier.

## Signature

`def do_ocr_single_class_knn(character: HObject, image: HObject, ocrhandle: HHandle, num_classes: Sequence[int], num_neighbors: Sequence[int]) -> Tuple[Sequence[str], Sequence[float]]`

`def do_ocr_single_class_knn_s(character: HObject, image: HObject, ocrhandle: HHandle, num_classes: Sequence[int], num_neighbors: Sequence[int]) -> Tuple[str, float]`

## Description

`do_ocr_single_class_knn` uses the OCR-k-NN classifier
*`ocrhandle`* to determine the best training samples for the
features of the character given by the region *`character`* and
the gray values *`image`* and returns their classes in
*`class`* and the corresponding confidences in *`confidence`*.
If the first *`num_neighbors`* training vectors have different classes,
maximally *`num_classes`* classes are returned sorted by frequency
and weighted distance.
The confidences lie between 0.0 and 1.0. The larger the value, the
more reliable is the classification.
The confidence can be only computed robustly
if *`num_neighbors`* is large enough.

Because multiple classes may be returned by
`do_ocr_single_class_knn`, *`character`* may only contain
a single region (a single character). If multiple characters should
be classified in a single call, [`do_ocr_multi_class_knn`](do_ocr_multi_class_knn.md) must
be used. Before calling `do_ocr_single_class_knn`, the classifier must
be trained with [`trainf_ocr_class_knn`](trainf_ocr_class_knn.md) or
[`select_feature_set_trainf_knn`](select_feature_set_trainf_knn.md).
If all *`num_neighbors`* neighbors are of the same class, only
one class is returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`character`** (input_object)  region `→` HObject

Character to be recognized.

**`image`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Gray values of the character.

**`ocrhandle`** (input_control)  ocr_knn `→` HHandle

Handle of the k-NN classifier.

**`num_classes`** (input_control)  integer-array `→` Sequence[int]

Number of maximal classes to determine.

Default:
1

Suggested values:
1, 2, 3, 4, 5

**`num_neighbors`** (input_control)  integer-array `→` Sequence[int]

Number of neighbors to consider.

Default:
1

Suggested values:
1, 2, 3, 4, 5

**`class`** (output_control)  string(-array) `→` Sequence[str]

Results of classifying the character with the
k-NN.

**`confidence`** (output_control)  real(-array) `→` Sequence[float]

Confidence(s) of the class(es) of the character.

## Result

If the parameters are valid, the operator
`do_ocr_single_class_knn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`trainf_ocr_class_knn`,
`read_ocr_class_knn`

## Alternatives

`do_ocr_multi_class_knn`

## See also

`create_ocr_class_knn`,
`classify_class_knn`

## Module

OCR/OCV
