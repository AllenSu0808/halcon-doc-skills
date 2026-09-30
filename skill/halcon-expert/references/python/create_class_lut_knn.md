# create_class_lut_knn (Operator)

## Name

`create_class_lut_knn` — Create a look-up table using a k-nearest neighbors
classifier (k-NN) to classify byte
images.

## Signature

`def create_class_lut_knn(knnhandle: HHandle, gen_param_name: Sequence[str], gen_param_value: Sequence[Union[str, int, float]]) -> HHandle`

## Description

`create_class_lut_knn` generates a look-up table (LUT)
*`class_luthandle`* using the data of a trained k-nearest neighbors
classifier (k-NN) *`knnhandle`* to classify multi-channel byte images.
By using this k-NN-based LUT classifier, the operator
[`classify_image_class_knn`](classify_image_class_knn.md) of the subsequent classification can be
replaced by the operator [`classify_image_class_lut`](classify_image_class_lut.md). The
classification is speed up considerably, because the estimation
of the class in every image point is no longer
necessary since every possible response of the k-NN is stored in the LUT.
For the generation of the LUT, the parameter `num_dim` of
called operator [`create_class_knn`](create_class_knn.md) is important.
The number of image channels the images must have to be
classified is defined in `num_dim`.

To create the LUT,
all pixel values are classified with [`classify_class_knn`](classify_class_knn.md).
The returned classes are stored in the LUT. Because of the discretization
of the LUT, the accuracy of the LUT classifier could become lower than the
accuracy of [`classify_image_class_knn`](classify_image_class_knn.md).

With *"bit_depth"* the accuracy of the classification, the
required storage, and the runtime needed to create
the LUT can be controlled.

The following parameters of the k-NN-based LUT classifier can be set with
*`gen_param_name`* and *`gen_param_value`*:

- ***"bit_depth"*:** —

  Number of bits used from the pixels. It controls the storage requirement
  of the LUT classifier and is bounded by the bit depth of the image
  (*"bit_depth"* <= *8*). If the bit depth of the
  LUT is smaller (*"bit_depth"* < *8*), the classes
  of multiple pixel combinations will be mapped to the same LUT entry,
  which can result in a lower accuracy for the classification. One of these
  clusters contains
  $$2^{N}umDim\cdot(8-\text{bit_depth})$$ ![figure](../assets/2b8b81fee3f7b73d.svg) pixel combinations,
  where `num_dim` denotes the dimension of the LUT, which is
  specified in [`create_class_knn`](create_class_knn.md). For example,
  for *"bit_depth"* = *7*,
  `num_dim` = *3*, the classes of 8 pixel
  combinations are mapped in the same LUT entry. The LUT requires at most
  $$2^{NumDim\cdot bit\_depth+2$$ ![figure](../assets/eecbb3f47df83d8f.svg) bytes of storage.
  For example, for `num_dim` = *3*,
  *"bit_depth"* = *8* and number of classes is smaller than
  *16*, the LUT requires 8 MB of storage
  with internal storage optimization.
  The runtime for the classification in [`classify_image_class_lut`](classify_image_class_lut.md)
  becomes minimal if the LUT fits into the cache.

  Suggested values:
   *6*,*7*,*8*

  Default:
   *8*

  Restriction:
   *"bit_depth"* >= *1*,
  *"bit_depth"* <= *8*.
- ***"rejection_threshold"*:** —

  Threshold for the rejection of uncertain classified points of the k-NN.
  The parameter represents a threshold on the distance
  returned by the classification (see [`classify_class_knn`](classify_class_knn.md)).
  All pixels having a distance over
  *"rejection_threshold"* are not assigned to any class.

  Default:
   *5*

  Restriction:
   *"rejection_threshold"* >= *0*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`knnhandle`** (input_control)  class_knn `→` HHandle

Handle of the k-NN classifier.

**`gen_param_name`** (input_control)  attribute.name-array `→` Sequence[str]

Names of the generic parameters that can be adjusted
for the LUT classifier creation.

Default:
[]

Suggested values:
"bit_depth", "rejection_threshold"

**`gen_param_value`** (input_control)  attribute.value-array `→` Sequence[Union[str, int, float]]

Values of the generic parameters that can be adjusted
for the LUT classifier creation.

Default:
[]

Suggested values:
8, 7, 6, 0.5, 5, 10, 50

**`class_luthandle`** (output_control)  class_lut `→` HHandle

Handle of the LUT classifier.

## Result

If the parameters are valid, the operator `create_class_lut_knn`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`train_class_knn`,
`read_class_knn`

## Possible Successors

`classify_image_class_lut`

## Alternatives

`create_class_lut_svm`,
`create_class_lut_gmm`,
`create_class_lut_mlp`

## See also

`classify_image_class_lut`,
`clear_class_lut`

## Module

Foundation
