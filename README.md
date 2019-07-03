# ECE 252 Labs Backend
---

This is a tiny python script to return parts of an image (requires pillow, tornado).

#### `get-image-part_L2.py`
It simulates some service that does computation and returns a random strip of the image after some time.
Instead of computing, the script just waits `abs(random.gauss(0.2, 0.2))` seconds and then returns the image.

##### Valid URL
`http://ece252-M.arora-aditya.com:2520/image?img=N`

`M,N = 1,2,3`

#### `get-image-part_L3.py`
This service takes in the part number, and returns the corresponding part of the image without any wait time

##### Valid URL
`http://ece252-M.arora-aditya.com:2530/image?img=N&part=K`

`M,N = 1,2,3 ` and ` 0<=K<=49`

\
_Credit for the images inside used goes to [Irene Huang](https://github.com/yqh).Credit for most of the project goes to [Prof. Patrick Lam](https://github.com/patricklam) and [this repository](https://github.com/patricklam/get-image-part)_

It has been modified to match the expected response for ECE252
