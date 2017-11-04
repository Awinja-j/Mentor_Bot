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
            if q_name == 'search':
                mentor = Mentor.query.filter(Mentor.stack.ilike('%{}%'.format(q_name)))
                print ("------mentor", mentor)
                if not mentor:
                    return 'There is no mentor available at the moment in that stack', 400
                else:
                    all_users = []
                    for mentors in mentor:
                        all_users.append({"phone_number": mentors.phone_number,
                                          "full name": mentors.full_name})
                    return all_users, 200

            elif type(q_name) == list:
                if len(q_name) == 5:
                    name = q_name[0] + " " + q_name[1]
                    phone_number = q_name[2]
                    stack = q_name[3]
                    stack_details = q_name[4]
                    check_mentor = Mentor.query.filter(Mentor.phone_number.ilike('%{}%'.format(phone_number)))
                    if check_mentor:
                        return "Sorry your already registered as a mentor", 200
                    mentor= Mentor(name, phone_number, stack, stack_details)
                    mentor.save()
                    return "Thanks for availing yourself as a mentor", 200
                else:
                    name = q_name[0] + " " + q_name[1]
                    phone_number = q_name[2]
                    stack = q_name[3]
                    check_mentor = Mentor.query.filter(Mentor.phone_number.ilike('%{}%'.format(phone_number)))
                    if check_mentor:
                        return "Sorry your already registered as a mentor", 200
                    mentor = Mentor(name, phone_number, stack)
                    mentor.save()
                    return "Thanks for availing yourself as a mentor", 200

        mentor = Mentor.query.all()
        all_users = []
        for mentors in mentor:
            all_users.append({"phone_number":mentors.phone_number,
                                  "full name":mentors.full_name,
                                  "stack":mentors.stack,
                                  "stack_details":mentors.stack_details})
        return all_users, 200


    def clean_response(self):
        payload = request.get_data()
        print("----payload", payload)
        data = json.loads(payload)
        print("----data", data)
        if data['result']['action'] == '@searches':
            return data['result']['parameters']['searches']
        elif data['result']['action'] == '@mentor_details':
            return data['result']['parameters']['mentor_details']
        else:
            return "Sorry we didn't understand your query.", 404








