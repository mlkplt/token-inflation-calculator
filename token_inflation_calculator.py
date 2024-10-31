#author: @mlkplt

def calculate_annual_inflation(circulating_supply, new_supply_per_unlock, unlock_frequency='quarterly'):
    """
    Calculate the annual inflation rate for any cryptocurrency or token, considering different unlock frequencies.

    Parameters:
    - circulating_supply (float): Current circulating supply of the token/coin.
    - new_supply_per_unlock (float): Number of new tokens/coins entering circulation per unlock period.
    - unlock_frequency (str): Frequency of the unlocks. Can be 'monthly', 'weekly', or 'quarterly'. Default is 'quarterly'.

    Returns:
    - float: Annual inflation rate as a percentage.
    """

    # Determine the number of unlocks per year based on the frequency
    if unlock_frequency == 'monthly':
        unlocks_per_year = 12
    elif unlock_frequency == 'weekly':
        unlocks_per_year = 52
    elif unlock_frequency == 'quarterly':
        unlocks_per_year = 4
    else:
        raise ValueError("Invalid unlock frequency. Choose from 'monthly', 'weekly', or 'quarterly'.")

    # Calculate annual new supply based on the unlock frequency
    annual_new_supply = new_supply_per_unlock * unlocks_per_year

    # Calculate annual inflation rate
    annual_inflation_rate = (annual_new_supply / circulating_supply) * 100
    return annual_inflation_rate

# Example usage
circulating_supply = 628_000_000       # For example: 628 million LINK
new_supply_per_unlock = 10_000_000     # For example: 10 million LINK per unlock
unlock_frequency = 'monthly'           # Options: 'monthly', 'weekly', or 'quarterly'

annual_inflation = calculate_annual_inflation(circulating_supply, new_supply_per_unlock, unlock_frequency)
print(f"Annual Inflation Rate: {annual_inflation:.2f}%")
