import sqlite3

class SqliteDB():


    def createDB(self):
        dbcon = sqlite3.connect('invite.db')
        cur = dbcon.cursor()
        cur.execute("CREATE TABLE invites( invited_user_uuid TEXT PRIMARY KEY,user_uuid TEXT,status INTEGER,pix_type INTEGER, pix_info TEXT, payer_uuid TEXT,receipt BLOB)")
        dbcon.commit()
        dbcon.close()


    def insertNewInvite(self,user_uuid,invited_user_uuid):
        dbcon = sqlite3.connect('invite.db')
        cur = dbcon.cursor()
        cur.execute("INSERT INTO invites VALUES(?,?,1,NULL,NULL,NULL,NULL)",(invited_user_uuid,user_uuid))
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

    def updateInviteTo3(self,invited_user_uuid,pix_type,pix_info):
        """altera invite para o estatus 3 caso status for 2"""
        dbcon = sqlite3.connect('invite.db')
        cur = dbcon.cursor()
        cur.execute("UPDATE invites SET status = status +1,pix_type=?, pix_info = ? WHERE invited_user_uuid = ? and status = 2",(pix_type,pix_info,invited_user_uuid))
        result = cur.rowcount
        dbcon.commit()
        dbcon.close()
        return result

    def updateInviteTo4(self,invited_user_uuid,payer_uuid,receipt):
        """altera invite para o estatus 4 caso status for 3"""
        dbcon = sqlite3.connect('invite.db')
        cur = dbcon.cursor()
        cur.execute("UPDATE invites SET status = status +1, receipt = ? , payer_uuid = ? WHERE invited_user_uuid = ? and status = 3",(receipt,payer_uuid,invited_user_uuid))
        result = cur.rowcount
        dbcon.commit()
        dbcon.close()
        return result


######### selects ###############

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
        cur.execute("SELECT * FROM invites WHERE user_uuid = ?",(invited_user_uuid,))
        rows = cur.fetchall()
        dbcon.close()
        return rows

    def selectInvitedUserAndStatus(self,invited_user_uuid,status):
        dbcon = sqlite3.connect('invite.db')
        cur = dbcon.cursor()
        cur.execute("SELECT * FROM invites WHERE user_uuid = ? AND  status = ? ",(invited_user_uuid,status))
        rows = cur.fetchall()
        dbcon.close()
        return rows

    


