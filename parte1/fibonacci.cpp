#include <iostream>
#include <chrono>

using namespace std;
using namespace std::chrono;

// Original iterative Fibonacci
long int fibonacci_iter(int n) {
    //T(n) = 4n + 5
    //O(n)
    if (n == 1) {
        return 1;
    } else if (n == 2) {
        return 1;
    } else {
        int f1 = 1, f2 = 1, f = 0;
        for (int i = 2; i < n; i++) {
            f = f1 + f2;
            f1 = f2;
            f2 = f;
        }
        return f;
    }
}

// Original recursive Fibonacci
long int fibonacci_rec(int n) {
    //T(0) = 1
    //T(2) = 1
    //T(n) = T(n-1) + T(n-2)
    // O(2^n)

    if (n == 1) {
        return 1;
    } else if (n == 2) {
        return 1;
    } else {
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2);
    }
}

// AI iterative Fibonacci
long int ai_fibonacci_iterative(int n) {
    //T(n) = 4n + 4
    //O(n)
    if (n <= 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    }
    int prev = 0, curr = 1;
    for (int i = 2; i <= n; i++) {
        int temp = curr;
        curr = prev + curr;
        prev = temp;
    }
    return curr;
}

// AI recursive Fibonacci
long int ai_fibonacci_recursive(int n) {
    //T(0) = 1
    //T(2) = 1
    //T(n) = T(n-1) + T(n-2)
    //O(2^n)

    if (n <= 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    }
    return ai_fibonacci_recursive(n - 1) + ai_fibonacci_recursive(n - 2);
}


int main(int argc, char* argv[]) {
    if (argc != 3) {
        //print_usage(argv[0]);
        return 1;
    }

    std::string func = argv[1];
    int n = std::atoi(argv[2]);

    if (n <= 0) {
        std::cerr << "Error: n must be a positive integer\n";
        return 1;
    }

    long int result = 0;
    auto start = high_resolution_clock::now();

    for(int i=0; i<1; i++){
        if (func == "iter") {
            result = fibonacci_iter(n);
        } else if (func == "rec") {
            result = fibonacci_rec(n);
        } else if (func == "ai_iter") {
            result = ai_fibonacci_iterative(n);
        } else if (func == "ai_rec") {
        result = ai_fibonacci_recursive(n);
        }
    }
    auto end = high_resolution_clock::now();
    auto duration = duration_cast<std::chrono::nanoseconds>(end - start);

    cout << func<<","<< n << "," << duration.count() <<","<< result<<"\n";
    return 0;
}