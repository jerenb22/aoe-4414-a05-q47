# conv_ops.py
#
# Usage: python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p
# This script calculates the output shape and operation count of a convolution layer.
# Parameters:
# c_in: Input channel count
# h_in: Input height count
# w_in: Input width count
# n_filt: Number of filters in the convolution layer
# h_filt: Filter height count
# w_filt: Filter width count
# s: Stride of convolution filters
# p: Amount of padding on each of the four input map sides
#
# Output:
# The output channel count, output height count, output width count,
# number of additions performed, number of multiplications performed,
# and number of divisions performed.
#
# Written by Jeren Browder
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

import sys  # For command-line arguments

# Calculate the output dimensions and operations for a convolution layer
def calculate_convolution(c_in, h_in, w_in, n_filt, h_filt, w_filt, s, p):
    c_out = c_in
    h_out = ((h_in + 2 * p - h_filt) / s) + 1
    w_out = ((w_in + 2 * p - w_filt) / s) + 1

    adds = n_filt*h_out*w_out*c_in*h_filt*w_filt
    muls = n_filt*h_out*w_out*c_in*h_filt*w_filt # Each add corresponds to a multiplication for the convolution
    divs = 0     # No divisions in standard convolution operations
    
    return c_out, h_out, w_out, adds, muls, divs

# Initialize script arguments
c_in = h_in = w_in = n_filt = h_filt = w_filt = s = p = 0

# Parse script arguments
if len(sys.argv) == 9:
    c_in = float(sys.argv[1])
    h_in = float(sys.argv[2])
    w_in = float(sys.argv[3])
    n_filt = float(sys.argv[4])
    h_filt = float(sys.argv[5])
    w_filt = float(sys.argv[6])
    s = float(sys.argv[7])
    p = float(sys.argv[8])
else:
    print('Usage: python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p')
    exit()

# Write script below this line
c_out, h_out, w_out, adds, muls, divs = calculate_convolution(c_in, h_in, w_in, n_filt, h_filt, w_filt, s, p)

# Print the results
print(int(c_out))  # Output channel count
print(int(h_out))  # Output height count
print(int(w_out))  # Output width count
print(int(adds))   # Number of additions performed
print(int(muls))   # Number of multiplications performed
print(int(divs))   # Number of divisions performed
