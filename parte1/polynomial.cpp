#include <iostream>
#include <chrono>

using namespace std;
using namespace std::chrono;

// Original iterative polynomial evaluation
long int polynomial_iter(const int n, const int x, const int* vec) {
    //2n
    //O(n)

    int p = vec[n];

    for(int i = n - 1; i >= 0; i--){
        p = vec[i] + x*p;
    }

    return p;
}

// Original recursive polynomial evaluation
long int polynomial_rec(const int n, const int x, const int* vec){
   //T(0) = 1
    //T(n) = T(n-1) + 1
    // O(2^n)

    if(n == 0) {
        return vec[0];
    }
    int p = vec[n] + x*polynomial_rec(n-1, x, vec);

    return p;
}

// AI iterative polynomial evaluation
long int ai_polynomial_iterative(const int n, const int x, const int* vec) {
    //2n
    //O(n)
    long int result = vec[0];
    for (int i = 1; i <= n; ++i) {
        result = result * x + vec[i];
    }
    return result;
}

// AI recursive polynomial evaluation
long int ai_polynomial_recursive(const int n, const int x, const int* vec) {
      //T(0) = 1
    //T(n) = T(n-1) + 1
    // O(2^n)

    if (n == 0)
        return vec[0];
    return x * ai_polynomial_recursive(n - 1, x, vec) + vec[n];
}


int main(int argc, char* argv[]) {
//cout << "Here"<<endl;
//     if (argc != 3) {
//        //print_usage(argv[0]);
//        return 1;
//    }

    std::string func = argv[1];
    int n = std::atoi(argv[2]);
    int x = std::atoi(argv[3]);

    int* vec = new int[n+1];

    for(int i = 0; i<= n; i++){
        vec[i] = 2;
    }

    if (n <= 0) {
        std::cerr << "Error: n must be a positive integer\n";
        delete[] vec;
        return 1;
    }

    long int result = 0;
    auto start = high_resolution_clock::now();

    for(int i=0; i<1; i++){
        if (func == "iter") {
            result = polynomial_iter(n, x, vec);
        } else if (func == "rec") {
            result = polynomial_rec(n, x, vec);
        } else if (func == "ai_iter") {
            result = ai_polynomial_iterative(n, x, vec);
        } else if (func == "ai_rec") {
        result = ai_polynomial_recursive(n, x, vec);
        }
    }
    auto end = high_resolution_clock::now();
    auto duration = duration_cast<std::chrono::nanoseconds>(end - start);

    delete[] vec;

    cout << func<<","<< n << "," << duration.count() <<","<< result<<"\n";
    return 0;
}