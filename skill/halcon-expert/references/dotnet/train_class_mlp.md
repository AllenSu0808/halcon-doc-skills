# TrainClassMlp (Operator)

## Name

`TrainClassMlp` — Train a multilayer perceptron.

## Signature

`static void HOperatorSet.TrainClassMlp(HTuple MLPHandle, HTuple maxIterations, HTuple weightTolerance, HTuple errorTolerance, out HTuple error, out HTuple errorLog)`

`double HClassMlp.TrainClassMlp(int maxIterations, double weightTolerance, double errorTolerance, out HTuple errorLog)`

## Description

`TrainClassMlp` trains the multilayer perceptron (MLP) given
in *`MLPHandle`*. Before the MLP can be trained, *all*
training samples to be used for the training must be stored in the
MLP using [`AddSampleClassMlp`](add_sample_class_mlp.md) or
[`ReadSamplesClassMlp`](read_samples_class_mlp.md). If after the training new
additional training samples should be used a new MLP must be created
with [`CreateClassMlp`](create_class_mlp.md), in which again *all* training
samples to be used (i.e., the original ones and the additional ones)
must be stored. In these cases, it is useful to save and read the
training data with [`WriteSamplesClassMlp`](write_samples_class_mlp.md) and
[`ReadSamplesClassMlp`](read_samples_class_mlp.md), respectively. A second training
with additional training samples is not explicitly forbidden by
`TrainClassMlp`. However, this typically does not lead to
good results because the training of an MLP is a complex nonlinear
optimization problem, and consequently the second training with new
data will very likely lead to the fact that the optimization gets
stuck in a local minimum.

If a rejection class has been specified using
[`SetRejectionParamsClassMlp`](set_rejection_params_class_mlp.md), before the actual training
the samples for the rejection class are generated.

During the training, the error the MLP achieves on the stored
training samples is minimized by using a nonlinear optimization
algorithm. If the MLP has been regularized with
[`SetRegularizationParamsClassMlp`](set_regularization_params_class_mlp.md), an additional weight
penalty term is taken into account. With this, the MLP weights
described in [`CreateClassMlp`](create_class_mlp.md) are determined. Furthermore,
if an automatic determination of the regularization parameters has
been specified with [`SetRegularizationParamsClassMlp`](set_regularization_params_class_mlp.md),
these parameters are optimized as well. As described at
[`SetRegularizationParamsClassMlp`](set_regularization_params_class_mlp.md), training the MLP with
automatic determination of the regularization parameters requires
significantly more time than training an unregularized MLP or an MLP
with fixed regularization parameters.

[`CreateClassMlp`](create_class_mlp.md) initializes the MLP weights with random
values to make it very likely that the optimization converges to the
global minimum of the error function. Nevertheless, in rare cases
it may happen that the random values determined with
`randSeed` in [`CreateClassMlp`](create_class_mlp.md) result in a relatively
large optimum error, i.e., that the optimization gets stuck in a
local minimum. If it can be conjectured that this has happened the
MLP should be created anew with a different value for
`randSeed` in order to check whether a significantly smaller
error can be achieved.

The parameters *`maxIterations`*, *`weightTolerance`*, and
*`errorTolerance`* control the nonlinear optimization
algorithm. Note that if an automatic determination of the
regularization parameters has been specified with
[`SetRegularizationParamsClassMlp`](set_regularization_params_class_mlp.md), these parameters refer
to one training within one step of the evidence procedure.
*`maxIterations`* specifies the maximum number of iterations of
the optimization algorithm. In practice, values between
*100* and *200* should be sufficient for most
problems. *`weightTolerance`* specifies a threshold for the
change of the weights per iteration. Here, the absolute value of
the change of the weights between two iterations is summed. Hence,
this value depends on the number of weights as well as the size of
the weights, which in turn depend on the scaling of the training
data. Typically, values between *0.00001* and *1*
should be used. *`errorTolerance`* specifies a threshold for
the change of the error value per iteration. This value depends on
the number of training samples as well as the number of output
variables of the MLP. Also here, values between *0.00001*
and *1* should typically be used. The optimization is
terminated if the weight change is smaller than
*`weightTolerance`* and the change of the error value is
smaller than *`errorTolerance`*. In any case, the optimization
is terminated after at most *`maxIterations`* iterations. It
should be noted that, depending on the size of the MLP and the
number of training samples, the training can take from a few seconds
to several hours.

