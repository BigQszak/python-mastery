#%%
x = 1172.5
print(x.as_integer_ratio())

print(x.is_integer())

y = 12345
print(y.numerator)
print(y.denominator)
y.bit_length()

# %%
symbols = 'AAPL IBM MSFT YHOO SCO'

symbols[0]
symbols[7]
symbols[-1]
symbols[-5]
# %%
symbols[:4]

# %%
symbols[-3:]

# %%
symbols[5:8]
# %%
'IBM' in symbols
# %%
'AA' in symbols

# %%
'CAT' in symbols
# %%
symbols.lower()
# %%
symbols
# %%
lowersymb = symbols.lower()
# %%
lowersymb
# %%
symbols
# %%
symbols.find('MSFT')

# %%
symbols = 'HPQ AAPL IBM MSFT YHOO  GOOG'
# %%
symlist = symbols.split()
# %%
symlist
# %%
symlist[0]

# %%
symlist[-1]

# %%
symlist
# %%
symlist[0]
# %%
'AIG' in symlist
# %%
'AA' in symlist
# %%
symlist.append('RHT')
# %%
symlist
# %%
prices = { 'IBM': 91.1, 'GOOG': 490.1, 'AAPL':312.23 }
# %%
prices['IBM']
# %%
prices['IBM'] = 123.45
# %%
prices
# %%
list(prices)
# %%
prices.keys()

# %%
prices.values()
# %%
