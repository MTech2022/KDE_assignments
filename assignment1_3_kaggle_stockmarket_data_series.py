import pandas as pd
import matplotlib.pyplot as plot  # For plotting graphs

#https://matplotlib.org/stable/gallery/style_sheets/fivethirtyeight.html
plot.style.use('fivethirtyeight')


df = pd.read_csv("./data/ADANIPORTS.csv")
#Attribute: ['Date','Volume', 'High','Low','Close','Open']
print("~~~~~~~~~: i. Plot the temporal change of attributes High and Low values :~~~~~~~~~");
print("CLOSE current plot figure to open next plot-------------------\n");
plot.figure(figsize=(12, 6))
plot.plot(df[["High", "Low"]], label=["High","Low"])
plot.title('Temporal change of attributes High and Low values')
plot.legend(loc='best')
plot.show()


print("~~~~~~~~~: ii. A boxplot with Open and Close attributes on the x-axis displayed :~~~~~~~~~");
print("CLOSE current plot figure to open next plot-------------------\n");
plot.figure(figsize=(12, 6))
plot.boxplot(df[['Close', 'Open']], labels=["Close", "Open"],showfliers=False)
plot.title('A boxplot with Open and Close attributes on the x-axis displayed')
plot.show()

print("~~~~~~~~~: iii. A histogram with the Volume attribute :~~~~~~~~~");
print("CLOSE current plot figure to open next plot-------------------\n");
plot.figure(figsize=(12, 6))
plot.hist(df['Volume'], label="Volume")
plot.title('A histogram with the Volume attribute')
plot.legend(loc='best')
plot.show()