On output, `TrainClassMlp` returns the error of the MLP with
the optimal weights on the training samples in *`error`*.
Furthermore, *`errorLog`* contains the error value as a
function of the number of iterations. With this, it is possible to
decide whether a second training of the MLP with the same training
data without creating the MLP anew makes sense. If
*`errorLog`* is regarded as a function, it should drop off
steeply initially, while leveling out very flatly at the end. If
*`errorLog`* is still relatively steep at the end, it usually
makes sense to call `TrainClassMlp` again. It should be
noted, however, that this mechanism should *not* be used to
train the MLP successively with *`maxIterations`* =
*1* (or other small values for *`maxIterations`*)
because this will substantially increase the number of iterations
required to train the MLP. Note that if an automatic determination
of the regularization parameters has been specified with
[`SetRegularizationParamsClassMlp`](set_regularization_params_class_mlp.md), *`error`* and
*`errorLog`* refer to the last training that was executed in
the evidence procedure. If the error log should be monitored within
the individual iterations of the evidence procedure, the outer
iteration of the evidence procedure must be implemented explicitly,
as described at [`SetRegularizationParamsClassMlp`](set_regularization_params_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator modifies the state of the following input parameter:

- MLPHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`MLPHandle`** (input_control, state is modified)  class_mlp `→` [HClassMlp](HClassMlp.md), [HTuple](HTuple.md) (*IntPtr*)

MLP handle.

**`maxIterations`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum number of iterations of the
optimization algorithm.

Default:
200

Suggested values:
20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300

**`weightTolerance`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Threshold for the difference of the weights of
the MLP between two iterations of the
optimization algorithm.

Default:
1.0

Suggested values:
1.0, 0.1, 0.01, 0.001, 0.0001, 0.00001

Restriction:
`WeightTolerance >= 1.0e-8`

**`errorTolerance`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Threshold for the difference of the mean error
of the MLP on the training data between two
iterations of the optimization algorithm.

Default:
0.01

Suggested values:
1.0, 0.1, 0.01, 0.001, 0.0001, 0.00001

Restriction:
`ErrorTolerance >= 1.0e-8`

**`error`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Mean error of the MLP on the training data.

**`errorLog`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Mean error of the MLP on the training data as a
function of the number of iterations of the
optimization algorithm.

## Example (HDevelop)

```
* Train an MLP
create_class_mlp (NumIn, NumHidden, NumOut, 'softmax', \
                  'normalization', 1, 42, MLPHandle)
read_samples_class_mlp (MLPHandle, 'samples.mtf')
train_class_mlp (MLPHandle, 100, 1, 0.01, Error, ErrorLog)
write_class_mlp (MLPHandle, 'classifier.mlp')
```

## Result

If the parameters are valid, the operator `TrainClassMlp`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

`TrainClassMlp` may return the error 9211 (Matrix is not
positive definite) if `preprocessing` =
*"canonical_variates"* is used. This typically indicates
that not enough training samples have been stored for each class.

## Possible Predecessors

`AddSampleClassMlp`,
`ReadSamplesClassMlp`,
`SetRegularizationParamsClassMlp`

## Possible Successors

`EvaluateClassMlp`,
`ClassifyClassMlp`,
`WriteClassMlp`,
`CreateClassLutMlp`

## Alternatives

`TrainDlModelBatch`,
`ReadClassMlp`

## See also

`CreateClassMlp`

## References

Christopher M. Bishop: “Neural Networks for Pattern Recognition”;
Oxford University Press, Oxford; 1995.
  
Andrew Webb: “Statistical Pattern Recognition”; Arnold, London;
1999.

## Module

Foundation
