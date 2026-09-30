# SetRejectionParamsClassMlp (Operator)

## Name

`SetRejectionParamsClassMlp` — Set the parameters of a rejection class.

## Signature

`static void HOperatorSet.SetRejectionParamsClassMlp(HTuple MLPHandle, HTuple genParamName, HTuple genParamValue)`

`void HClassMlp.SetRejectionParamsClassMlp(HTuple genParamName, HTuple genParamValue)`

`void HClassMlp.SetRejectionParamsClassMlp(string genParamName, string genParamValue)`

## Description

`SetRejectionParamsClassMlp` sets the parameters of an
automatically generated rejection class inside of a multilayer
perceptron (MLP) given by *`MLPHandle`*. In some applications,
it is desirable to know whether a feature vector is similar to one
of the training set. If a feature vector lies outside of the
provided training set, it should be classified as a special
rejection class. This means that the feature vector is different to
the confidence area of the classifier. If a rejection class should
be created automatically, an additional class must be specified
while creating the classifier in [`CreateClassMlp`](create_class_mlp.md). Here,
the parameter `numOutput` must be increased by one.

The parameters of the rejection class are selected with
*`genParamName`* and the respective values with
*`genParamValue`*.

- ***"rejection_class_index"*:** —

  By default, the last class
  serves as the rejection class. If another class should be used,
  *`genParamName`* must be set to
  *"rejection_class_index"* and *`genParamValue`* to the
  class index.
- ***"sampling_strategy"*:** —

  Currently, three strategies
  exist to generate samples for the rejection class during the
  training of the MLP. These strategies can be selected by setting
  *`genParamName`* to *"sampling_strategy"* and
  *`genParamValue`* to *"hyperbox_around_all_classes"*,
  *"hyperbox_around_each_class"*, or
  *"hyperbox_ring_around_each_class"*. The sampling strategy
  *"hyperbox_around_all_classes"* takes the bounding box of all
  training samples that have been provided so far. The sampling
  strategy *"hyperbox_around_each_class"* is similar with the
  only difference that the bounding box around each class is taken as
  the area where the rejection samples are generated. The sampling
  strategy *"hyperbox_ring_around_each_class"* generates
  samples only in the enlarged areas around the bounding box of each
  class, thus generating a hyperbox ring around the original samples.
  Please note that with increasing dimensionality the sampling
  strategies *"hyperbox_around_each_class"* and
  *"hyperbox_ring_around_each_class"* provide the same result.
  If no rejection class sampling strategy should be used, which is the
  default, *`genParamValue`* must be set to
  *"no_rejection_class"*.
- ***"hyperbox_tolerance"*:** —

  The factor
  *"hyperbox_tolerance"* describes by what amount the
  bounding box should be enlarged in all dimensions. Then, inside
  this box samples are randomly generated from a uniform distribution.
  The default value is 0.2.
- ***"rejection_sample_factor"*:** —

  The number of rejection
  samples is the number of provided samples multiplied by
  *"rejection_sample_factor"*. If not enough samples are
  generated, the rejection class may not be classified correctly. If
  the rejection class has too many samples, the normal classes are
  classified as rejection class. The default value is 1.0. Note that
  the training time will increase by a factor of $1+f$, where
  $f$ is the value of *"rejection_sample_factor"*.
- ***"random_seed"*:** —

  To ensure reproducible results, a
  random seed can be set with *"random_seed"*. The default
  value is 42.

Because this operator only parametrizes the training of the MLP, the
values are not saved by [`WriteClassMlp`](write_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- MLPHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`MLPHandle`** (input_control, state is modified)  class_mlp `→` [HClassMlp](HClassMlp.md), [HTuple](HTuple.md) (*IntPtr*)

MLP handle.

**`genParamName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters.

Default:
"sampling_strategy"

List of values:
"hyperbox_tolerance", "random_seed", "rejection_class_index", "rejection_sample_factor", "sampling_strategy"

**`genParamValue`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / double / int / long)

Values of the generic parameters.

Default:
"hyperbox_around_all_classes"

List of values:
"hyperbox_around_all_classes", "hyperbox_around_each_class", "hyperbox_ring_around_each_class", "no_rejection_class"

## Result

If the parameters are valid, the operator
`SetRejectionParamsClassMlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`CreateClassMlp`

## Possible Successors

`TrainClassMlp`

## Module

Foundation
