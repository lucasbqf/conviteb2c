import sqlite3

class SqliteDB():


    def createDB(self):
        dbcon = sqlite3.connect('invite.db')
        cur = dbcon.cursor()
        cur.execute("CREATE TABLE invites( invited_user_uuid TEXT PRIMARY KEY,user_uuid TEXT,status INTEGER)")
        dbcon.commit()
        dbcon.close()


    def insertNewInvite(self,user_uuid,invited_user_uuid):
        dbcon = sqlite3.connect('invite.db')
        cur = dbcon.cursor()
        cur.execute("INSERT INTO invites VALUES(?,?,1)",(user_uuid,invited_user_uuid))
        dbcon.commit()
        dbcon.close()
    
    def updateInviteTo2(self,invited_user_uuid):
        """altera invite para o estatus 2 caso status for 1"""
        dbcon = sqlite3.connect('invite.db')
        cur = dbcon.cursor()
        cur.execute("UPDATE invites SET status = status +1 WHERE invited_user_uuid = ? and status = 1",(invited_user_uuid,))
        result = cur.rowcount
        dbcon.commit()
        dbcon.close()
        return result

    def updateInviteTo3(self,invited_user_uuid):
        """altera invite para o estatus 3 caso status for 2"""
        dbcon = sqlite3.connect('invite.db')
        cur = dbcon.cursor()
        cur.execute("UPDATE invites SET status = status +1 WHERE invited_user_uuid = ? and status = 2",(invited_user_uuid,))
        result = cur.rowcount
        dbcon.commit()
        dbcon.close()
        return result

    def updateInviteTo4(self,invited_user_uuid):
        """altera invite para o estatus 4 caso status for 3"""
        dbcon = sqlite3.connect('invite.db')
        cur = dbcon.cursor()
        cur.execute("UPDATE invites SET status = status +1 WHERE invited_user_uuid = ? and status = 3",(invited_user_uuid,))
        result = cur.rowcount
        dbcon.commit()
        dbcon.close()
        return result




    def getAllInvites(self):
        dbcon = sqlite3.connect('invite.db')
        cur = dbcon.cursor()
        cur.execute("SELECT * FROM invites")
        rows = cur.fetchall()
        dbcon.close()

        return rows

    def getAllInvitesByStatus(self,status):
        dbcon = sqlite3.connect('invite.db')
        cur = dbcon.cursor()
        cur.execute("SELECT * FROM invites WHERE status = ?",(status,))
        rows = cur.fetchall()
        dbcon.close()
        
        return rows

    def selectInvitedUser(self,invited_user_uuid):
        dbcon = sqlite3.connect('invite.db')
        cur = dbcon.cursor()
        cur.execute("SELECT * FROM invites WHERE invited_user_uuid = ?",(invited_user_uuid,))
        rows = cur.fetchall()
        dbcon.close()
        print(rows)
        return rows


    


