# QueryAopInfo (Operator)

## Name

`QueryAopInfo` — Query indexing structure of AOP information for operators.

## Signature

`static void HOperatorSet.QueryAopInfo(HTuple operatorName, HTuple indexName, HTuple indexValue, out HTuple name, out HTuple value)`

`static HTuple HSystem.QueryAopInfo(HTuple operatorName, HTuple indexName, HTuple indexValue, out HTuple value)`

`static HTuple HSystem.QueryAopInfo(string operatorName, string indexName, string indexValue, out HTuple value)`

## Description

HALCON supports a mechanism to adapt the behavior of automatic
parallelization of image processing operators (AOP) to the machine's
hardware capability. The
information for this adaption can be obtained by the operator
[`OptimizeAop`](optimize_aop.md) and can be partly read and modified by the operators
[`GetAopInfo`](get_aop_info.md) and [`SetAopInfo`](set_aop_info.md), respectively. To address
specific AOP information the operator's optimization data is indexed within
a 3-ary hierarchy that can be obtained by `QueryAopInfo`. The
three hierarchy stages are indexed by the operator name, the iconic type,
and a parameter string value denoting a special mode or method supported by
the operator.

If an empty string *""* is passed to *`operatorName`*,
the parameters *`indexName`* and *`indexValue`* are ignored and
all operator names in *`value`* are returned, for which optimization
data is stored.
*`name`* contains the index identifier *"operator"* as many
times as operator names are returned. Specifying a single operator
name in *`operatorName`* and passing an empty string *""* to the
parameters
*`indexName`* and *`indexValue`* queries all iconic types
the operator holds optimization data for. *`value`* contains the type
strings, *`name`* the index identifier *"iconic_type"*,
respectively. Finally, when specifying a certain
operator in *`operatorName`* and a specific iconic type by passing the
dimension identifier *"iconic_type"* to *`indexName`* and
the specific iconic type to *`indexValue`*, *`name`* contains
the parameter index identifier *`value`* holds the parameter string
values supported by the operator. The format of the parameter identifier
string is compound containing the string *parameter*, followed by
a colon separator *:* and a digit, denoting the
parameter index (starting with 1). If the operator does not
support any mode parameter or the operator's parameter values were not
varied during optimization process of [`OptimizeAop`](optimize_aop.md) the string
*"parameter:0"* is returned for *`name`* and *`value`*
contains an empty string. In case no AOP information is stored for the
specified index, *`name`* returns an empty string.

## Execution Information

- Multithreading type: exclusive (runs in parallel only with independent operators).
- Multithreading scope: local (may only be called from the same thread in which the window, model, or tool instance was created).
- Processed without parallelization.

## Parameters

**`operatorName`** (input_control)  string `→` [HTuple](HTuple.md) (*string* / int / long)

Operator to get information for

Default:
""

**`indexName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Further specific index

Default:
""

Suggested values:
"", "iconic_type"

**`indexValue`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Further specific address

Number of elements:
IndexName == IndexValue

Default:
""

Suggested values:
"", "byte", "int1", "int2", "uint2", "int4", "int8", "direction", "cyclic", "vector_field", "complex", "region", "xld", "xld_cont", "xld_poly"

**`name`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Name of next index stage

**`value`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Values of next index stage

## Result

`QueryAopInfo` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Module

Foundation
