# create_class_lut_svm (Operator)

## Name

`create_class_lut_svm` — Create a look-up table using a Support-Vector-Machine to classify byte
images.

## Signature

`def create_class_lut_svm(svmhandle: HHandle, gen_param_name: Sequence[str], gen_param_value: Sequence[Union[str, int]]) -> HHandle`

## Description

`create_class_lut_svm` generates a look-up table (LUT)
*`class_luthandle`* using the data of a trained Support-Vector-Machine
(SVM) *`svmhandle`* to classify multi-channel byte images. By using
this SVM-based LUT classifier the operator [`classify_image_class_svm`](classify_image_class_svm.md)
of the subsequent classification can be replaced by the operator
[`classify_image_class_lut`](classify_image_class_lut.md). The classification gets a major speed-up,
because the estimation of the class in every image point is no longer
necessary since every possible response of the SVM is stored in the LUT.
For the generation of the LUT, the parameters `num_features`,
`preprocessing`, and `num_components` defined in the earlier
called operator [`create_class_svm`](create_class_svm.md) are important.
In `num_features`, the number of image channels the images must have
to be classified is defined. By using the `preprocessing`
(see [`create_class_svm`](create_class_svm.md)) the number of image channels can be
transformed to `num_components`. `num_components` defines
the length of the feature vector, which the classifier
[`classify_class_svm`](classify_class_svm.md) handles internally. Because of performance and
disk space, the LUT is restricted to be maximal *3*-dimensional. Since
it replaces the operator [`classify_class_svm`](classify_class_svm.md),
`num_components` <= *3* must hold.
If there is no preprocessing that reduces the number of image channels
(`num_features` = `num_components`), all possible pixel values,
which can occur in a byte image, are classified with
[`classify_class_svm`](classify_class_svm.md). The returned classes are stored in the LUT.
If there is a preprocessing that reduces the number of image channels
(`num_features` > `num_components`), the preprocessing
parameters of the SVM are stored in a separate structure of the LUT. To
create the LUT, all transformed pixel values are classified with
[`classify_class_svm`](classify_class_svm.md).
The returned classes are stored in the LUT. Because of the discretization
of the LUT, the accuracy of the LUT classifier could become lower than the
accuracy of [`classify_image_class_svm`](classify_image_class_svm.md).
With *"bit_depth"* and *"class_selection"* the accuracy of
the classification, the required storage, and the runtime needed to create
the LUT can be controlled.

The following parameters of the SVM-based LUT classifier can be set with
*`gen_param_name`* and *`gen_param_value`*:

- ***"bit_depth"*:** —

  Number of bits used from the pixels. It controls the storage requirement
  of the LUT classifier and is bounded by the bit depth of the image
  (*"bit_depth"* <= *8*). If the bit depth of the
  LUT is smaller (*"bit_depth"* < *8*), the classes
  of multiple pixel combinations will be mapped to the same LUT entry,
  which can result in a lower accuracy for the classification. One of these
  clusters contains
  $2^{N}umComponents\cdot(8-\text{bit}_{depth})$ ![figure](../assets/71e2a1843aac7e4b.svg) pixel combinations,
  where `num_components` denotes the dimension of the LUT, which is
  specified in [`create_class_svm`](create_class_svm.md). For example,
  for *"bit_depth"* = *7*,
  `num_components` = *3*, the classes of 8 pixel
  combinations are mapped in the same LUT entry. The LUT requires at most
  $2^{N}NumComponents\cdot bit\_depth+2$ ![figure](../assets/8cd5090353586584.svg) bytes of storage.
  For example, for `num_components` = *3*,
  *"bit_depth"* = *8* and `num_classes` < *16*
  (specified in [`create_class_svm`](create_class_svm.md)), the LUT requires 8 MB of storage
  with internal storage optimization. If `num_classes` = *1*,
  the LUT requires only 2 MB of storage by using the full bit depth of the
  LUT. The runtime for the classification in [`classify_image_class_lut`](classify_image_class_lut.md)
  becomes minimal if the LUT fits into the cache.

  Suggested values:
   *6*,*7*,*8*

  Default:
   *8*

  Restriction:
   *"bit_depth"* >= *1*,
  *"bit_depth"* <= *8*.
- ***"class_selection"*:** —

  Method for the class selection for the LUT. Can be modified to control
  the accuracy and the runtime needed to create the LUT classifier.
  The value in *"class_selection"* is ignored if the bit depth of
  the LUT is maximal, thus *"bit_depth"* = *8* holds.
  If the bit depth of the LUT is smaller
  (*"bit_depth"* < *8*), the classes of multiple pixel
  combinations will be mapped to the same LUT entry. One of these clusters
  contains
  $2^{N}umComponents\cdot(8-\text{bit}_{depth})$ ![figure](../assets/71e2a1843aac7e4b.svg) pixel combinations,
  where `num_components` denotes the dimension of the LUT, which is
  specified in [`create_class_svm`](create_class_svm.md). By choosing
  *"class_selection"* = *"best"*, the class that
  appears most often in the cluster is stored in the LUT.
  For *"class_selection"* = *"fast"*, only one pixel of the
  cluster, i.e., the pixel with the smallest value (component-wise), is
  classified. The returned class is stored in the LUT. In this case, the
  accuracy of the subsequent classification could become lower. On the other
  hand, the runtime needed to create the LUT can be reduced, which is
  proportional to the maximal needed storage of the LUT, which is defined
  with
  $2^{N}NumComponents\cdot bit\_depth+2$ ![figure](../assets/8cd5090353586584.svg).

  List of values:
   *"fast"*, *"best"*

  Default:
   *"fast"*

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`svmhandle`** (input_control)  class_svm `→` HHandle

SVM handle.

**`gen_param_name`** (input_control)  attribute.name-array `→` Sequence[str]

Names of the generic parameters that can be adjusted
for the LUT classifier creation.

Default:
[]

Suggested values:
"bit_depth", "class_selection"

**`gen_param_value`** (input_control)  attribute.value-array `→` Sequence[Union[str, int]]

Values of the generic parameters that can be adjusted
for the LUT classifier creation.

Default:
[]

Suggested values:
8, 7, 6, "fast", "best"

**`class_luthandle`** (output_control)  class_lut `→` HHandle

Handle of the LUT classifier.

## Result

If the parameters are valid, the operator `create_class_lut_svm`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`train_class_svm`,
`read_class_svm`

## Possible Successors

`classify_image_class_lut`

## Alternatives

`create_class_lut_gmm`,
`create_class_lut_knn`,
`create_class_lut_mlp`

## See also

`classify_image_class_lut`,
`clear_class_lut`

## Module

Foundation
