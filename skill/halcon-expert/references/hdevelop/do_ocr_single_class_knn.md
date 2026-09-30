# do_ocr_single_class_knn (Operator)

## Name

`do_ocr_single_class_knn` — Classify a single character with an OCR classifier.

## Signature

`do_ocr_single_class_knn(Character, Image : : OCRHandle, NumClasses, NumNeighbors : Class, Confidence)`

## Description

`do_ocr_single_class_knn` uses the OCR-k-NN classifier
*`OCRHandle`* to determine the best training samples for the
features of the character given by the region *`Character`* and
the gray values *`Image`* and returns their classes in
*`Class`* and the corresponding confidences in *`Confidence`*.
If the first *`NumNeighbors`* training vectors have different classes,
maximally *`NumClasses`* classes are returned sorted by frequency
and weighted distance.
The confidences lie between 0.0 and 1.0. The larger the value, the
more reliable is the classification.
The confidence can be only computed robustly
if *`NumNeighbors`* is large enough.

Because multiple classes may be returned by
`do_ocr_single_class_knn`, *`Character`* may only contain
a single region (a single character). If multiple characters should
be classified in a single call, [`do_ocr_multi_class_knn`](do_ocr_multi_class_knn.md) must
be used. Before calling `do_ocr_single_class_knn`, the classifier must
be trained with [`trainf_ocr_class_knn`](trainf_ocr_class_knn.md) or
[`select_feature_set_trainf_knn`](select_feature_set_trainf_knn.md).
If all *`NumNeighbors`* neighbors are of the same class, only
one class is returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Character`** (input_object)  region `→` object

Character to be recognized.

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2)

Gray values of the character.

**`OCRHandle`** (input_control)  ocr_knn `→`  (handle)

Handle of the k-NN classifier.

**`NumClasses`** (input_control)  integer-array `→`  (integer)

Number of maximal classes to determine.

Default:
1

Suggested values:
1, 2, 3, 4, 5

**`NumNeighbors`** (input_control)  integer-array `→`  (integer)

Number of neighbors to consider.

Default:
1

Suggested values:
1, 2, 3, 4, 5

**`Class`** (output_control)  string(-array) `→`  (string)

Results of classifying the character with the
k-NN.

**`Confidence`** (output_control)  real(-array) `→`  (real)

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
