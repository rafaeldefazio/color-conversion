"""
MIT License
-----------

Copyright (c) 2020 Rafael Biagioni de Fazio (github.com/rafaeldefazio/)
Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""


# precondition: normalized RGB color
# postcondition: color in HSV
def RGBtoHSV(r, g, b):

	r = float(r)
	g = float(g)
	b = float(b)

	minimum = min(r, g, b)
	maximum = max(r, g, b)

	if maximum > 0:
		S = (maximum - minimum ) / maximum
	else:
		S = 0

	V = maximum

	delta = maximum - minimum

	if S == 0:
		H = -1

	else:

		if r is maximum:
			if g < b:
				H = (60 * (g - b)/delta) + 360
			else:
				H = (60 * (g - b)/delta)
		elif g is maximum:
			H = (60 * (b - r)/delta) + 120

		else:
			H = (60 * (r - g)/delta) + 240

	return (H, S, V)


# precondition: normalized RGB color
# postcondition: color in CMY
def RGBtoCMY(r, g, b):
	return (1-r, 1-g, 1-b)


# precondition: normalized RGB color
# postcondition: color in XYZ (3 decimal places)
# output[0] is X, Y, Z
# outupt[1] is Xc, Yc, Zc

def RGBtoXYZ(r, g, b, decimal=3):

	r = float(r)
	g = float(g)
	b = float (b)


	X = (0.49 * r) + (0.31 * g) + (0.2 * b)
	Y = (0.177 * r) + (0.812 * g) + (0.011 * b)
	Z = (0 * r) + (0.01 * g) + (0.99 * b)


	if (X+Y+Z) == 0:
		return (0.0,0.0,0.0)
	else:
		Xc = X/(X+Y+Z)
		Yc = Y/(X+Y+Z)
		Zc = 1 - Xc - Yc

		return (
			(round(X, decimal), round(Y, decimal), round(Z, decimal)),
			(round(Xc, decimal), round(Yc, decimal), round(Zc, decimal))
			 )


# Test colors
colors = (
	(0, 0, 1), # pure blue
	(1, 1, 1), # white
	(0.5, 0.5, 0.5), # medium gray
	(1, 0.5, 0), # orange
	(0, 0.2, 0.2), # dark cyan
	(0, 0, 0), # black
	(0.5, 1, 0.5) # light green
	)

for r, g, b in colors:

	print(f'[Color: ({r}, {g}, {b}) in RGB]')

	HSV = RGBtoHSV(r, g, b)
	CMY = RGBtoCMY(r, g, b)
	XYZ = RGBtoXYZ(r, g, b)

	print(f'HSV:\t {HSV}')
	print(f'CMY:\t', CMY)

	print('XYZ:')
	print(f'\t(X, Y, Z) is {XYZ[0]}')
	print(f'\t(Xc, Yc, Zc) is {XYZ[1]}')

	print('\n')
