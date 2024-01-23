pragma circom  2.0.0;

template Multiply() {

    // Declaration of signals.
    signal input x;
    signal input y;

    signal output out;

    // Constraints.
    out <== x * y;

}

component main = Multiply();
