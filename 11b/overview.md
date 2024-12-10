# Lecture 11b: Using Cython to get the speed of C in Python

In the earlier "Optimization" notebook we have demonstrated a number of techniques for optimizing python code, including using numpy to perform operations on arrays of input. We showed that with these techniques one can observe a significant speed up in the total run time of the program.

However, there are some instances in which numpy operations cannot be applied directly. Maybe there is no way to write what you are trying to do in terms of numpy operations. In these cases Cython can be used.

Cython code can be used to supplement python code. Cython code (like C or Fortran code) needs to be compiled before it can be run, but python's support for Cython will allow this to happen automatically. Cython code appears very similar to python code but a few different rules apply:

 * You will have to write out all for loops explictly - There is no numpy-like operations on an entire array that can be done
 * To acheive optimal performance you do need to think in terms of what the underlying C code, which this will be automatically translated into, will do. This is difficult without doing a whole other class dedicated to that language (we'll leave that until the 4th year!). However, important things to consider and the need to declare the types of variables (is this variable going to be used to store integers, or floating point numbers, or complex numbers, or ....) Also consider that creating a new storage array does take a little bit of time, so reuse arrays (reusing memory) when possible.

```{tableofcontents}
```

