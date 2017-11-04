import os
import inspect
import sys
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from flask import request, json, abort
from flask_restful import Resource
import pprint
from app.models.models import Mentor


class MentorBot(Resource):
    def post(self):
        print ("i am posting")
        q_name = self.clean_response()
        # q_name = request.args.get('q', "")
        print ("----q name", q_name)
        if q_name:
            mentor = Mentor.query.filter(Mentor.stack.ilike('%{}%'.format(q_name)))
            if not mentor:
                return 'There is no mentor available at the moment in that stack'
            else:
                all_users = []
                for mentors in mentor:
                    all_users.append({"phone_number": mentors.phone_number,
                                      "full name": mentors.full_name})
                return all_users
        else:
            mentor = Mentor.query.all()
            all_users = []
            for mentors in mentor:
                all_users.append({"phone_number":mentors.phone_number,
                                  "full name":mentors.full_name,
                                  "stack":mentors.stack,
                                  "stack_details":mentors.stack_details})
            return all_users

    # def post(self):
    #     print("i am posting")
    #     if not request.json:
    #         abort(400)
    #     if not request.json['phone_number']:
    #         abort(400)
    #
    #     mentor = Mentor.query.filter_by(phone_number=request.json['phone_number']).first()
    #
    #     if mentor:
    #         return 'Sorry, you already exist in our database', 404
    #     else:
    #         full_name = request.json['full_name']
    #         phone_number = request.json['phone_number']
    #         stack = request.json['stack']
    #         stack_details = request.json['stack_details']
    #         mentor = Mentor(full_name, phone_number, stack, stack_details)
    #         Mentor.save(mentor)
    #         # db.session.add(mentor)
    #         # db.session.commit()
    #         return 'Welcome to Mentor bot {}, you have been added succesfully'.format(full_name), 201

    def clean_response(self):
        payload = request.get_data()
        print("----payload", payload)
        data = json.loads(payload)
        print("----data", data)
        if data['result']['action'] == '@searches':
            return data['result']['parameters']['searches']






