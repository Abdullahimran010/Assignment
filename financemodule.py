def intrest_monthly(balance,annual_intrest_rate):
	intrest = balance*(annual_intrest_rate/1200)
	return intrest
	
def future_investment_value(investment_amount,monthly_intrest_rate,number_of_years):
	futurVal = investment_amount*((1+monthly_intrest_rate)**number_of_years)*12	
	return futurVal
