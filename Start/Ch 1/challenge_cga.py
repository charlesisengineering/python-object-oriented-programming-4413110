# Python Object Oriented Programming by Joe Marini course example
# Programming challenge: define a class to represent a stock symbol

# Challenge: create a class to represent stock information.
# Your class should have properties for:
# Ticker (string)
# Price (float)
# Company (string)
# And a method get_description() which returns a string in the form
# of "Ticker: Company -- $Price"

class Stock:
  def __init__(self, ticker, price, name):
    self.ticker = ticker
    self.price = price
    self.name = name

  def get_description(self):
    description = '{0}: {1} -- ${2}'.format(self.ticker, self.name, self.price)
    return description
    # return f'{self.ticker}: {self.name} -- ${self.price}' TODO research what this nice way to do it is called


# ~~~~~~~~~ TEST CODE ~~~~~~~~~
msft = Stock("MSFT", 342.0, "Microsoft Corp")
goog = Stock("GOOG", 135.0, "Google Inc")
meta = Stock("META", 275.0, "Meta Platforms Inc")
amzn = Stock("AMZN", 135.0, "Amazon Inc")

print(msft.get_description())
print(goog.get_description())
print(meta.get_description())
print(amzn.get_description())
