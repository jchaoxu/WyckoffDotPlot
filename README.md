# How to use this graph plotter
  1. Double click main.exe
  2. Enter required inputs.
  3. Find the output graph in the rst folder.

## Inputs Description

### Number of days
- Means how many days before the current date you would like to include within the graph. For example, you want to see a graph starting from 6 days ago, type in 5.
  - Please be aware of that non-working days are included.
  - start date will be: today - (the input you give)
  - end date will be: today

### Stock Code
- Indicate the code of the stock you want.
- The prefix means the markets the stock belongs to.
  - sz for Shenzhen
  - sh for Shanghai
- The 6 digits means the stock code
- Example: sz.000001 for 平安银行, sh.603000 for 人民网.

### Frequency
- The data frequency used to plot the graph. "d" for daily K data, '30' for 30-minute-k data, and so on.
- Indicates the data precision. Smaller the input is, more dots will be provided.

### Stock price decimal places
- How many decimal places you want for the stock price.
  - For example, if the input is 1, only 1 decimal places will be used during plotting, i.e., 16.39 will be counted as 16.3.
- Do not provide any inputs larger than 2.
- 0 means keep all decimal places.
- Tips: You may want to keep more decimal places if the stock price is low.

### Dot number
- The compression ratio.
- Indicate the type of the dot plot (i.e., single dot ploat, three dot plat, five dot plot).
- Please enter a integer greater or equal to 1.
