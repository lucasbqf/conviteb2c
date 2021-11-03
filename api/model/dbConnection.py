

from api.model.sqlitedb import SqliteDB

class DBConnection():
    def __init__(self):
      self.db = SqliteDB()

    
    def createdb(self):
        self.db.createDB()


    def insertNewInvite(self,user_uuid,invited_user_uuid):
        self.db.insertNewInvite(user_uuid,invited_user_uuid)

    def updateInviteToStatus2(self,invited_user_uuid):
        '''da o update para o estatus pago, ou seja,
         o usuario convidado realizou o pagamento de alguma parcela da divida e que o convidou
         pode reenvidicar o premio do convite'''
        result = self.db.updateInviteTo2(invited_user_uuid)
        return result


    def updateInviteToStatus3(self,invited_user_uuid,pix_type,pix_info):
        '''da o update para o estatus reinvidicado, ou seja,
         após o convidado realizar o pagamento, o usuario seleciona a opção de reenvindicar premio do convite'''
        result = self.db.updateInviteTo3(invited_user_uuid,pix_type,pix_info)
        return result

    def updateInviteToStatus4(self,invited_user_uuid,payer_uuid,receipt):
        '''da o update para o estatus finalizado, ou seja,
         após o usuario realizar a renvindicação, o administrativo realiza o pagamento e alterna o status para finalizado'''
        result = self.db.updateInviteTo4(invited_user_uuid,payer_uuid,receipt )
        return result

    def getAllInvites(self):
        result = self.db.getAllInvites()
        return result
    def getAllInvitesByStatus(self,status):
        result = self.db.getAllInvitesByStatus(status)
        return result

    def getAllInvitesByUser(self,user_uuid):
        result = self.db.selectInvitedUser(user_uuid)
        return result

    def getInvitesByUserAndStatus(self,user_uuid,status):
        result = self.db.selectInvitedUserAndStatus(user_uuid,status)
        return result

