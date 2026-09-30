# ReadKalman (Operator)

## Name

`ReadKalman` — Read the description file of a Kalman filter.

## Warning

**`ReadKalman` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.ReadKalman(HTuple fileName, out HTuple dimension, out HTuple model, out HTuple measurement, out HTuple prediction)`

`static HTuple HMisc.ReadKalman(string fileName, out HTuple model, out HTuple measurement, out HTuple prediction)`

## Description

The operator `ReadKalman` reads the description file
*`fileName`* of a Kalman filter. Kalman filters return an
estimate of the current state (or even the prediction of a future state)
of a discrete, stochastically disturbed, linear system. They are
successfully used in image processing, especially in the analysis of
image sequences. A Kalman filtering is based on a mathematical model
of the system to be examined which at any point in time has the following
characteristics:

- **Model parameter:** —

  transition matrix $A$, control matrix $G$ including
  the controller output $u$ and the measurement matrix $C$
- **Model stochastic:** —

  system-error covariance matrix $Q$,
  system-error - measurement-error covariance matrix $L$
  and measurement-error covariance matrix $R$
- **Estimate of the initial state of the system:** —

  state $x_{0}$ and corresponding covariance matrix $P_{0}$

Many systems do not need entries “from outside”, and therefore $G$
and $u$ can be dropped. Further, system errors and measurement
errors are normally not correlated ($L$ is dropped). The
characteristics mentioned above can be stored in an ASCII-file and then
can be read with the help of the operator `ReadKalman`.
This ASCII-file must have the following structure:
Dimension row
+ content row
+ matrix A
+ matrix C
+ matrix Q
[ + matrix G + vector u ]
[ + matrix L ]
+ matrix R
[ + matrix P0 ]
[ + vector x0 ]
The dimension row thereby is always of the following form:
n = <integer> m = <integer> p = <integer>
whereby n indicates the number of the state variables, m the number
of the measurement values and p the number of the controller members
(see also *`dimension`*). The maximal dimension will hereby
be limited by a system constant (= 30 for the time being).

The content row has the following form:
A*C*Q*G*u*L*R*P*x*
and describes the following content of the file. Instead of $'\ast'$,
'+' (= parameter is available) respectively '-' (= parameter is missing)
have to be set. Please note that only the parameters marked by [...] in the
above list may be left out in the description file. If the initial state
estimate $a_{0}$ is missing (i.e. 'x-'), the components of the
vector will supposed to be 0.0. If the covariance matrix $P_{0}$ of
the initial state estimate is missing (i.e. 'P-'), the error will be
supposed to be tremendous. In this case the matrix elements will be set
to 10000.0. This value seems to be very high, however, it is only sufficient
if the range of components of the state vector x is smaller to the
tenth power.
$(r\times s)$ matrices will be stored per row in the following
form:
$$\langle a_{11} \rangle \langle a_{12} \rangle \dots \langle a_{1s} \rangle\\ \vdots \\\n\langle a_{r1} \rangle \langle a_{r2} \rangle \dots \langle a_{rs} \rangle$$ ![figure](../assets/4a0f9711d352a72f.svg)
(the spaces and line feed characters can be chosen at will),

vectors will be stored correspondingly in the following form:
![figure](../assets/771fe1afd418c73d.svg)
The following parameter values are returned by the operator
`ReadKalman`:

- ***`dimension`*:** —

  This parameter includes the dimensions of the status vector, the
  measurement vector and the controller vector. *`dimension`*
  thereby is a vector $[n,m,p]$, whereby
  $n$ indicates the number of the state variables,
  $m$ the number of the measurement values and
  $p$ the number of the controller members.
  For a system without determining control
  (i.e. without influence “from outside”) therefore
  *`dimension`* = $[n,m,0]$.
- ***`model`*:** —

  This parameter includes the lined up matrices (vectors)
  $A,C,Q,G,u$ and (if necessary)
  $L$ having been stored in row-major order.
  *`model`* therefore is a vector of the length
  $n\times n+n\times m+n\times n+n\times p+p[+n\times m]$.
  The last summand is dropped, in case the system errors and measurement
  errors are not correlated, i.e. there is no value for $L$.
- ***`measurement`*:** —

  This parameter includes the matrix $R$ which has been stored
  in row-major order. *`measurement`* therefore is vector of the
  dimension $m\times m$.
- ***`prediction`*:** —

  This parameter includes the matrix $P_{0}$ (the error
  covariance matrix of the initial state estimate) and the initial state
  estimate $x_{0}$ lined up. This means, it is a vector of the
  length $n\times n+n$.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

Description file for a Kalman filter.

Default:
"kalman.init"

**`dimension`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

The dimensions of the state vector, the measurement
vector and the controller vector.

**`model`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

The lined up matrices $A,C,Q$, possibly
$G$ and $u$, and if necessary $L$
stored in row-major order.

**`measurement`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

The matrix $R$ stored in row-major order.

**`prediction`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

The matrix $P_{0}$ (error covariance matrix of
the initial state estimate) stored in row-major order
and the initial state estimate $x_{0}$ lined up.

## Example (HDevelop)

```
* An example of the description-file:
*
* n=3 m=1 p=0
* A+C+Q+G-u-L-R+P+x+
* transition matrix A:
* 1 1 0.5
* 0 1 1
* 0 0 1
* measurement matrix C:
* 1 0 0
* system-error covariance matrix Q:
* 54.3 37.9 48.0
* 37.9 34.3 42.5
* 48.0 42.5 43.7
* measurement-error covariance matrix R:
* 1.2
* estimation-error covariance matrix (for the initial estimate) P0: \
* 0 0 0
* 0 180.5 0
* 0 0 100
* initial estimate x0:
* 0 100 0
*
* the result of read_kalman with the upper descriptionfile
* as inputparameter:
*
* Dimension   = [3,1,0]
* Model       = [1.0,1.0,0.5,0.0,1.0,1.0,0.0,0.0,1.0,1.0,0.0,0.0,
*                     54.3,37.9,48.0,37.9,34.3,42.5,48.0,42.5,43.7]
* Measurement = [1.2]
* Prediction  = [0.0,0.0,0.0,0.0,180.5,0.0,0.0,0.0,100.0,0.0,100.0,
*                           0.0].
```

## Result

If the description file is readable and correct, the operator
`ReadKalman` returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is
raised.

## Possible Successors

`FilterKalman`

## See also

`UpdateKalman`,
`FilterKalman`

## Module

Foundation
