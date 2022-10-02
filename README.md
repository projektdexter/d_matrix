# distance_matrix
This function will generate a distance matrix for a set of points on the cartesian plane

This distance matrix is particularly useful for testing Vehicle Routing Problem or Traveling Salesperson Problem in supply chain.

 
## Users can initialize the input parameters as follows:

**_input_:** (int or nx2 dataframe) 

If input is an **integer n** the code will generate **n random points** on a plane and calculate the **pairwise distance** between all the points and return a **nxn matrix**.

If input is a **pandas nx2 dataframe** with x_cordinates in column 0 and y_coordinates in column 1 the code will directly calculate the **pairwise distance** between all the points and return a **nxn matrix**.

**_depo_init_** = False (default): If depo_init is set to True, the code will add a point for at row 0 with coordinates = (depo_x, depo_y)

**_depo_x_** =0 (default), **_depo_y_** = 0 (default): x and y coordinates of the depot point

**_x_lb_** = 0 (default), **_y_lb_** = 0 (default), **_x_ub_** = 100 (default), **_y_ub_** = 100 (default): User can also pass the lower bound and upper bound for random points.

## Example 1:
```
df, d_matrix = random_dmatrix(input = 10)
print(df)
print(d_matrix)
```
## Output:

```
df =
 x_cord  y_cord
0      58      58
1      85      29
2      46      28
3      67      89
4      68      34
5      12      10
6      79      29
7      31       8
8      44      66
9       2      66

d_matrix =
      0     1     2     3     4     5     6     7     8     9
0   0.0  40.0  32.0  32.0  26.0  66.0  36.0  57.0  16.0  57.0
1  40.0   0.0  39.0  63.0  18.0  75.0   6.0  58.0  55.0  91.0
2  32.0  39.0   0.0  65.0  23.0  38.0  33.0  25.0  38.0  58.0
3  32.0  63.0  65.0   0.0  55.0  96.0  61.0  89.0  33.0  69.0
4  26.0  18.0  23.0  55.0   0.0  61.0  12.0  45.0  40.0  73.0
5  66.0  75.0  38.0  96.0  61.0   0.0  70.0  19.0  64.0  57.0
6  36.0   6.0  33.0  61.0  12.0  70.0   0.0  52.0  51.0  85.0
7  57.0  58.0  25.0  89.0  45.0  19.0  52.0   0.0  59.0  65.0
8  16.0  55.0  38.0  33.0  40.0  64.0  51.0  59.0   0.0  42.0
9  57.0  91.0  58.0  69.0  73.0  57.0  85.0  65.0  42.0   0.0
```
## Example 2:
```
df, d_matrix = random_dmatrix(input = 10, depo_init=True, depo_x=10, depo_y=15)
print(df)
print(d_matrix)
```
## Output:

```
df =
 x_cord  y_cord
0      10      15
1      96       8
2      32      17
3      47      86
4      66      74
5      47      75
6      67      56
7      78      38
8       3      83
9       6      72

d_matrix = 
      0      1     2     3     4     5     6     7      8      9
0   0.0   86.0  22.0  80.0  81.0  70.0  70.0  72.0   68.0   57.0
1  86.0    0.0  65.0  92.0  72.0  83.0  56.0  35.0  119.0  110.0
2  22.0   65.0   0.0  71.0  66.0  60.0  52.0  51.0   72.0   61.0
3  80.0   92.0  71.0   0.0  22.0  11.0  36.0  57.0   44.0   43.0
4  81.0   72.0  66.0  22.0   0.0  19.0  18.0  38.0   64.0   60.0
5  70.0   83.0  60.0  11.0  19.0   0.0  28.0  48.0   45.0   41.0
6  70.0   56.0  52.0  36.0  18.0  28.0   0.0  21.0   69.0   63.0
7  72.0   35.0  51.0  57.0  38.0  48.0  21.0   0.0   87.0   80.0
8  68.0  119.0  72.0  44.0  64.0  45.0  69.0  87.0    0.0   11.0
9  57.0  110.0  61.0  43.0  60.0  41.0  63.0  80.0   11.0    0.0
```
## Example 3:
```
df, d_matrix = random_dmatrix(input = 10, depo_init=True, depo_x=10, depo_y=15, x_lb=5, y_lb=5, x_ub=20, y_ub=20)
print(df)
print(d_matrix)
```
## Output:

```
df =
 x_cord  y_cord
0      10      15
1      12       9
2       9      11
3      15      16
4      17       6
5      14       7
6      11      19
7      16       9
8      17      16
9      18      10

d_matrix = 
      0     1    2     3     4     5     6     7     8     9
0   0.0   6.0  4.0   5.0  11.0   9.0   4.0   8.0   7.0   9.0
1   6.0   0.0  4.0   8.0   6.0   3.0  10.0   4.0   9.0   6.0
2   4.0   4.0  0.0   8.0   9.0   6.0   8.0   7.0   9.0   9.0
3   5.0   8.0  8.0   0.0  10.0   9.0   5.0   7.0   2.0   7.0
4  11.0   6.0  9.0  10.0   0.0   3.0  14.0   3.0  10.0   4.0
5   9.0   3.0  6.0   9.0   3.0   0.0  12.0   3.0   9.0   5.0
6   4.0  10.0  8.0   5.0  14.0  12.0   0.0  11.0   7.0  11.0
7   8.0   4.0  7.0   7.0   3.0   3.0  11.0   0.0   7.0   2.0
8   7.0   9.0  9.0   2.0  10.0   9.0   7.0   7.0   0.0   6.0
9   9.0   6.0  9.0   7.0   4.0   5.0  11.0   2.0   6.0   0.0
```
## Example 4:
```
df, d_matrix = random_dmatrix(input = pd.DataFrame({'x_cord': [10,15,20,25],'y_cord':[10,25,30,24]}), 
                                                    depo_init=True, depo_x=10, depo_y=15)
print(df)
print(d_matrix)
```
## Output:

```
df = 
x_cord  y_cord
0      10      15
1      10      10
2      15      25
3      20      30
4      25      24

d_matrix =
      0     1     2     3     4
0   0.0   5.0  11.0  18.0  17.0
1   5.0   0.0  16.0  22.0  21.0
2  11.0  16.0   0.0   7.0  10.0
3  18.0  22.0   7.0   0.0   8.0
4  17.0  21.0  10.0   8.0   0.0
