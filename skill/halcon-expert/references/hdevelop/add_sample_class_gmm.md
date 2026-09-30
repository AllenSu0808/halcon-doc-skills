# add_sample_class_gmm (Operator)

## Name

`add_sample_class_gmm` — Add a training sample to the training data of a Gaussian Mixture
Model.

## Signature

`add_sample_class_gmm( : : GMMHandle, Features, ClassID, Randomize : )`

## Description

`add_sample_class_gmm` adds a training sample to the Gaussian
Mixture Model (GMM) given by *`GMMHandle`*. The training
sample is given by *`Features`* and *`ClassID`*.
*`Features`* is the feature vector of the sample, and
consequently must be a real vector of length `NumDim`, as
specified in [`create_class_gmm`](create_class_gmm.md). *`ClassID`* is the
class of the sample, an integer between 0 and `NumClasses`-1
(set in [`create_class_gmm`](create_class_gmm.md)).

In the special case where the feature vectors are of
**integer** type, they are lying in the feature space in a grid
with step width 1.0. For example, the RGB feature vectors typically
used for color classification are triples having integer values
between 0 and 255 for each of their components. In fact, there
might be even several feature vectors representing the same point.
When training a GMM with such data, the training algorithm may tend
to align the modeled Gaussians along linearly dependent lines or
planes of data that are parallel to the grid dimensions. If the
number of `Centers` returned by [`train_class_gmm`](train_class_gmm.md) is
unusually high, this indicates such a behavior of the algorithm.
The parameter *`Randomize`* can be used to handle such
undesired effects. If *`Randomize`* > 0.0, random Gaussian
noise with mean 0 and standard deviation *`Randomize`* is added
to each component of the training data vectors, and the transformed
training data is stored in the GMM. For values of
*`Randomize`* $\le$ 1.0, the randomized data will look
like small clouds around the grid points, which does not improve the
properties of the data cloud. For values of *`Randomize`*
>> 2.0, the randomization might have a too strong
influence on the resulting GMM. For integer feature vectors, a
value of *`Randomize`* between 1.5 and 2.0 is recommended,
which transforms the integer data into homogeneous clouds,
without modifying its general form in the feature space. If the
data has been created from integer data by scaling, the same
problem may occur. Here, *`Randomize`* must be scaled with the
same scale factor that was used to scale the original data.

Before the GMM can be trained with [`train_class_gmm`](train_class_gmm.md),
*all* training samples must be added to the GMM with
`add_sample_class_gmm`.

The number of currently stored training samples can be queried with
[`get_sample_num_class_gmm`](get_sample_num_class_gmm.md). Stored training samples can be
read out again with [`get_sample_class_gmm`](get_sample_class_gmm.md).

Normally, it is useful to save the training samples in a file with
[`write_samples_class_gmm`](write_samples_class_gmm.md) to facilitate reusing the samples,
and to facilitate that, if necessary, new training samples can be
added to the data set, and hence to facilitate that a *newly
created* GMM can be trained *anew* with the extended data
set.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- GMMHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`GMMHandle`** (input_control, state is modified)  class_gmm `→`  (handle)

GMM handle.

**`Features`** (input_control)  real-array `→`  (real)

Feature vector of the training sample to be
stored.

**`ClassID`** (input_control)  number `→`  (integer)

Class of the training sample to be stored.

**`Randomize`** (input_control)  real `→`  (real)

Standard deviation of the Gaussian noise added
to the training data.

Default:
0.0

Suggested values:
0.0, 1.5, 2.0

Restriction:
`Randomize >= 0.0`

## Result

If the parameters are valid, the operator
`add_sample_class_gmm` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`create_class_gmm`

## Possible Successors

`train_class_gmm`,
`write_samples_class_gmm`

## Alternatives

`read_samples_class_gmm`,
`add_samples_image_class_gmm`

## See also

`clear_samples_class_gmm`,
`get_sample_num_class_gmm`,
`get_sample_class_gmm`

## Module

Foundation
