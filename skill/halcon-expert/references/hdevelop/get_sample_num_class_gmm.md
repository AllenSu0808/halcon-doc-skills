# get_sample_num_class_gmm (Operator)

## Name

`get_sample_num_class_gmm` — Return the number of training samples stored in the training data of
a Gaussian Mixture Model (GMM).

## Signature

`get_sample_num_class_gmm( : : GMMHandle : NumSamples)`

## Description

`get_sample_num_class_gmm` returns in *`NumSamples`* the
number of training samples that are stored in the Gaussian Mixture
Model (GMM) given by *`GMMHandle`*.
`get_sample_num_class_gmm` should be called before the
individual training samples are read out with
[`get_sample_class_gmm`](get_sample_class_gmm.md), e.g., for the purpose of reclassifying
the training data (see [`get_sample_class_gmm`](get_sample_class_gmm.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`GMMHandle`** (input_control)  class_gmm `→`  (handle)

GMM handle.

**`NumSamples`** (output_control)  integer `→`  (integer)

Number of stored training samples.

## Result

If the parameters are valid, the operator
`get_sample_num_class_gmm` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`add_sample_class_gmm`,
`add_samples_image_class_gmm`,
`read_samples_class_gmm`

## Possible Successors

`get_sample_class_gmm`

## See also

`create_class_gmm`

## Module

Foundation
