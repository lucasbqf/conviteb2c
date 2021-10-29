from flask import Flask
from flask_restful import Api
from model.dbConnection import DBConnection

from resources.Invite import InviteClaim, InviteCreator, InvitePaid, Invites, inviteFinish

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)



@app.before_first_request
def criabanco():
    try:
        print('criando Banco de dados')
        dbconnection = DBConnection()
        dbconnection.createdb()
    except:
        print('banco de dados ja existe')

api.add_resource(InviteCreator, '/creat_invite')
api.add_resource(InvitePaid, '/update_invite_paid')
api.add_resource(InviteClaim, '/update_invite_claim')
api.add_resource(inviteFinish, '/update_invite_finished')


api.add_resource(Invites, '/all_invites')
#api.add_resource(InviteByUser, '/userinvite=<string:user_id>')


