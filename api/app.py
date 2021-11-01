from flask import Flask
from flask_restful import Api
from api.model.dbConnection import DBConnection

from api.resources.Invite import InviteClaim, InviteCreator, InvitePaid, Invites, inviteFinish,InviteByUser

def create_app():
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

    @app.route("/")
    def index():
        return "enpoints: <br> /create_invite , /update_invite_paid, /update_invite_claim, /update_invite_finished, /get_all_invites, /get_userinvite=<string:user_id>"


    api.add_resource(InviteCreator, '/create_invite')
    api.add_resource(InvitePaid, '/update_invite_paid')
    api.add_resource(InviteClaim, '/update_invite_claim')
    api.add_resource(inviteFinish, '/update_invite_finished')


    api.add_resource(Invites, '/get_all_invites')
    api.add_resource(InviteByUser, '/get_userinvite=<string:user_id>')


    return app
