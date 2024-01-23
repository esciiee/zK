pragma circom  2.0.0;

// implementation of ex-5 R1CS: out = 3*x*x*y + 5*x*y -x -2*y + 3

template EX5() {

    // Declaration of signals.

    // Input signals
    signal input x;
    signal input y;

    // Auxiliary signals
    signal v1;
    signal v2;

    // Output signals
    signal output out;

    // Constraints.
    v1 <== 3*x * x;
    v2 <== 5*x * y;
    out <== v1 * y + v2 - x - 2*y + 3;

}

component main = EX5();
