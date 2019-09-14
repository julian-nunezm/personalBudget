try:
    print("------------------------------------------------\n")
    print("Calculo Pago Total Compra de Tarjeta de Credito")
    print("------------------------------------------------\n")
    amount = 7000000
    months = [6, 12, 18, 24, 30, 36]
    interest = 0.029
    
    for month in months:
        print("Analisis para " + str(month) + " meses:")
        monthlyAmount = amount / month
        pendingAmount = amount
        totalInterestAmount = 0
        for n in range(month):
            interestAmount = pendingAmount * interest
            pendingAmount -= monthlyAmount
            totalInterestAmount += interestAmount
        print("Valor Cuota: " + str(f"{round(monthlyAmount,2):,}"))
        print("Total Intereses por Pagar: " + str(f"{round(totalInterestAmount,2):,}"))
        print("Porcentaje total de intereses pagados: " + str(round((totalInterestAmount/amount)*100,2)) + "%.")
        print("\n")
except Exception as e:
    print(f"Error: {str(e)}")
