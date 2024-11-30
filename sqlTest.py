import pymssql
fmConn = pymssql.connect(server="IKE")
fmCurr = fmConn.cursor
fmCurr.execute("select top 1 * from FinanceManager.dbo.refAccounts")
row = fmCurr.fetchone()
while row:
    print(row[0])
    row = fmCurr.fetchone()

fmConn.close

