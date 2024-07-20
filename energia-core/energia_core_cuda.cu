#include <cuda_runtime.h>
#include <stdio.h>

__global__ void energia_device_read_data_kernel(int *device_id, float *data, int len) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < len) {
        // Read data from device hardware
        data[idx] = device_id[idx] * 2.0f;
    }
}

__global__ void energia_device_write_data_kernel(int *device_id, float *data, int len) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < len) {
        // Write data to device hardware
        device_id[idx] = (int)data[idx] / 2;
    }
}

extern "C" {
    void energia_device_read_data(int *device_id, float *data, int len) {
        int blockSize = 256;
        int numBlocks = (len + blockSize - 1) / blockSize;
        energia_device_read_data_kernel<<<numBlocks, blockSize>>>(device_id, data, len);
        cudaDeviceSynchronize();
    }

    void energia_device_write_data(int *device_id, float *data, int len) {
        int blockSize = 256;
        int numBlocks = (len + blockSize - 1) / blockSize;
        energia_device_write_data_kernel<<<numBlocks, blockSize>>>(device_id, data, len);
        cudaDeviceSynchronize();
    }
}
