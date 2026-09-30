# update_kalman (Operator)

## Name

`update_kalman` — Read an update file of a Kalman filter.

## Warning

**`update_kalman` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`update_kalman( : : FileName, DimensionIn, ModelIn, MeasurementIn : DimensionOut, ModelOut, MeasurementOut)`

## Description

The operator `update_kalman` reads the update file
*`FileName`* of a Kalman filter. Kalman filters return an
estimate of the current state (or even the prediction of a future state)
of a discrete, stochastically disturbed, linear system.

A Kalman filtering is based on a mathematical model of the system
to be examined which at any point in time has the following
characteristics:

- **Model parameter:** —

  transition matrix $A$, control matrix $G$ including the controller
  output $u$ and the measurement matrix $C$
- **Model stochastic:** —

  system-error covariance matrix $Q$, system-error - measurement-error
  covariance matrix $L$ and measurement-error covariance matrix $R$
- **Measurement vector:** —

  $y$
- **History of the system:** —

  extrapolation vector $\hat{x}$ ![figure](../assets/45170b4d5c95d84b.svg) and extrapolation-error covariance
  matrix $\hat{P}$ ![figure](../assets/3a73586742c2d851.svg)

Many systems do not need entries “from outside” and therefore $G$
and $u$ can be dropped. Further, system errors and measurement
errors are normally not correlated ($L$ is dropped). Some of the
characteristics mentioned above may change dynamically (from one iteration
to the next). The operator `update_kalman` serves to modify
parts of the system according to an update file (ASCII) with the following
structure (see also [`read_kalman`](read_kalman.md)):
Dimension row
+ content row
+ matrix A
+ matrix C
+ matrix Q
+ matrix G + vector u
+ matrix L
+ matrix R
The dimension row thereby has the following form:
n = <integer> m = <integer> p = <integer>
whereby n indicates the number of the state variables, m the number
of the measurement values and p the number of the controller members
(see also *`DimensionIn`* / *`DimensionOut`*).
The maximal dimension will hereby be limited by a system constant
(= 30 for the time being). As in this case changes should take
effect at a valid model, the dimensions n and m are invariant
(and will only be indicated for purposes of control).

The content row has the following form:
A*C*Q*G*u*L*R*
and describes the further content of the file. Instead of
$'\ast'$, '+' (= parameter is available) respectively
'-' (= parameter is missing) has to be set. In contrast to
description files for [`read_kalman`](read_kalman.md), the system
description needs not be complete in this case. Only those parts
of the system which are changed must be indicated. The indication
of estimated values is unnecessary, as these values must stem
from the latest filtering according to the structure of the filter.

$(r\times s)$ matrices will be stored in row-major
order in the following form:
$$\langle a_{11} \rangle \langle a_{12} \rangle \dots \langle a_{1s} \rangle\\ \vdots \\\n\langle a_{r1} \rangle \langle a_{r2} \rangle \dots \langle a_{rs} \rangle$$ ![figure](../assets/4a0f9711d352a72f.svg)
(the spaces/line feed characters can be chosen at will),

vectors will be stored correspondingly in the following form:
$$<comment,i.e. string> \n< a_1 > \cdots < a_k >$$ ![figure](../assets/5d650faa6c73d432.svg)
The following parameter values of the operator [`read_kalman`](read_kalman.md)
will be changed:

- ***`DimensionIn`* / *`DimensionOut`*:** —

  These parameters include the dimensions of the state vector, measurement
  vector and controller vector and therefore are vectors
  $[n,m,p]$, whereby $n$ indicates the
  number of the state variables, $m$ the number of the measurement
  values and $p$ the number of the controller members.
  $n$ and $m$ are invariant for a given system,
  i.e. they must not differ from corresponding input
  values of the update file.
  For a system without without influence “from outside”
  $p$ = *0*.
- ***`ModelIn`* / *`ModelOut`*:** —

  These parameters include the lined up matrices (vectors)
  $A,C,Q,G,u$ and if necessary
  $L$ which have been stored in row-major order.
  *`ModelIn`* / *`ModelOut`* therefore are vectors of the
  length $n\times n+n\times m+n\times n+n\times p+p[+n\times m]$.
  The last summand is dropped if system errors and measurement errors
  are not correlated, i.e. no value has been set for $L$.
- ***`MeasurementIn`* / *`MeasurementOut`*:** —

  These parameters include the matrix $R$ stored in row-major order,
  and therefore are vectors of the dimension $m\times m$.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`FileName`** (input_control)  filename.read `→`  (string)

Update file for a Kalman filter.

Default:
'kalman.updt'

**`DimensionIn`** (input_control)  integer-array `→`  (integer)

The dimensions of the state vector, measurement
vector and controller vector.

Default:
[3,1,0]

Value range:
`0
≤
DimensionIn
≤
30`

**`ModelIn`** (input_control)  real-array `→`  (real)

The lined up matrices A,C,Q, possibly G and u, and if
necessary L which all have been stored in row-major
order.

Default:
[1.0,1.0,0.5,0.0,1.0,1.0,0.0,0.0,1.0,1.0,0.0,0.0,54.3,37.9,48.0,37.9,34.3,42.5,48.0,42.5,43.7]

Value range:
`0.0
≤
ModelIn
≤
10000.0`

**`MeasurementIn`** (input_control)  real-array `→`  (real)

The matrix R stored in row-major order.

Default:
[1,2]

Value range:
`0.0
≤
MeasurementIn
≤
10000.0`

**`DimensionOut`** (output_control)  integer-array `→`  (integer)

The dimensions of the state vector, measurement
vector and controller vector.

**`ModelOut`** (output_control)  real-array `→`  (real)

The lined up matrices A,C,Q, possibly G and u, and if
necessary L which all have been stored in row-major
order.

**`MeasurementOut`** (output_control)  real-array `→`  (real)

The matrix R stored in row-major order.

## Example (HDevelop)

```
* The following values are describing the system
*
* DimensionIn   = [3,1,0]
* ModelIn       = [1.0,1.0,0.5,0.0,1.0,1.0,0.0,0.0,1.0,1.0,0.0,0.0,
*                       54.3,37.9,48.0,37.9,34.3,42.5,48.0,42.5,43.7]
* MeasurementIn = [1,2]
*
* An example of the Updatefile:
*
* n=3 m=1 p=0
* A+C-Q-G-u-L-R-
* transitions at time t=15:
* 2 1 1
* 0 2 2
* 0 0 2
*
* the results of update_kalman:
*
* DimensionOut   = [3,1,0]
* ModelOut       = [2.0,1.0,1.0,0.0,2.0,2.0,0.0,0.0,2.0,1.0,0.0,0.0,
*                        54.3,37.9,48.0,37.9,34.3,42.5,48.0,42.5,43.7]
* MeasurementOut = [1.2]
```

## Result

If the update file is readable and correct, the operator
`update_kalman` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Successors

`filter_kalman`

## See also

`read_kalman`,
`filter_kalman`

## Module

Foundation
