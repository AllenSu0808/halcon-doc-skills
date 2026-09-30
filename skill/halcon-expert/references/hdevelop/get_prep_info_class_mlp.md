# get_prep_info_class_mlp (Operator)

## Name

`get_prep_info_class_mlp` — Compute the information content of the preprocessed feature vectors
of a multilayer perceptron.

## Signature

`get_prep_info_class_mlp( : : MLPHandle, Preprocessing : InformationCont, CumInformationCont)`

## Description

`get_prep_info_class_mlp` computes the information content of
the training vectors that have been transformed with the
preprocessing given by *`Preprocessing`*.
*`Preprocessing`* can be set to *'principal_components'*
or *'canonical_variates'*. The preprocessing methods are
described with [`create_class_mlp`](create_class_mlp.md). The information content is
derived from the variations of the transformed components of the
feature vector, i.e., it is computed solely based on the training
data, independent of any error rate on the training data. The
information content is computed for all relevant components of the
transformed feature vectors (`NumInput` for
*'principal_components'* and min(`NumOutput` - 1,
`NumInput`) for *'canonical_variates'*, see
[`create_class_mlp`](create_class_mlp.md)), and is returned in
*`InformationCont`* as a number between 0 and 1. To convert
the information content into a percentage, it simply needs to be
multiplied by 100. The cumulative information content of the first
n components is returned in the n-th component of
*`CumInformationCont`*, i.e., *`CumInformationCont`*
contains the sums of the first n elements of
*`InformationCont`*. To use `get_prep_info_class_mlp`, a
sufficient number of samples must be added to the multilayer
perceptron (MLP) given by *`MLPHandle`* by using
[`add_sample_class_mlp`](add_sample_class_mlp.md) or [`read_samples_class_mlp`](read_samples_class_mlp.md).

*`InformationCont`* and *`CumInformationCont`* can be used
to decide how many components of the transformed feature vectors
contain relevant information. An often used criterion is to require
that the transformed data must represent x% (e.g., 90%) of the
data. This can be decided easily from the first value of
*`CumInformationCont`* that lies above x%. The number thus
obtained can be used as the value for `NumComponents` in a
new call to [`create_class_mlp`](create_class_mlp.md). The call to
`get_prep_info_class_mlp` already requires the creation of an
MLP, and hence the setting of `NumComponents` in
[`create_class_mlp`](create_class_mlp.md) to an initial value. However, if
`get_prep_info_class_mlp` is called it is typically not known
how many components are relevant, and hence how to set
`NumComponents` in this call. Therefore, the following
two-step approach should typically be used to select
`NumComponents`: In a first step, an MLP with the maximum
number for `NumComponents` is created (`NumInput` for
*'principal_components'* and
min(`NumOutput` - 1, `NumInput`)
for *'canonical_variates'*). Then, the
training samples are added to the MLP and are saved in a file using
[`write_samples_class_mlp`](write_samples_class_mlp.md). Subsequently,
`get_prep_info_class_mlp` is used to determine the information
content of the components, and with this `NumComponents`.
After this, a new MLP with the desired number of components is
created, and the training samples are read with
[`read_samples_class_mlp`](read_samples_class_mlp.md). Finally, the MLP is trained with
[`train_class_mlp`](train_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MLPHandle`** (input_control)  class_mlp `→`  (handle)

MLP handle.

**`Preprocessing`** (input_control)  string `→`  (string)

Type of preprocessing used to transform the
feature vectors.

Default:
'principal_components'

List of values:
'canonical_variates', 'principal_components'

**`InformationCont`** (output_control)  real-array `→`  (real)

Relative information content of the transformed
feature vectors.

**`CumInformationCont`** (output_control)  real-array `→`  (real)

Cumulative information content of the transformed
feature vectors.

## Example (HDevelop)

```
* Create the initial MLP
create_class_mlp (NumIn, NumHidden, NumOut, 'softmax', \
                  'principal_components', NumIn, 42, MLPHandle)
* Generate and add the training data
for J := 0 to NumData-1 by 1
    * Generate training features and classes
    * Data = [...]
    * Class = [...]
    add_sample_class_mlp (MLPHandle, Data, Class)
endfor
write_samples_class_mlp (MLPHandle, 'samples.mtf')
* Compute the information content of the transformed features
get_prep_info_class_mlp (MLPHandle, 'principal_components',\
                         InformationCont, CumInformationCont)
* Determine NumComp by inspecting InformationCont and CumInformationCont
* NumComp = [...]
* Create the actual MLP
create_class_mlp (NumIn, NumHidden, NumOut, 'softmax', \
                  'principal_components', NumComp, 42, MLPHandle)
* Train the MLP
read_samples_class_mlp (MLPHandle, 'samples.mtf')
train_class_mlp (MLPHandle, 100, 1, 0.01, Error, ErrorLog)
write_class_mlp (MLPHandle, 'classifier.mlp')
```

## Result

If the parameters are valid, the operator
`get_prep_info_class_mlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

`get_prep_info_class_mlp` may return the error 9211 (Matrix is
not positive definite) if *`Preprocessing`* =
*'canonical_variates'* is used. This typically indicates
that not enough training samples have been stored for each class.

## Possible Predecessors

`add_sample_class_mlp`,
`read_samples_class_mlp`

## Possible Successors

`clear_class_mlp`,
`create_class_mlp`

## References

Christopher M. Bishop: “Neural Networks for Pattern Recognition”;
Oxford University Press, Oxford; 1995.
  
Andrew Webb: “Statistical Pattern Recognition”; Arnold, London;
1999.

## Module

Foundation
