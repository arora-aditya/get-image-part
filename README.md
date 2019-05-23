ECE 252 Lab 2 Backend
==================

This is a tiny python script to return parts of an image (requires pillow, tornado).
It simulates some service that does computation and returns after some time.
Instead of computing, the script just waits abs(random.gauss(0.2, 0.2)) seconds and then returns the image.

_Credit for most of the project goes to [Prof. Patrick Lam](https://github.com/patricklam) and [this repository](https://github.com/patricklam/get-image-part)_

It has been modified to match the expected response for ECE252
