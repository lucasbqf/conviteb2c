import sqlite3
try:
        dbcon = sqlite3.connect('invite.db')
        cur = dbcon.cursor()
        cur.execute("UPDATE invites SET status = 2, pix_info = NULL, pix_type = NULL, payer_uuid = NULL, receipt = NULL")
        result = cur.rowcount
        dbcon.commit()
        dbcon.close()
        print("limpou status de todos os invites")
except Exception as error:
        print(error)
