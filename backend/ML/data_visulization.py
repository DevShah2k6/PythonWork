import matplotlib.pyplot as plt
import seaborn as sns

def data_chart(crop):
    plt.scatter(crop["Min_x0020_Price"], crop["Max_x0020_Price"])
    plt.title("Min Price vs Max Price")
    plt.show()

    plt.hist(crop["Modal_x0020_Price"])
    plt.title("Modal Price Distribution")
    plt.show()

    avg_modal_price = crop.groupby("State")["Modal_x0020_Price"].mean()
    plt.figure(figsize=(10,12))
    plt.bar(avg_modal_price.index,avg_modal_price.values)
    plt.title("State-wise Average Modal Price")
    plt.xlabel("State")
    plt.ylabel("Average Modal Price")
    plt.show()

    avg_market_price = (
            crop.groupby("Market")["Modal_x0020_Price"]
            .mean()
            .sort_values(ascending=False)
            .head(10)
        )

    plt.figure(figsize=(12, 7))
    plt.bar(avg_market_price.index, avg_market_price.values)
    plt.title("Top 10 Markets by Average Modal Price")
    plt.xlabel("Market")
    plt.ylabel("Average Modal Price")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


    commodity_count = crop["Commodity"].value_counts().head(10)

    plt.figure(figsize=(12, 7))
    plt.bar(commodity_count.index, commodity_count.values)
    plt.title("Top 10 Commodities by Number of Market Records")
    plt.xlabel("Commodity")
    plt.ylabel("Number of Records")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()