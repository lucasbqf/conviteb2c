from os import error
from flask_restful import Resource, reqparse

from api.model.dbConnection import DBConnection

class InviteCreator(Resource):
    dbconnection = DBConnection()
    """endpoint para criação de um convite no banco de dados, passando via json o user_id e o invited_user_id e criando 
    novo convite com o status 1(status registrado)"""    
    path_params = reqparse.RequestParser()
    path_params.add_argument('user_id',required = True, help= "user_id cannot be null")
    path_params.add_argument('invited_user_id',required = True, help= "invited_user_id cannot be null")
    def post(self):
        dados = self.path_params.parse_args()
        print(dados['user_id'])
        print(dados['invited_user_id'])
        try:
            self.dbconnection.insertNewInvite(dados['user_id'],dados['invited_user_id'])
            return {'message': " created invite from user_id:'{}' to invited_user_id: '{}'".format(dados['user_id'],dados['invited_user_id'])},200
        except Exception as error:
            print(error)
            return {'message': " failed to save  invite from user_id:'{}' to invited_user_id: '{}' maybe invited_user_id already exists or there's a problem with the DB \n {}".format(dados['user_id'],dados['invited_user_id'],error)},500


class InvitePaid(Resource):
    """realiza a atualização do status do convite encontrando-o pelo invited_user_id do status 1 para o estatus 2 estatus pago, pronto para quem convidou reenvidicar"""
    dbconnection = DBConnection()
    path_params = reqparse.RequestParser()
    path_params.add_argument('invited_user_id',required = True, help="invited_user_id cannot be null")
    def post(self):
        dados = self.path_params.parse_args()
        try:
            print("tentando update no usuario ="+ dados['invited_user_id'])
            result = self.dbconnection.updateInviteToStatus2(dados['invited_user_id'])
            if result== 1: 
                print("update ok")
                return{"message":"'{}' updated successfully ".format(dados['invited_user_id'])},200
            elif result == 0 :
                print("usuario nao existe ou nao pode ser dado update")
                return{"message":"'{}' don't exist or cannot be updated to status 2".format(dados['invited_user_id'])},404
                
        except Exception as error:
            print(error)
            return {"message": "Error:{}".format (error)},500

class InviteClaim(Resource):
    """realiza a atualização do status do convite encontrando-o pelo invited_user_id do status 2 para o estatus 3 estatus reinvidicado, pronto para o Administrativo realizar o Pagamento"""
    dbconnection = DBConnection()
    path_params = reqparse.RequestParser()
    path_params.add_argument('invited_user_id',required = True, help="invited_user_id cannot be null")
    path_params.add_argument('pix_type',required = True, help="pix_type cannot be null")
    path_params.add_argument('pix_info',required = True, help="pix_info cannot be null")
    def post(self):
        dados = self.path_params.parse_args()
        try:
            result = self.dbconnection.updateInviteToStatus3(dados['invited_user_id'],dados['pix_type'],dados['pix_info'])
            if result== 1: 
                return{"message":"'{}' updated successfully ".format(dados['invited_user_id'])},200
            elif result == 0 :
                return{"message":"'{}' don't exist or cannot be updated to status 3".format(dados['invited_user_id'])},404
        except Exception as error:
            return {"message": "Error:{}".format (error)},500

class inviteFinish(Resource):
    """realiza a atualização do status do convite encontrando-o pelo invited_user_id do status 3 para o estatus 4 estatus Finalizado, onde o valor ja foi reinvidicao pelo usuario e o administrativo realizou o pagamento"""
    dbconnection = DBConnection()
    path_params = reqparse.RequestParser()
    path_params.add_argument('invited_user_id',required = True, help="invited_user_id cannot be null")
    path_params.add_argument('payer_id',required = True, help="payer_uuid cannot be null")
    path_params.add_argument('receipt',required = True, help="you must include a receipt of payment")
    def post(self):
        dados = self.path_params.parse_args()
        try:
            result = self.dbconnection.updateInviteToStatus4(dados['invited_user_id'],dados['payer_id'],dados['receipt'])
            if result== 1: 
                return{"message":"'{}' updated successfully ".format(dados['invited_user_id'])},200
            elif result == 0 :
                return{"message":"'{}' don't exist or cannot be updated to status 4".format(dados['invited_user_id'])},404
        except Exception as error:
            return {"message": "Error:{}".format (error)},500


############----------endpoints para visualização dos convites----------############

class Invites(Resource):
    """ endpoint que retorna todos os convites com GET, caso seja um Post, retorna convites com status informado na requisição"""
    dbconnection = DBConnection()
    path_params = reqparse.RequestParser()
    path_params.add_argument('status')
    def get(self):
        try:
            results = self.dbconnection.getAllInvites()
            entries = []
            for result in results:
                entries.append(
                    {
                        'invited_user_id':result[0],
                        'user_id':result[1],
                        'status':result[2],
                        'pix_type':result[3],
                        'pix_info':result[4],
                        'payer_id':result[5],
                        'receipt':result[6]
                    }
                )
            return{"result": entries },200
        except Exception as error:
            return {"message": "Error:{}".format (error)},500

        
    def post(self):
        dados = self.path_params.parse_args()
        try:
            if dados['status'] != None: 
                if int(dados['status']) > 0 and int(dados['status']) < 5:
                    results = self.dbconnection.getAllInvitesByStatus(dados['status'])
                    entries = []
                    for result in results:
                        entries.append(
                            {
                                'invited_user_id':result[0],
                                'user_id':result[1],
                                'status':result[2],
                                'pix_type':result[3],
                                'pix_info':result[4],
                                'payer_id':result[5],
                                'receipt':result[6]
                            }
                        )
                    return{"result": entries },200
                else:
                    return {"message":"a status code is invalid"},400 
            else:
                return {"message":"a status code is required"},400
        except Exception as error:
            return {"message": "Error:{}".format (error)},500

class InviteByUser(Resource):
    """ endpoint que retorna todos os convites de um usuario com GET,
    caso seja um Post, retorna convites do usuario com status informado na requisição"""
    dbconnection = DBConnection()
    path_params = reqparse.RequestParser()
    path_params.add_argument('status')

    def get(self,user_id):
        try:
            results = self.dbconnection.getAllInvitesByUser(user_id)
            entries = []
            for result in results:
                entries.append(
                    {
                        'invited_user_id':result[0],
                        'user_id':result[1],
                        'status':result[2]
                    }
                )
            return{"result": entries },200
        except Exception as error:
            return {"message": "Error:{}".format (error)},500


    def post(self,user_id):
        dados = self.path_params.parse_args()
        try:
            if dados['status'] != None: 
                if int(dados['status']) > 0 and int(dados['status']) < 5:
                    results = self.dbconnection.getInvitesByUserAndStatus(user_id,dados['status'])
                    entries = []
                    for result in results:
                        entries.append(
                            {
                                'invited_user_id':result[0],
                                'user_id':result[1],
                                'status':result[2]
                            }
                        )
                    return{"result": entries },200
                else:
                    return {"message":"a status code is invalid"},400 
            else:
                return {"message":"a status code is required"},400

        except Exception as error:
            return {"message": "Error:{}".format (error)},500



